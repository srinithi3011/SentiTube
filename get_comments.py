from googleapiclient.discovery import build
import pandas as pd

API_KEY = "AIzaSyCpOtP04dubgsECqScijTIaxor76xO1ZY8"

youtube = build("youtube", "v3", developerKey=API_KEY)

from urllib.parse import urlparse, parse_qs

url = input("Paste YouTube URL: ")

parsed_url = urlparse(url)
video_id = parse_qs(parsed_url.query).get("v")[0]

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=50,
    textFormat="plainText"
)

response = request.execute()

comments = []

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    comments.append(comment)

df = pd.DataFrame(comments, columns=["Comment"])
df.to_csv("comments.csv", index=False)

print("Comments saved to comments.csv")
try:
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query).get("v")[0]
except:
    print("Invalid YouTube URL")
    exit()