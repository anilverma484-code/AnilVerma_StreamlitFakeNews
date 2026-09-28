import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# --------------------------------------------------
# 1. Training data
# --------------------------------------------------

news = [
    "Government announces new education policy",
    "Scientists discover a new species in the ocean",
    "Celebrity says drinking water cures all diseases",
    "Miracle medicine cures every disease instantly",
    "Central bank announces new interest rate",
    "Aliens have landed in New Delhi"
]

# 0 = Real, 1 = Fake
labels = [
    0,
    0,
    1,
    1,
    0,
    1
]

# --------------------------------------------------
# 2. Convert text into numbers
# --------------------------------------------------

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(news)

# --------------------------------------------------
# 3. Train the AI model
# --------------------------------------------------

model = LogisticRegression()
model.fit(X, labels)

# --------------------------------------------------
# 4. Streamlit interface
# --------------------------------------------------

st.title("📰 Fake News Classifier")

st.write("Enter a news article below to classify it.")

article = st.text_area(
    "Enter News Article:",
    placeholder="Type or paste a news article here..."
)

# --------------------------------------------------
# 5. Prediction
# --------------------------------------------------

if st.button("Check News"):

    if article.strip() == "":
        st.warning("Please enter a news article.")

    else:
        # Convert article into numbers
        article_vector = vectorizer.transform([article])

        # Predict
        prediction = model.predict(article_vector)

        # Display result
        if prediction[0] == 1:
            st.error("⚠️ Likely FAKE")
        else:
            st.success("✅ Likely REAL")

