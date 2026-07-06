import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("comments.csv")

text = " ".join(df["Comment"].astype(str))

words = text.lower().split()

# Remove common useless words
stop_words = {
    "the","is","a","an","and","to","of","in",
    "for","on","this","that","it","i","you",
    "my","was","are","be","have","has","had","got","get","do","go",
    "will","would","can","could","should","so","say","say","tell","up","from","as","but","just","been"
}
youtube_words = {
    "video","youtube","channel","subscribe",
    "watch","watching","view","views"
}
lyrics_words = {
    "gonna","never","make","give","let",
    "know","want","love","yeah","oh"
}
custom_stop_words = {
    "gonna","never","make","give","you","video",
    "youtube","channel","subscribe","watch",
    "watching","like","love","good","great"
}

filtered_words = [
    word for word in words
    if word not in stop_words and word not in youtube_words and word not in lyrics_words and word not in custom_stop_words
]
import re

text = " ".join(df["Comment"].astype(str)).lower()

words = re.findall(r'\b[a-z]{3,}\b', text)

counter = Counter(filtered_words)

top_words = counter.most_common(10)

words = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.figure(figsize=(8,5))
plt.bar(words, counts)
plt.title("Top Keywords in Comments")
plt.xlabel("Keywords")
plt.ylabel("Frequency")
plt.show()