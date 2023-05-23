import streamlit as st

st.write("TEST")
video_file = open("https://github.com/JVJayarah3/about_me/blob/main/video/Blue%20Grey%20Modern%20User%20Persona%20Graph%20(1).mp4")
video_bytes = video_file.read()
st.video(video_bytes)
