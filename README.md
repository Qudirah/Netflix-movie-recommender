<h1> Netflix Movie Recommender </h1>


The system recommends 10 movies when you input a movie you once enjoyed on Netflix. The dataset is a public dataset that can be found on kaggle. I used python libraries such as pandas, sklearn and nltk. Pandas is used for the preprocessing while nltk is used for the text preprocessing. The words were lemmatized(considering the part of speech) and then vectorized (using tfidf vectorizer). Cosine similarity is used to measure the distance between the vector arrays and as such it arranges them in descending order and recommends the first 10.

<h3> How to run locally on your system </h3>


1. Copy the python code and make sure it runs in your jupyter notebook
2. Copy the deploy code in your vscode
3. In your terminal, type streamlit run deploy.py and then enter
4. Click on the link provided to make it run
5. Make sure to have all file saved. Including the pickle files

