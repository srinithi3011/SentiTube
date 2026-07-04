from googleapiclient.discovery import build

API_KEY = "AIzaSyCpOtP04dubgsECqScijTIaxor76xO1ZY8"

youtube = build("youtube", "v3", developerKey=API_KEY)

video_id = "dQw4w9WgXcQ"  # Example video

request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    maxResults=10,
    textFormat="plainText"
)

response = request.execute()

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    print(comment)