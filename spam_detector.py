SPAM_KEYWORDS = [

    "subscribe",

    "my channel",

    "click here",

    "visit",

    "free",

    "giveaway",

    "telegram",

    "whatsapp",

    "follow me",

    "earn money",

    "http",

    "https",

    "www."

]


def is_spam(comment):

    text = comment.lower()

    for word in SPAM_KEYWORDS:

        if word in text:
            return True

    return False