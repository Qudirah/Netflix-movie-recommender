# 🎬 Netflix Movie Recommender

Welcome to the **Netflix Movie Recommender** — a lightweight app that helps you find similar movies based on your favorite pick! Whether you're into thrillers, rom-coms, or mind-bending sci-fi, this app aims to make your next Netflix binge just a click away.

> _"Built in just 30 minutes during a live demo, but ready to help you all night long."_

---

## 💡 About This Project

This project was created during the **Google Developer Student Clubs (GDSC)** **Build with AI** event — a dynamic, hands-on session where participants explored the exciting intersection of artificial intelligence and real-world use cases.

I was invited to speak and build a mini AI-powered solution, and in under 30 minutes, we developed a working **movie recommendation system** using:

- **Pandas** and **scikit-learn** for data handling and similarity computation
- **Pickle** for saving precomputed similarity matrices
- **Streamlit** for the web interface
- A splash of ✨ enthusiasm + caffeine

---

## 🚀 Try It Live

Click here to test the app:  
👉 [Netflix Movie Recommender on Streamlit](https://recommendmovi.streamlit.app/)

---

## 🧠 How It Works

1. The app uses a dataset of movies and extracts relevant features like genres, keywords, cast, and crew.
2. It vectorizes this information using **TF-IDF** and calculates **cosine similarity** between movies.
3. When a user selects a movie, the app recommends the top 5 most similar titles.

---

## 📦 Tech Stack

- `Python`
- `Pandas`, `Scikit-learn`, `Pickle`
- `Streamlit` (for UI)

---

## 🧰 Setup Locally

```bash
# Clone the repo
git clone https://github.com/Qudirah/Netflix-movie-recommender.git
cd Netflix-movie-recommender

# Set up virtual env (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run deploy.py
