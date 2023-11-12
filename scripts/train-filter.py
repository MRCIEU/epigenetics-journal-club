from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Sample positive and negative examples
positive_examples = ["I love this product!", "This is amazing.", "Great service."]
negative_examples = ["Terrible experience.", "Not satisfied at all.", "Waste of money."]

# Labels for positive and negative examples
positive_labels = [1] * len(positive_examples)
negative_labels = [0] * len(negative_examples)

# Combine positive and negative examples and labels
all_examples = positive_examples + negative_examples
all_labels = positive_labels + negative_labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(all_examples, all_labels, test_size=0.2, random_state=42)

# Load pre-trained DistilBERT model and tokenizer
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased')

# Tokenize and encode the training data
X_train_encoded = tokenizer(X_train, truncation=True, padding=True, return_tensors='pt')
X_test_encoded = tokenizer(X_test, truncation=True, padding=True, return_tensors='pt')

# Train the model
model.train()
labels = torch.tensor(y_train)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

for epoch in range(3):  # You might want to adjust the number of epochs
    optimizer.zero_grad()
    outputs = model(**X_train_encoded, labels=labels)
    loss = outputs.loss
    loss.backward()
    optimizer.step()

# Evaluate the model
model.eval()
with torch.no_grad():
    outputs = model(**X_test_encoded)
    predictions = torch.argmax(outputs.logits, dim=1).numpy()

# Evaluate the performance of the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report
print("Classification Report:")
print(classification_report(y_test, predictions))

# Example usage
new_example = ["This is a fantastic product!"]
new_example_encoded = tokenizer(new_example, truncation=True, padding=True, return_tensors='pt')
with torch.no_grad():
    new_example_output = model(**new_example_encoded)
    new_example_prediction = torch.argmax(new_example_output.logits, dim=1).item()

if new_example_prediction == 1:
    print("Prediction: Positive")
else:
    print("Prediction: Negative")
