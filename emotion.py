from textblob import TextBlob


def detect_emotion(comments):

    emotions = {
        "Happy": 0,
        "Neutral": 0,
        "Sad": 0
    }

    for comment in comments:

        polarity = TextBlob(comment).sentiment.polarity

        if polarity > 0.2:
            emotions["Happy"] += 1

        elif polarity < -0.2:
            emotions["Sad"] += 1

        else:
            emotions["Neutral"] += 1

    return emotions