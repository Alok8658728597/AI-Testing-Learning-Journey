# Confusion Matrix Explained with Spam Filter Example
## 📊 What is a Confusion Matrix?
It’s a table used to evaluate how well a classification model (like a spam filter) is performing. It compares the actual labels vs the predicted labels.
## 📧 Spam Filter Example
## 🎯 Visual Summary

|                | Predicted Spam | Predicted Not Spam |
|----------------|----------------|---------------------|
| Actual Spam    | TP             | FN                  |
| Actual Not Spam| FP             | TN                  |

## 🧠 What Each Term Means
TP (True Positive): Spam email correctly marked as spam.
FP (False Positive): Good email wrongly marked as spam.
FN (False Negative): Spam email wrongly marked as safe.
TN (True Negative): Good email correctly marked as safe.
## 🎯 Easy Trick to Remember
FP (False Positive) = False Alarm
The system thinks it's spam, but it's not.
Like wrongly blocking a genuine email.
FN (False Negative) = Missed Detection
The system thinks it's safe, but it's actually spam.
Like letting a scam email into your inbox.