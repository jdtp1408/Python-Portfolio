import spacy
import pandas as pd
from textblob import TextBlob

# Loading the medium size language model
nlp = spacy.load('en_core_web_md')

# Loading the reviews data into the program
df = pd.read_csv('amazon_product_reviews.csv')

# Ensure 'reviews.text' column is treated as strings and strip leading/trailing whitespaces
df['reviews.text'] = df['reviews.text'].astype(str).apply(lambda x: x.strip())

# Remove any n/a values to clean data
clean_reviews = df['reviews.text'].dropna()

# Creates function that processes reviews for nlp and removes stop words
def process_review(review):
  doc = nlp(review)
# Filter tokens
  filtered_tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]

  return filtered_tokens

# Apply the process_review function to each review
df['filtered_tokens'] = clean_reviews.apply(process_review)

# Creates function that calculates polarity and subjectivity figures
def sentiment_analysis(text):
  blob = TextBlob(str(text))
  return blob.sentiment

# Applies the sentiment_analysis function to each review
df['sentiment'] = df['filtered_tokens'].apply(sentiment_analysis)

# Displays sample observations for analysis
print("Here are 7 sample observations from the data, including the review, the filtered/cleaned reviews, and their polarity and subjectivity scores")
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[0])
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[20])
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[472])
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[1362])
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[2529])
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[4730])
print(df[['reviews.text', 'filtered_tokens', 'sentiment']].iloc[4996])

# Similarity of two reviews with low or negative polarity
negative_review = nlp(df['reviews.text'][0])
low_review = nlp(df['reviews.text'][2529])

print("The similarity between a review with low positive polarity and one with low negative polarity: " + str(negative_review.similarity(low_review)))

# Similarity of two reviews with higher positive polarity
positive_review = nlp(df['reviews.text'][472])
larger_positive_review = nlp(df['reviews.text'][4996])

print("The similarity between a positive polarity review and a review with larger positive polarity: " + str(positive_review.similarity(larger_positive_review)))

# Similarity calculation for the large positive polarity and negative polarity reviews
print("The similarity between the review with a larger positive polarity and the negative polarity review: " + str(larger_positive_review.similarity(negative_review)))