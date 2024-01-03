## exec(open("scripts/train-bag-of-words.py").read())


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, precision_recall_curve

import torch
import csv
import numpy

## categories: ewas, methods, dnamage, prediction, epigenetics, *
category = "*"

cases = set()
with open("data/papers.csv",mode="r", encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if category == "*" or row["Category"] == category:
            cases.add(row["Paper ID"])

labels = []
examples = []
with open("data/ignore.csv",mode="r", encoding="ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        example = row["source"]+". "+row["title"]+". "+row["abstract"]
        if len(example.split()) > 10:
            if row["pmid"] in cases:
                labels.append(1)
            else:
                labels.append(0)
            examples.append(example)


if False: 
    pmax = 1000 
    examples = [ examples[i] for i in range(pmax) ]
    labels = [ labels[i] for i in range(pmax) ]

# Step 1: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(examples, labels, test_size=0.2, random_state=42)

# Step 2: Create a bag-of-words representation of the text
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_train = numpy.array(X_train.todense())

# Step 3: Train a classifier (Naive Bayes in this case)
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Step 4: Make predictions on the test set
X_test = vectorizer.transform(X_test)
X_test = numpy.array(X_test.todense())
predictions = classifier.predict(X_test)

# Step 5: Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")

probabilities = classifier.predict_proba(X_test)
probabilities = [ x[1]/sum(x) for x in probabilities ]

auc = roc_auc_score(y_test, probabilities,multi_class="ovr")
print(f"AUC: {auc:.2f}")

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

## category == "*"
# Accuracy: 0.91
# AUC: 0.85
# Classification Report:
#               precision    recall  f1-score   support

#            0       0.96      0.95      0.95      3950
#            1       0.41      0.47      0.44       307

#     accuracy                           0.91      4257
#    macro avg       0.68      0.71      0.70      4257
# weighted avg       0.92      0.91      0.92      4257

# Probability of good paper > 3.28E-23
# retrieves 85.7% of good papers
# along with 5.2 bad papers per good paper.
# With no model, this increases to 11.4 bad papers

## category == "ewas"
# Accuracy: 0.97
# AUC: 0.94
# Classification Report:
#               precision    recall  f1-score   support

#            0       0.98      0.99      0.99      4122
#            1       0.57      0.47      0.52       135

#     accuracy                           0.97      4257
#    macro avg       0.77      0.73      0.75      4257
# weighted avg       0.97      0.97      0.97      4257

# Probability of good paper > 7.73E-39
# retrieves 94.8% of good papers
# along with 7.4 bad papers per good paper.
# With no model, this increases to 15.8 bad papers


## apply to a set of candidate papers in candidates.csv
with open("candidates.csv",mode="r", encoding="ISO-8859-1") as infile:
    with open("candidates-with-probs.csv",mode="w", encoding="ISO-8859-1") as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile,fieldnames=reader.fieldnames + ["probs"])
        writer.writeheader()
        for row in reader:
            new_paper = row["source"]+". "+row["title"]+". "+row["abstract"]
            new_paper = vectorizer.transform([new_paper])
            new_paper = numpy.array(new_paper.todense())
            new_prob = classifier.predict_proba(new_paper)[0]
            new_prob = new_prob[1]/sum(new_prob)
            row["probs"] = new_prob
            writer.writerow(row)
