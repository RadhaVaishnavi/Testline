
# Personalized Quiz Performance Analysis and Recommendations

# Project Overview
This project analyzes quiz performance data to identify patterns, weaknesses, and improvement areas for students. It generates actionable recommendations based on historical quiz data, submission accuracy, and response patterns. Key functionalities include:
Schema exploration and performance trend analysis.
Insights into weak topics and difficulty levels.
Personalized recommendations for improvement.
Setup Instructions
# step 1: Clone the Repository:
git clone repository_url
cd repository_directory  
# step 2 : Install Dependencies:
# step 3: Ensure you have Python 3.x installed. Install the required libraries using:
pip install -r requirements.txt  
# step 4: Run the Script:

# step 5: Execute the main script in your preferred IDE or terminal:
python main.py  

Data Sources:
The project fetches data from the following endpoints:
Quiz Data: https://www.jsonkeeper.com/b/LLQT
Quiz Submissions: https://api.jsonserve.com/rJvd7g
Historical Data: https://api.jsonserve.com/XgAgFJ

# Approach Description

# Data Retrieval and Preprocessing:

Fetch JSON data from API endpoints.
Convert nested JSON structures into DataFrames for analysis.

# Analysis:

Explore patterns in performance by topics, difficulty levels, and accuracy.
Group historical data to calculate metrics like average score and mistake count.

# Insights Generation:

Identify weak areas (low accuracy or high mistakes).
Highlight improvement trends by comparing past and current performance.

# Recommendations:

Suggest focus topics, question types, or difficulty levels.
Key Visualizations
Includes visualizations such as:
Accuracy trends by topic.
Mistake distribution across quizzes.
Recommendations summary.

# Insights Summary
Weak areas identified include quizzes with average accuracy below 70%.
Significant improvement trends were observed in quizzes where students repeatedly practiced.
Personalized recommendations include focusing on specific topics and attempting quizzes of moderate difficulty to build confidence.
