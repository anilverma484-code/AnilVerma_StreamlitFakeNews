# 📰 Fake News Classifier

A simple **Machine Learning + Streamlit** web application that classifies a news statement as **Likely REAL** or **Likely FAKE** using **TF-IDF text representation** and **Logistic Regression**.

## 🚀 Project Overview

This project demonstrates how Natural Language Processing (NLP) and Machine Learning can be used to build a simple text classification application.

The application:

1. Accepts a news article or statement from the user.
2. Converts the text into numerical features using **TF-IDF**.
3. Uses a **Logistic Regression** model for classification.
4. Displays the prediction through an interactive Streamlit interface.

## 🧠 Technologies Used

* **Python**
* **Streamlit** – Web application interface
* **Scikit-learn** – Machine Learning
* **TF-IDF Vectorizer** – Converts text into numerical features
* **Logistic Regression** – Classification algorithm

## 📂 Project Structure

```text
fake-news-classifier/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the complete Python code for the Streamlit application, including:

* Training data
* TF-IDF vectorization
* Logistic Regression model
* Streamlit user interface
* News prediction

### `requirements.txt`

Contains the Python packages required to run the application.

```text
streamlit
scikit-learn
```

## ⚙️ How to Run Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/fake-news-classifier.git
```

### Step 2: Open the project folder

```bash
cd fake-news-classifier
```

### Step 3: Install the required packages

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your web browser.

## 🔍 How the Model Works

### 1. Training Data

The application contains a small sample dataset consisting of news statements labelled as:

```text
0 = Real
1 = Fake
```

### 2. TF-IDF

The **TF-IDF (Term Frequency–Inverse Document Frequency)** technique converts text into numerical features that can be processed by a machine-learning algorithm.

### 3. Logistic Regression

The Logistic Regression model learns patterns from the labelled training examples and predicts whether new text is likely to belong to the **Real** or **Fake** category.

### 4. Prediction

When the user enters a news article and clicks **Check News**, the application:

```text
News Article
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Prediction
     ↓
Likely REAL / Likely FAKE
```

## 🌐 Deployment

This application can be deployed using **Streamlit Community Cloud**.

Basic deployment process:

```text
Create Streamlit App
        ↓
Create requirements.txt
        ↓
Upload files to GitHub
        ↓
Connect GitHub repository to Streamlit Community Cloud
        ↓
Deploy
        ↓
Public Web Application
```

## ⚠️ Important Limitation

This application is intended for **educational and demonstration purposes**.

The model is trained on a very small sample dataset and therefore **should not be used to determine whether real-world news is actually true or false**.

A reliable fake-news detection system would require:

* A large and representative dataset
* Fact-checked training labels
* More sophisticated NLP techniques
* Validation and test datasets
* Performance evaluation
* Regular updating of the training data

Therefore, the output **"Likely REAL" or "Likely FAKE" should not be interpreted as factual verification**.

## 🎓 Learning Objectives

This project demonstrates the basic workflow of a machine-learning application:

* Text preprocessing
* Feature extraction
* TF-IDF
* Supervised learning
* Logistic Regression
* Text classification
* Streamlit application development
* GitHub-based deployment

## 👨‍💻 Author

**Anil Verma**

This project was developed as an educational demonstration of **Natural Language Processing, Machine Learning, and Streamlit application development**.
