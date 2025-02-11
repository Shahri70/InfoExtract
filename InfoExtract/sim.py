import pandas as pd
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Load the CSV file
csv_file_path = '50word_with_topic_llama2Model_finale.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Preprocess the topics and convert them into embeddings
# You should adjust the preprocessing steps based on your dataset and requirements
sentences = [str(topic).split() for topic in df['topic']]
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, sg=0)
while True:
    # Step 3: Accept user input and convert it into an embedding
    user_input = input("Enter your keyword: ")
    user_input = user_input.split()  # You can adjust this based on your input processing needs
    user_embedding = np.mean([model.wv[word] for word in user_input if word in model.wv], axis=0)

    # Step 4: Calculate similarity between user input and topics
    similarities = []
    for topic in df['topic']:
        topic_embedding = np.mean([model.wv[word] for word in str(topic).split() if word in model.wv], axis=0)
        if np.any(topic_embedding):
            similarity = cosine_similarity([user_embedding], [topic_embedding])
            similarities.append(similarity[0][0])
        else:
            similarities.append(0)  # Handle cases where the topic has no valid words

    # Step 5: Return the most similar topic
    max_similarity_index = np.argmax(similarities)
    most_similar_topic = df.loc[max_similarity_index, 'topic']
    print("Most similar topic:", most_similar_topic)
    data=df[df["topic"] == most_similar_topic]
    print(data.head())
