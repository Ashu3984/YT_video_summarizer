import os
from youtube_transcript_api import YouTubeTranscriptApi

prompt = """You are youtube video summarizer. You will be taking the transcript text
and have to summarize the entire video and providing the important summary in points within 250 words"""

def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)
        transcript=""
        for i in transcript_text:
            transcript += " " + i["text"]
            
        return transcript
    except Exception as e:
        raise e
