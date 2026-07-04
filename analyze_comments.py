import pandas as pd
from textblob import TextBlob

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

total = positive + negative + neutral
health_score = ((positive - negative) / total) * 100
health_score = max(0, min(100, health_score + 50))

print("\n===== SentiTube Report =====")
print("Total Comments:", total)
print("Positive:", positive)
print("Negative:", negative)
print("Neutral :", neutral)

print("\nCreator Health Score:", round(health_score, 2), "/100")

print("\n===== SentiTube Report =====")
print("Total Comments:", total)
print("Positive:", positive)
print("Negative:", negative)
print("Neutral :", neutral)

print("\nPercentages")
print("Positive:", round((positive/total)*100, 2), "%")
print("Negative:", round((negative/total)*100, 2), "%")
print("Neutral :", round((neutral/total)*100, 2), "%")
if health_score >= 80:
    print("Audience Reaction: Excellent 🔥")
elif health_score >= 60:
    print("Audience Reaction: Good 👍")
elif health_score >= 40:
    print("Audience Reaction: Average 🙂")
else:
    print("Audience Reaction: Needs Improvement ⚠️")