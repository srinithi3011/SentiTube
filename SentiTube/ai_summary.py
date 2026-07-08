from collections import Counter
import re


def generate_summary(positive, neutral, negative, score):

    comments = positive + neutral + negative

    text = " ".join(comments).lower()

    words = re.findall(r"\b[a-zA-Z]{4,}\b", text)

    stop_words = {
        "this","that","with","have","your","from",
        "they","were","been","there","would",
        "could","should","video","videos","really",
        "very","just","what","when","where",
        "which","will","good","great","nice",
        "awesome","love"
    }

    words = [w for w in words if w not in stop_words]

    common = Counter(words).most_common(5)

    topics = ", ".join([w.title() for w, _ in common])

    if score >= 80:

        mood = "highly positive"

        suggestion = (
            "Continue producing similar content because viewers are highly satisfied."
        )

    elif score >= 60:

        mood = "mostly positive"

        suggestion = (
            "Minor improvements could further increase audience engagement."
        )

    elif score >= 40:

        mood = "mixed"

        suggestion = (
            "Review negative feedback to improve future videos."
        )

    else:

        mood = "mostly negative"

        suggestion = (
            "Consider improving content quality based on audience feedback."
        )

    summary = f"""
The audience response is {mood}.

Most discussions revolve around:
{topics}.

Out of {len(comments)} analyzed comments,
the overall Creator Health Score is {score}%.

Recommendation:
{suggestion}
"""

    return summary