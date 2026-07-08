from urllib.parse import urlparse, parse_qs

url = input("Paste YouTube URL: ")

parsed_url = urlparse(url)

video_id = parse_qs(parsed_url.query).get("v")

if video_id:
    print("Video ID:", video_id[0])
else:
    print("Invalid YouTube URL")