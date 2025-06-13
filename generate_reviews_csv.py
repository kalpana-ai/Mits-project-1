import pandas as pd
import random

# Sample phrases for generating reviews
positive = [
    "Amazing product!", "Love this so much!", "Highly recommend!", "Fantastic quality!",
    "Best purchase ever!", "Exceeded expectations!", "Super happy!", "Worth every penny!"
]
negative = [
    "Terrible service!", "Waste of money!", "Broke after one use!", "Horrible quality!",
    "Very disappointing!", "Complete scam!", "Worst experience!", "Not worth it!"
]
neutral = [
    "It's okay.", "Does the job.", "Nothing special.", "Could be better.",
    "Decent for the price.", "Works fine.", "Not bad.", "Fairly good."
]
details = [
    "Fast delivery.", "Poor customer support.", "Tricky setup.", "Great design.",
    "Arrived damaged.", "Easy to use.", "Slow shipping.", "Good value."
]

# Generate 1200 reviews
reviews = []
for _ in range(1200):
    sentiment = random.choice(['positive', 'negative', 'neutral'])
    if sentiment == 'positive':
        review = random.choice(positive) + " " + random.choice(details)
    elif sentiment == 'negative':
        review = random.choice(negative) + " " + random.choice(details)
    else:
        review = random.choice(neutral) + " " + random.choice(details)
    reviews.append(review)

# Create DataFrame
df = pd.DataFrame({'text': reviews})

# Save to CSV
df.to_csv('reviews.csv', index=False, encoding='utf-8')
print("Created 'reviews.csv' with 1200 reviews.")