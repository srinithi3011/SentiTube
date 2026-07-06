from googleapiclient.discovery import build

API_KEY = "AIzaSyCpOtP04dubgsECqScijTIaxor76xO1ZY8"

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