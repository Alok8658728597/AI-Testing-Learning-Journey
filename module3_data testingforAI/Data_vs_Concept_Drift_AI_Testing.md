
# 🧠 Data Drift vs Concept Drift in AI Testing

This guide explains two critical concepts in AI Testing — Data Drift and Concept Drift — with clear definitions, examples, detection methods, and QA relevance.

---

## 🔄 What is Data Drift?
**Data Drift** occurs when the distribution of input data changes over time, but the relationship between input and output remains the same.

### 📊 Example:
A loan approval model was trained mostly on salaried employees. Over time, more freelancers apply. The model logic is still valid, but input data has shifted.

> ✅ Model logic is fine, input data changed → Data Drift

---

## 🔁 What is Concept Drift?
**Concept Drift** happens when the relationship between input and output changes — meaning the model's logic becomes outdated.

### 📊 Example:
A spam detection model was trained on emails with "Win a prize". Spammers now use "Exclusive deal". The model fails to detect new spam.

> ❌ Input data is similar, but output meaning changed → Concept Drift

---

## 🔍 Key Differences

| Feature            | Data Drift                          | Concept Drift                        |
|--------------------|--------------------------------------|---------------------------------------|
| What changes?      | Input data distribution              | Input-output relationship             |
| Model performance  | May degrade slowly                   | Can degrade rapidly                   |
| Fix                | Monitor input features               | Retrain model with updated labels     |

---

## 🧪 How to Detect Data Drift

### ✅ 1. Compare Feature Distributions
- Kolmogorov–Smirnov (KS) Test
- Population Stability Index (PSI)
- Histogram comparison

### ✅ 2. Use Tools
- Evidently AI
- River
- Alibi Detect

### 📘 QA Example:
You compare age distribution in training vs. live data. PSI > 0.25 → significant drift.

---

## 🔍 How to Detect Concept Drift

### ✅ 1. Monitor Model Accuracy
- Track accuracy, precision, recall over time
- Sudden drop = possible Concept Drift

### ✅ 2. Use Drift Detection Algorithms
- DDM (Drift Detection Method)
- EDDM (Early Drift Detection Method)
- ADWIN (Adaptive Windowing)

### ✅ 3. Retrain with Updated Labels

### 📘 QA Example:
Spam model accuracy drops from 95% to 70%. You confirm input data is stable → Concept Drift suspected.

---

## 🧰 Tools Used by QA Engineers

| Technique        | Used by QA | Used by Dev | Notes |
|------------------|------------|-------------|-------|
| KS Test          | ✅         | ✅          | Compare distributions |
| PSI              | ✅         | ✅          | Quantify drift |
| Histogram        | ✅         | ✅          | Visual inspection |

---

## 💡 Interview Tip
> "As a QA engineer, I use KS Test, PSI, and histogram comparison to detect Data Drift. For Concept Drift, I monitor model accuracy and use DDM or EDDM algorithms."

---

## 📘 Summary
- Data Drift = input data changes
- Concept Drift = model logic becomes outdated
- QA engineers play a key role in detecting and reporting drift

Use this guide to revise and explain confidently in interviews.
