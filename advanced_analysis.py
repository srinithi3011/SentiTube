import pandas as pd
from textblob import TextBlob

df = pd.read_csv("comments.csv")

sentiments = []
scores = []

for comment in df["Comment"]:
    score = TextBlob(str(comment)).sentiment.polarity
    scores.append(score)

    if score > 0:
        sentiments.append("Positive")
    elif score < 0:
        sentiments.append("Negative")
    else:
        sentiments.append("Neutral")

df["Score"] = scores
df["Sentiment"] = sentiments

df.to_csv("sentiment_report.csv", index=False)

print("Report generated successfully!")

print("\nTop Positive Comments")
print(df.sort_values("Score", ascending=False)[["Comment","Score"]].head(5))
print("\nTop Negative Comments")
print(df.sort_values("Score")[["Comment","Score"]].head(5))