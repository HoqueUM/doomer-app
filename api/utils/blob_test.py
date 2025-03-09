from textblob import TextBlob

headline = "First national analysis finds America's butterflies are disappearing at 'catastrophic' rate"

blob = TextBlob(headline)

polarity = blob.sentiment.polarity

print(blob.sentiment)

if polarity > 0:
    print("Positive")
elif polarity < 0:
    print("Negative")
else:
    print("Neutral")