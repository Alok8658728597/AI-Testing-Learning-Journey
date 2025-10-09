# Module 1: AI Testing Fundamentals

## What is AI Testing and Why Is It Different from Traditional Testing?

AI Testing involves validating systems that use artificial intelligence or machine learning. Unlike traditional software testing, AI testing focuses on:

- Testing AI-based systems (e.g., chatbots, recommendation engines, image classifiers)
- Using AI tools to assist in testing traditional software
- Validating model predictions (classification, regression)
- Testing NLP responses (chatbots, translation)
- Checking image recognition accuracy (vision models)
- Monitoring model drift over time
- Evaluating fairness and bias in predictions
- Using AI tools to auto-generate test cases or detect flaky tests

🎯 **Goal**: Understand what you're testing and why.

---

## Classification Models

**Description**: Predicts a category or label from input data.

**Examples**:
- Spam Detection: Email is classified as Spam or Not Spam.
- Disease Prediction: Patient is Diabetic or Non-Diabetic.
- Sentiment Analysis: Review is Positive, Negative, or Neutral.

**QA Relevance**:
- Bug classification (UI bug, API bug, etc.)
- Test case prioritization (high-risk vs low-risk)

---

## Regression Models

**Description**: Predicts a continuous numeric value.

**Examples**:
- House Price Prediction: Predict price based on features.
- Stock Price Forecasting: Estimate future stock value.
- Temperature Prediction: Predict tomorrow’s temperature.

**QA Relevance**:
- Performance testing (e.g., response time prediction)
- Test data generation with realistic values

---

## NLP (Natural Language Processing) Models

**Description**: Processes and understands human language.

**Examples**:
- Chatbots: GenAI assistants like ChatGPT.
- Language Translation: English to Hindi.
- Text Summarization: Summarize long articles.

**QA Relevance**:
- Chatbot testing
- Test case generation from requirements
- Multilingual support validation

---

## Vision Models (Computer Vision)

**Description**: Analyzes and understands images or videos.

**Examples**:
- Face Recognition: Unlock phone using face.
- Object Detection: Detect cars, pedestrians.
- Medical Imaging: Detect tumors in X-rays.

**QA Relevance**:
- UI layout comparison
- OCR validation (e.g., scanned forms)

---

## Generative Models

**Description**: Generates new data similar to training data.

**Examples**:
- Image Generation: Create images from text.
- Text Generation: Write articles or code.
- Music Generation: Compose music.

**QA Relevance**:
- Test data generation
- Mock API response creation
- AI-generated content validation

---

## Reinforcement Learning Models

**Description**: Learns by trial and error to maximize rewards.

**Examples**:
- Game Playing: AI learns to play chess.
- Robotics: Robot learns to walk.
- Self-driving Cars: Learn to drive safely.

**QA Relevance**:
- RPA testing
- Game testing
- Self-learning system validation
