# Spam Filter Example: TP, FP, FN, TN, Accuracy, Precision, Recall, F1 Score

## Scenario: Testing a Spam Filter

You test 10 emails. Some are actually spam, some are not spam. The AI model tries to predict which ones are spam.

## Email Classification Results

### Count Summary

- **TP (True Positive)** = 3 → Spam correctly identified

- **FP (False Positive)** = 2 → Not spam but wrongly flagged

- **FN (False Negative)** = 2 → Spam missed

- **TN (True Negative)** = 3 → Not spam and correctly ignored

## Metrics and Definitions

### Accuracy

- **What It Means**: Overall correctness

- **Formula**: `(TP + TN) / Total`

- **Value**: 60%

### Precision

- **What It Means**: Out of predicted spam, how many were actually spam

- **Formula**: `TP / (TP + FP)`

- **Value**: 60%

### Recall

- **What It Means**: Out of actual spam, how many were caught

- **Formula**: `TP / (TP + FN)`

- **Value**: 60%

### F1 Score

- **What It Means**: Balance between precision and recall

- **Formula**: `2 × (P × R) / (P + R)`

- **Value**: 60%

## Easy Way to Remember
