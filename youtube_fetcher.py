import os


from googleapiclient.discovery import build
from dotenv import load_dotenv


class YouTubeFetcher:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('YT_API_KEY')
        self.service_youtube = build("youtube", "v3", developerKey=self.api_key)


    def fetch_comments(self, video_id: str, max_results: int = 100) -> list:
        request = self.service_youtube.commentThreads().list(
            part = "snippet",
            videoId = video_id,
            maxResults = max_results
        )
        response = request.execute()
        return self._parse_comments(response)


    def _parse_comments(self, response: dict) -> list:
        comments_list = []
        for item in response.get("items", []):
            comments_list.append(item['snippet']['topLevelComment']['snippet']['textOriginal'])

        return comments_list
    
