# AI Testing Concepts


AI Testing Concepts

## Bias

**Simple Explanation:**

Bias means the system is unfair — it favors one type of input over another.

**🧠 Real-Life Example:**

Imagine a school that only gives admission to students from one city, even though students from other cities are equally qualified. That’s unfair — that’s bias.

**🧪 Real-Time QA Example:**

You’re testing a job portal. You notice that resumes with male names are selected more often than female names, even when qualifications are the same.

**Defect Report:** 

System favors male candidates — possible gender bias.

## Fairness

**Simple Explanation:**

Fairness means the system treats everyone equally, no matter their background.

**🧠 Real-Life Example:**

A fair teacher gives marks based on answers, not based on who the student is.

**🧪 Real-Time QA Example:**

You test a loan approval system. You enter the same income and credit score for two users — one from a metro city and one from a rural area. If only the metro user gets approved, that’s unfair.

**Defect Report:** 

Loan approval logic may be unfair based on location.

## Explainability

**Simple Explanation:**

Explainability means the system should tell you why it made a decision.

**🧠 Real-Life Example:**

If your bank rejects your loan, you want to know why — was it your income, credit score, or something else?

**🧪 Real-Time QA Example:**

You test a fraud detection system. It blocks a transaction but doesn’t say why.

**Defect Report:** 

System should explain reason for blocking — missing explainability.

## Overfitting

**Simple Explanation:**

Overfitting means the system is too smart for its training data but fails in real life.

**🧠 Real-Life Example:**

A student memorizes answers from one book. In the exam, questions are different — and the student fails.

**🧪 Real-Time QA Example:**

You test a chatbot. It answers perfectly for known questions but gives wrong answers for new ones.

**Defect Report:** 

Chatbot performs well on trained data but fails on new inputs — possible overfitting.

## Underfitting

**Simple Explanation:**

Underfitting means the system didn’t learn enough — it performs badly everywhere.

**🧠 Real-Life Example:**

A student barely studies and fails both practice tests and final exams.

**🧪 Real-Time QA Example:**

You test a recommendation engine. It gives random suggestions — even for known user preferences.

**Defect Report:** 

System not learning patterns — possible underfitting.

**🧠 Memory Tip for Interviews:**

You can say:

“I test AI systems like any smart software. I check if they’re fair, if they explain their decisions, and if they behave consistently with both known and new data. I don’t use deep AI terms — I focus on real-world behavior.”