import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import seaborn as sns

   # Download required NLTK data
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

   # Load data from CSV
df = pd.read_csv('reviews.csv', encoding='utf-8')

   # Preprocess text
def preprocess_text(text):
       # Convert to lowercase
       text = text.lower()
       # Remove punctuation
       text = text.translate(str.maketrans('', '', string.punctuation))
       # Tokenize
       tokens = word_tokenize(text)
       # Remove stopwords
       stop_words = set(stopwords.words('english'))
       tokens = [word for word in tokens if word not in stop_words]
       return ' '.join(tokens)

   # Apply preprocessing
df['cleaned_text'] = df['text'].apply(preprocess_text)

   # Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

   # Function to get sentiment
def get_sentiment(text):
       scores = sid.polarity_scores(text)
       compound = scores['compound']
       if compound >= 0.05:
           return 'Positive'
       elif compound <= -0.05:
           return 'Negative'
       else:
           return 'Neutral'

   # Apply sentiment analysis
df['sentiment'] = df['cleaned_text'].apply(get_sentiment)
df['compound_score'] = df['cleaned_text'].apply(lambda x: sid.polarity_scores(x)['compound'])

   # Display results
print("\nSentiment Analysis Results:")
print(df[['text', 'sentiment', 'compound_score']])

   # Visualize sentiment distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='sentiment', data=df, order=['Positive', 'Neutral', 'Negative'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

   # Save results to CSV
df.to_csv('sentiment_results.csv', index=False)
print("\nResults saved to 'sentiment_results.csv'")