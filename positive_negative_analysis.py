import pandas as pd
from textblob import TextBlob
import os
from collections import Counter

# Check the path of the desktop
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Load the Excel file
df = pd.read_excel(f'{desktop_path}/Friction Points by Category - Clean.xlsx')

# Assuming that 'feedback' is the column with the text you want to analyze
feedbacks = df['feedback']

# Analyze sentiments in the feedbacks and categorize them
sentiment_categories = ['Strong Negative', 'Negative', 'Neutral', 'Positive', 'Strong Positive']
sentiment_counts = Counter()

for feedback in feedbacks:
    blob = TextBlob(feedback)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score <= -0.6:
        sentiment_counts['Strong Negative'] += 1
    elif sentiment_score <= -0.2:
        sentiment_counts['Negative'] += 1
    elif sentiment_score <= 0.2:
        sentiment_counts['Neutral'] += 1
    elif sentiment_score <= 0.6:
        sentiment_counts['Positive'] += 1
    else:
        sentiment_counts['Strong Positive'] += 1

# Print the major trends
print("Major trends in the feedback:")
for category in sentiment_categories:
    print(f"{category}: {sentiment_counts[category]} feedbacks")