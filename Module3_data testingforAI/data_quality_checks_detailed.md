
# Data Quality Checks in AI Testing

Understanding data quality is essential for building reliable AI models. This guide explains each type of data quality check with simple, real-world examples for QA engineers.

---

## ✅ What Are Data Quality Checks?

Data quality checks are rules or validations applied to datasets before training or testing AI models. They help ensure the data is:
- Complete
- Accurate
- Consistent
- Valid
- Unique
- Timely

---

## 🔍 Why Are Data Quality Checks Important?

| Problem if Ignored         | Impact on AI Model                          |
|----------------------------|---------------------------------------------|
| Missing values             | Model confusion, inaccurate predictions     |
| Incorrect formats          | Errors during training                      |
| Duplicates                 | Overfitting, biased learning                |
| Outdated data              | Irrelevant predictions                      |
| Inconsistent units         | Misinterpretation of features               |
| Biased data                | Unfair or unethical decisions               |

---

## ✅ Types of Data Quality Checks with Examples

### 1. Completeness
**Check**: Are all required fields present?
- **Bad Data**:
  ```json
  { "name": "Alok", "income": "", "credit_score": 750 }
  ```
- **Issue**: Missing income field.
- **QA Action**: Check for empty or null fields.

### 2. Accuracy
**Check**: Are values realistic and correct?
- **Bad Data**:
  ```json
  { "size": -1200, "location": "Bangalore", "price": 5000000 }
  ```
- **Issue**: Negative house size.
- **QA Action**: Validate numeric ranges.

### 3. Consistency
**Check**: Are formats and units consistent?
- **Bad Data**:
  ```json
  { "salary": "50000 INR" }, { "salary": "600 USD" }
  ```
- **Issue**: Mixed currencies.
- **QA Action**: Standardize units.

### 4. Validity
**Check**: Do values follow expected formats?
- **Bad Data**:
  ```json
  { "email": "alokgmail.com" }
  ```
- **Issue**: Invalid email format.
- **QA Action**: Use regex to validate formats.

### 5. Uniqueness
**Check**: Are there duplicate records?
- **Bad Data**: Same transaction ID repeated.
- **Issue**: Model may learn wrong patterns.
- **QA Action**: Remove duplicate rows.

### 6. Timeliness
**Check**: Is the data up-to-date?
- **Bad Data**: Using customer data from 2015.
- **Issue**: Outdated preferences.
- **QA Action**: Use recent records only.

---

## 🧪 Real-Time QA Scenario: AI Chatbot

| Check         | What to Look For                              |
|---------------|-----------------------------------------------|
| Completeness  | Every query must have a response              |
| Accuracy      | No corrupted or gibberish text                |
| Consistency   | Same language and punctuation style           |
| Validity      | Proper sentence structure                     |
| Uniqueness    | No duplicate conversations                    |
| Timeliness    | Use recent queries, not outdated ones         |

---

## ✅ Summary Table

| Check Type     | What It Means                          | QA Example                          |
|----------------|----------------------------------------|-------------------------------------|
| Completeness   | No missing values                      | Income field must not be empty      |
| Accuracy       | Values must be realistic                | Age cannot be 200                   |
| Consistency    | Same format across records              | All salaries in INR                 |
| Validity       | Values follow rules                     | Email must contain “@”              |
| Uniqueness     | No duplicate entries                    | Same transaction ID only once       |
| Timeliness     | Data is recent                          | Use 2025 data, not 2015             |

---

Data quality checks are the foundation of trustworthy AI. QA engineers ensure that the data used is clean, fair, and ready for model training.
