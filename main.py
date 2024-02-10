import streamlit as st
from dotenv import load_dotenv

load_dotenv() #load all env variable
import google.generativeai as genai
import os

# from youtube_transcript_api import YouTubeTranscriptApi
from helper import extract_transcript_details

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 


def generate_gemini_content(transcript_text,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("Youtube Video Summarizer")
youtube_link = st.text_input("Enter youtube link")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)
    
if st.button("Get detailed Notes"):
    transcript_text= extract_transcript_details(youtube_link)
    
    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("##Detailed notes")
        st.write(summary)
