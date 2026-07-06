from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer=SentimentIntensityAnalyzer()

def analyze(comments):

    positive=[]
    neutral=[]
    negative=[]

    for comment in comments:

        score=analyzer.polarity_scores(comment)

        compound=score["compound"]

        if compound>=0.05:

            positive.append(comment)

        elif compound<=-0.05:

            negative.append(comment)

        else:

            neutral.append(comment)

    total=len(comments)

    if total==0:

        creator_score=0

    else:

        creator_score=round((len(positive)/total)*100,2)

    return positive,negative,neutral,creator_score