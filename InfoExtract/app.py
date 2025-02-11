from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your DataFrame here, or replace this with your data loading logic.
df = pd.read_csv('50word_with_topic_llama2Model_finale.csv')

@app.route('/')
def index():
    # Get the unique topics from your DataFrame
    topics = df['topic'].unique()
    return render_template('index.html', topics=topics)

@app.route('/filter', methods=['POST'])
def filter_data():
    selected_topic = request.form.get('selected_topic')
    filtered_df = df[df['topic'] == selected_topic]
    
    # Render only the filtered data HTML
    return render_template('filtered_data.html', filtered_df=filtered_df)

if __name__ == '__main__':
    app.run(debug=True)
