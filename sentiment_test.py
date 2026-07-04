from textblob import TextBlob

comment = input("Enter a comment: ")

analysis = TextBlob(comment)

score = analysis.sentiment.polarity

if score > 0:
    print("Positive 😊")
elif score < 0:
    print("Negative 😞")
else:
    print("Neutral 😐")

print("Polarity Score:", score)