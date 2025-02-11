import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 1: Load the CSV file
csv_file_path = '50word_with_topic_llama2Model_finale.csv'
df = pd.read_csv(csv_file_path)

# Step 2: Load a pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"  # You can choose a different model depending on your requirements
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
while True:
    # Step 3: Accept user input and convert it into an embedding
    user_input = input("Enter your search query: ")
    user_input = tokenizer(user_input, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        user_embedding = model(**user_input).last_hidden_state.mean(dim=1).squeeze().numpy()

    # Step 4: Calculate similarity between user input and topics
    similarities = []
    for topic in df['topic']:
        topic_input = tokenizer(str(topic), return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            topic_embedding = model(**topic_input).last_hidden_state.mean(dim=1).squeeze().numpy()
        similarity = cosine_similarity([user_embedding], [topic_embedding])
        similarities.append(similarity[0][0])

    # Step 5: Return the most similar topic
    max_similarity_index = np.argmax(similarities)
    most_similar_topic = df.loc[max_similarity_index, 'topic']
    print("Most similar topic:", most_similar_topic)
    data=df[df["topic"] == most_similar_topic]
    print(data.head())
