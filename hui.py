import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from URLs
quiz_endpoint_url = "https://jsonkeeper.com/b/LLQT"
quiz_submission_url = "https://api.jsonserve.com/rJvd7g"
api_endpoint_url = "https://api.jsonserve.com/XgAgFJ"

quiz_data = pd.read_json(quiz_endpoint_url)
quiz_submission_data = pd.read_json(quiz_submission_url)
historical_data = pd.read_json(api_endpoint_url)

# Merge data on user_id
merged_data = pd.merge(quiz_submission_data, historical_data, on='user_id')

# Analyze performance by topic and difficulty
topic_performance = merged_data.groupby('topic')['score'].mean()
difficulty_performance = merged_data.groupby('difficulty_level')['score'].mean()

# Visualize performance by topic
plt.figure(figsize=(10,6))
sns.barplot(x=topic_performance.index, y=topic_performance.values)
plt.title('Performance by Topic')
plt.xlabel('Topic')
plt.ylabel('Average Score')
plt.xticks(rotation=45)
plt.show()

# Generate recommendations based on weak areas
def generate_recommendations(user_id, merged_data):
    user_data = merged_data[merged_data['user_id'] == user_id]
    weak_topics = user_data[user_data['score'] < 50]['topic'].unique()
    recommended_topics = [topic for topic in weak_topics if topic not in ['Topic A', 'Topic B']]  # exclude topics already mastered
    
    return f"Focus on these topics for improvement: {', '.join(recommended_topics)}"

# Example usage
user_id = 123  # Replace with actual user ID
recommendations = generate_recommendations(user_id, merged_data)
print(recommendations)

# Additional insights: Track improvement trends
def track_improvement(user_id, merged_data):
    user_data = merged_data[merged_data['user_id'] == user_id]
    user_data = user_data.sort_values(by='quiz_date')
    improvement_trends = user_data[['quiz_date', 'score']]
    
    plt.figure(figsize=(10,6))
    plt.plot(improvement_trends['quiz_date'], improvement_trends['score'], marker='o')
    plt.title(f'Improvement Trends for User {user_id}')
    plt.xlabel('Quiz Date')
    plt.ylabel('Score')
    plt.xticks(rotation=45)
    plt.show()

# Track improvement trends for a user
track_improvement(user_id, merged_data)
