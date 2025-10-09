# 📘 Module 1: AI Testing Fundamentals

What is AI/ML?

What is an AI model?

Types of AI models (classification, regression, NLP, vision)

Classification Models

Description: Predicts a category or label from input data.

Examples:

Spam Detection: Email is classified as Spam or Not Spam.

Disease Prediction: Patient is Diabetic or Non-Diabetic.

Sentiment Analysis: Review is Positive, Negative, or Neutral.

QA Relevance:

Bug classification (UI bug, API bug, etc.)

Test case prioritization (high-risk vs low-risk)

Regression Models

Description: Predicts a continuous numeric value.

Examples:

House Price Prediction: Predict price based on features.

Stock Price Forecasting: Estimate future stock value.

Temperature Prediction: Predict tomorrow’s temperature.

QA Relevance:

Performance testing (e.g., response time prediction)

Test data generation with realistic values

NLP (Natural Language Processing) Models

Description: Processes and understands human language.

Examples:

Chatbots: GenAI assistants like ChatGPT.

Language Translation: English to Hindi.

Text Summarization: Summarize long articles.

QA Relevance:

Chatbot testing

Test case generation from requirements

Multilingual support validation

Vision Models (Computer Vision)

Description: Analyzes and understands images or videos.

Examples:

Face Recognition: Unlock phone using face.

Object Detection: Detect cars, pedestrians.

Medical Imaging: Detect tumors in X-rays.

QA Relevance:

UI layout comparison

OCR validation (e.g., scanned forms)

Generative Models

Description: Generates new data similar to training data.

Examples:

Image Generation: Create images from text.

Text Generation: Write articles or code.

Music Generation: Compose music.

QA Relevance:

Test data generation

Mock API response creation

AI-generated content validation

Reinforcement Learning Models

Description: Learns by trial and error to maximize rewards.

Examples:

Game Playing: AI learns to play chess.

Robotics: Robot learns to walk.

Self-driving Cars: Learn to drive safely.

QA Relevance:

RPA testing

Game testing

Self-learning system validation

What is AI testing and why is it different from traditional testing?   Testing AI-based systems (like chatbots, recommendation engines, image classifiers, etc.)

  Or using AI tools to assist in testing traditional software

  Validate model predictions (classification, regression)

  Test NLP responses (chatbots, translation)

  Check image recognition accuracy (vision models)

  Monitor model drift over time

  Evaluate fairness and bias in predictions

  Use AI tools to auto-generate test cases or detect flaky tests

📌 Goal: Understand what you're testing and why.


---

## 🧪 Easy Steps for QA Testers to Practice Each Model Type

### 🔹 Classification Models
1. Understand the output is a **label** (e.g., Spam or Not Spam).
2. Use public APIs like sentiment analysis or spam detection.
3. Create test cases with different inputs and verify predicted labels.
4. Validate edge cases (e.g., empty input, mixed language).

### 🔹 Regression Models
1. Understand the output is a **number** (e.g., price, temperature).
2. Use a house price prediction API or dataset.
3. Feed known inputs and compare predicted vs expected values.
4. Check for outliers and prediction consistency.

### 🔹 NLP Models
1. Use tools like ChatGPT, Google Translate, or Hugging Face APIs.
2. Test for grammar correction, translation, summarization.
3. Validate chatbot responses for intent and tone.
4. Check multilingual support and edge cases.

### 🔹 Vision Models
1. Use image classification or object detection APIs (e.g., Google Vision).
2. Upload test images and verify detected objects or labels.
3. Test for blurry, rotated, or partial images.
4. Validate OCR output from scanned forms.

### 🔹 Generative Models
1. Use tools like DALL·E (image generation) or ChatGPT (text generation).
2. Provide prompts and validate the quality of generated content.
3. Check for hallucinations or irrelevant outputs.
4. Use generated data for mock testing.

### 🔹 Reinforcement Learning Models
1. Understand these models learn by trial and error.
2. Explore open-source environments like OpenAI Gym.
3. Observe how the model improves over time.
4. Validate reward logic and behavior consistency.

---

## 🎯 Goal
Understand what you're testing and how to validate AI model behavior from a QA perspective.
