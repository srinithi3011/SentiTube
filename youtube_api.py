from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

API_KEY = "AIzaSyCpOtP04dubgsECqScijTIaxor76xO1ZY8"   # <-- Replace with your API key


# ----------------------------
# Extract Video ID from URL
# ----------------------------
def get_video_id(url):
    parsed = urlparse(url)

    if parsed.hostname == "youtu.be":
        return parsed.path[1:]

    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed.query).get("v", [""])[0]

    return ""


# ----------------------------
# Fetch Comments
# ----------------------------
def get_comments(video_id, max_comments=3000):

    youtube = build("youtube", "v3", developerKey=API_KEY)

    comments = []
    next_page_token = None

    while len(comments) < max_comments:

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )
        response = request.execute()
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

            if len(comments) >= max_comments:
                break

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return comments

def get_video_details(video_id):

    youtube = build("youtube", "v3", developerKey=API_KEY)

    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    )

    response = request.execute()

    if not response["items"]:
        return None

    video = response["items"][0]

    snippet = video["snippet"]
    stats = video["statistics"]

    return {
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "thumbnail": snippet["thumbnails"]["high"]["url"],
        "published": snippet["publishedAt"][:10],
        "views": stats.get("viewCount", "0"),
        "likes": stats.get("likeCount", "0"),
        "comments": stats.get("commentCount", "0")
    }