import pandas as pd
from textblob import TextBlob

df = pd.read_csv("comments.csv")

positive = 0
negative = 0
neutral = 0

scores = []

for comment in df["Comment"]:
    score = TextBlob(str(comment)).sentiment.polarity
    scores.append(score)

    if score > 0:
        positive += 1
    elif score < 0:
        negative += 1
    else:
        neutral += 1

df["Score"] = scores

total = positive + negative + neutral

health_score = ((positive - negative) / total) * 100
health_score = max(0, min(100, health_score + 50))

print("\n========== SENTITUBE DASHBOARD ==========")

print(f"\nTotal Comments: {total}")
print(f"Positive Comments: {positive}")
print(f"Negative Comments: {negative}")
print(f"Neutral Comments : {neutral}")

print(f"\nCreator Health Score: {round(health_score,2)}/100")

if health_score >= 80:
    print("Audience Reaction: Excellent 🔥")
elif health_score >= 60:
    print("Audience Reaction: Good 👍")
elif health_score >= 40:
    print("Audience Reaction: Average 🙂")
else:
    print("Audience Reaction: Needs Improvement ⚠️")

print("\n----- Top Positive Comments -----")
print(df.sort_values("Score", ascending=False)[["Comment"]].head(5))

print("\n----- Top Negative Comments -----")
print(df.sort_values("Score")[["Comment"]].head(5))
print("\n==============================")
print("       SENTITUBE DASHBOARD")
print("==============================\n")

print(f"Total Comments : {total}")
print(f"Positive       : {positive}")
print(f"Negative       : {negative}")
print(f"Neutral        : {neutral}")
print("\n------------------------------")
print(f"Creator Score  : {round(health_score,2)}/100")
print("------------------------------\n")