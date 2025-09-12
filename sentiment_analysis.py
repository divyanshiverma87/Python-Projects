from textblob import TextBlob

text = input("Enter your message: ")
blob = TextBlob(text)
polarity = blob.sentiment.polarity

if polarity > 0:
    print("🙂 Positive Sentiment")
elif polarity < 0:
    print("☹️ Negative Sentiment")
else:
    print("😐 Neutral Sentiment")

print(f"Polarity Score: {polarity}")
