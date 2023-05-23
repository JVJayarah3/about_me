import streamlit as st
import pyttsx3
st.set_page_config(layout='wide')
st.write("TEST")
#video_file = open("/main/video/test.mp4")
#https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4
#video_bytes = video_file.read()

about_me ="I am Jayaraj J V higly skilled petroleum engineer, have good command in Drilling, reservoir, completion and drilling software development. In programming point of view i have beginner to intermediate level of knowledge in python, data science, dashboard making, web application. I posses execellant problem solving capacity with quick desicion making skiill. i have a fond of providing roboust solution to the problem with project management. Next i would say, my biggest strength is active listening and fast learner means you dont have to spend much of your valuable time in training and supervising me. Finally the type of person i am means you will be getting someone in your team who is really hungry to learn, enthusiastic, self motivated and highly trustworthy. i am ready to start my work and i will never let you down. Thanks"
strength = "my 5 biggest strengths are number one disciplined and focussed, number 2 flexible and verstile, number3 resourceful, number4, loyal and trustworthy and finally a collabrative worker"
weakness = "one of my biggest weakness is i am very bad at giving people feedback, if someone ask me for feedback i would rather avoid it as i don't want to hurt their feeling. however i do appreciate that feedback is an essential part of self development. i have been trying improve in this area by forcing myself to give people feedback"
projection = "i have two project to do "

engine = pyttsx3.init()
with st.container():
    col1,col2,col3,col4= st.columns([3.5,1,1,1])
    with col1:
      st.video("https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4?raw=true")
    with col3:
      st.image("https://github.com/JVJayarah3/about_me/blob/main/video/drillstring.JPG?raw=true")
    with col4:
      b1 = st.button("ABOUT ME")
      if b1 :
            engine.say(about_me)
            engine.runAndWait()
      st.empty()
      b2 = st.button("STRENGTH")
      if b2 :
            engine.say(strength)
            engine.runAndWait()
        st.empty()
      b3 = st.button("WEAKNESS")
      if b3 :
            engine.say(weakness)
            engine.runAndWait()
      st.empty()
      b4 = st.button("PROJECTION
      if b4 :
            engine.say(projection)
            engine.runAndWait()         
      st.empty()
      b5 = st.button("REASONS")
      if b5 :
            engine.say(reasons)
            engine.runAndWait()       
