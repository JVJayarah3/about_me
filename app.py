import streamlit as st

st.write("TEST")
video_file = open("https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4")
video_bytes = video_file.read()
st.video(video_bytes)
