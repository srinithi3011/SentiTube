import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv("comments.csv")

positive = 0
negative = 0
neutral = 0

for comment in df["Comment"]:
    score = TextBlob(str(comment)).sentiment.polarity

    if score > 0:
        positive += 1
    elif score < 0:
        negative += 1
    else:
        neutral += 1

labels = ["Positive", "Negative", "Neutral"]
sizes = [positive, negative, neutral]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("SentiTube Comment:Sentiment Analysis")
plt.show()