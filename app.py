import streamlit as st
st.set_page_config(layout='wide')
st.write("TEST")
#video_file = open("/main/video/test.mp4")
#https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4
#video_bytes = video_file.read()

with st.container():
    col1,col2,col3,col4= st.columns([3.5,1,1,1])
    with col1:
      st.video("https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4?raw=true")
    with col3:
      st.image("https://github.com/JVJayarah3/about_me/blob/main/video/drillstring.JPG?raw=true")
    with col4:
      b1 = st.button("ABOUT ME")
      st.empty()
      b2 = st.button("STRENGTH & WEAKNESS")
      st.empty()
      b3 = st.button("---")
      st.empty()
      b4 = st.button("----")
