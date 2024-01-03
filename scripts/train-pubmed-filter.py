## exec(open("scripts/train-pubmed-filter.py").read())

## 36% of ram needed when 1000 abstracts analysed!
## 8% for 4000 journals/titles
## 45% for 20K journals/titles and takes 20 minutes

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, precision_recall_curve
import torch
import csv
import numpy

cases = set()
with open("data/papers.csv",mode="r", encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cases.add(row["Paper ID"])

labels = []
examples = []
with open("data/ignore.csv",mode="r", encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        example = row["source"]+". "+row["title"]#+". "+row["abstract"]
        if len(example.split()) > 10:
            if row["pmid"] in cases:
                labels.append(1)
            else:
                labels.append(0)
            examples.append(example)


if False: 
    pmax = 4000 
    examples = [ examples[i] for i in range(pmax) ]
    labels = [ labels[i] for i in range(pmax) ]

pretrained_model_name = "microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext"

tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name) 
    
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(examples, labels, test_size=0.2, random_state=42)

# Tokenize and encode the training data
X_train_encoded = tokenizer(X_train, truncation=True, padding=True, max_length=512, add_special_tokens=True, return_tensors='pt')
X_test_encoded = tokenizer(X_test, truncation=True, padding=True, max_length=512, add_special_tokens=True, return_tensors='pt')

model = AutoModelForSequenceClassification.from_pretrained(
    pretrained_model_name, 
    num_labels=2)

# Train the model
model.train()
y_train = torch.tensor(y_train)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

for epoch in range(5):  # optimal is usually between 1 and 10
    optimizer.zero_grad()
    outputs = model(**X_train_encoded, labels=y_train)
    loss = outputs.loss
    loss.backward()
    optimizer.step()

    
# Evaluate the model
model.eval()
with torch.no_grad():
    outputs = model(**X_test_encoded)

predictions = torch.argmax(outputs.logits, dim=1).numpy()
probabilities = [ x.numpy() for x in torch.sigmoid(outputs.logits) ]
probabilities = [ x[1]/sum(x) for x in probabilities ]

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

auc = roc_auc_score(y_test, probabilities)
print(f"AUC: {auc:.2f}")

# Display classification report
print("Classification Report:")
print(classification_report(y_test, predictions))


## we need to get nearly all the good papers
## i.e. recall needs to be near 100%
## but we don't want to have to look at a lot of bad papers
## i.e. precision should be high enough 
## (for every good paper, we'll need to look at 1/precision-1 bad papers)
precision, recall, thresholds = precision_recall_curve(y_test, probabilities)

min_recall = 0.85
min_improvement_factor = 2

current_bad_per_good = 1/precision[0]-1
min_precision = min_improvement_factor/(current_bad_per_good+1) 

indices = [i for i in range(len(recall)) if recall[i] > min_recall and precision[i] >= min_precision]

if len(indices) == 0:
    print("Minimum recall and improvement are not possible")

max_recall = max([recall[i] for i in indices])
index = [i for i in indices if recall[i] == max_recall][0]

print(f"Probability of good paper > {thresholds[index]:.2E}")
print(f"retrieves {recall[index]*100:0.1f}% of good papers")
print(f"along with {1/precision[index]-1:0.1f} bad papers per good paper.")
print(f"With no model, this increases to {1/precision[0]-1:0.1f} bad papers")


# Example usage
new_example = examples[36:40]
new_example_encoded = tokenizer(new_example, truncation=True, padding=True, max_length=512, add_special_tokens=True, return_tensors='pt')

with torch.no_grad():
    new_output = model(**new_example_encoded)
new_probs = [ x.numpy() for x in torch.sigmoid(new_output.logits) ]
new_probs = [ x[1]/sum(x) for x in new_probs ]
list(zip(labels[36:40].numpy(),new_probs))










https://huggingface.co/docs/transformers/v4.18.0/en/performance


from pynvml import *


def print_gpu_utilization():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(handle)
    print(f"GPU memory occupied: {info.used//1024**2} MB.")


def print_summary(result):
    print(f"Time: {result.metrics['train_runtime']:.2f}")
    print(f"Samples/second: {result.metrics['train_samples_per_second']:.2f}")
    print_gpu_utilization()


default_args = {
    "output_dir": "tmp",
    "evaluation_strategy": "steps",
    "num_train_epochs": 1,
    "log_level": "error",
    "report_to": "none",
}

training_args = TrainingArguments(
    per_device_train_batch_size=1,
    gradient_accumulation_steps=4, ## calculate gradients in 4 steps rather than 1
    gradient_checkpointing=True, ## recompute activations rather than store them
    fp16=True, ## use 16-bit instead of 32-bit for floats
    **default_args,
)

### quantizing to reduce memory 
import bitsandbytes as bnb
from torch import nn
from transformers.trainer_pt_utils import get_parameter_names

decay_parameters = get_parameter_names(model, [nn.LayerNorm])
decay_parameters = [name for name in decay_parameters if "bias" not in name]
optimizer_grouped_parameters = [
    {
        "params": [p for n, p in model.named_parameters() if n in decay_parameters],
        "weight_decay": training_args.weight_decay,
    },
    {
        "params": [p for n, p in model.named_parameters() if n not in decay_parameters],
        "weight_decay": 0.0,
    },
]

optimizer_kwargs = {
    "betas": (training_args.adam_beta1, training_args.adam_beta2),
    "eps": training_args.adam_epsilon,
}
optimizer_kwargs["lr"] = training_args.learning_rate
adam_bnb_optim = bnb.optim.Adam8bit(
    optimizer_grouped_parameters,
    betas=(training_args.adam_beta1, training_args.adam_beta2),
    eps=training_args.adam_epsilon,
    lr=training_args.learning_rate,
)

from accelerate import Accelerator
from torch.utils.data.dataloader import DataLoader

dataloader = DataLoader(ds, batch_size=training_args.per_device_train_batch_size)

if training_args.gradient_checkpointing:
    model.gradient_checkpointing_enable()

accelerator = Accelerator(fp16=training_args.fp16)
model, optimizer, dataloader = accelerator.prepare(model, adam_bnb_optim, dataloader)

model.train()
for step, batch in enumerate(dataloader, start=1):
    loss = model(**batch).loss
    loss = loss / training_args.gradient_accumulation_steps
    accelerator.backward(loss)
    if step % training_args.gradient_accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()


print_gpu_utilization()
