import streamlit as st
import pyttsx3
st.set_page_config(layout='wide')

#video_file = open("/main/video/test.mp4")
#https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4
#video_bytes = video_file.read()

about_me ="I am Jayaraj J V higly skilled petroleum engineer, have good command in Drilling, reservoir, completion and drilling software development. In programming point of view i have beginner to intermediate level of knowledge in python, data science, dashboard making, web application. I posses execellant problem solving capacity with quick desicion making skiill. i have a fond of providing roboust solution to the problem with project management. Next i would say, my biggest strength is active listening and fast learner means you dont have to spend much of your valuable time in training and supervising me. Finally the type of person i am means you will be getting someone in your team who is really hungry to learn, enthusiastic, self motivated and highly trustworthy. i am ready to start my work and i will never let you down. Thanks"
strength = "my 5 biggest strengths are number one disciplined and focussed, number 2 flexible and verstile, number3 resourceful, number4, loyal and trustworthy and finally a collabrative worker"
weakness = "one of my biggest weakness is i am very bad at giving people feedback, if someone ask me for feedback i would rather avoid it as i don't want to hurt their feeling. however i do appreciate that feedback is an essential part of self development. i have been trying improve in this area by forcing myself to give people feedback"
projection = "Presently i have three different project, on which i am working on number 1 well life which deals with the entire lifecycle of well from planning to abandonment. The main aim of this project is to showcase dashbord kind of out to the client from report throughout the entire life of well. number 2 is presenter this one is apart from the energy industry, the main aim of this is to make a short presentation from a large report and lastly matmate this is amied to give a real time support to client on finding the best solution to the equipment's problem by sorting the nearest available vendors and optimising solution"
with st.container():
    col1,col2,col3,col4= st.columns([1,3,1,1])
    with col2:
        st.title("ABOUT ME")
#engine = pyttsx3.init()
with st.container():
    col1,col2,col3,col4= st.columns([3.5,1,1,1])
    with col1:
      st.video("https://github.com/JVJayarah3/about_me/blob/main/video/test.mp4?raw=true")
    with col3:
      st.image("https://github.com/JVJayarah3/about_me/blob/main/video/drillstring.JPG?raw=true")
    with col4:
      b1 = st.button("ABOUT ME")
      if b1 :
            #audio_about = open("https://github.com/JVJayarah3/about_me/blob/main/video/about.mp3?raw=true",'rb')
            #audio_about_1 = audio_about.read()
            st.audio("https://github.com/JVJayarah3/about_me/blob/main/video/about.mp3?raw=true",format='audio/ogg')

      st.empty()
      """
      
      """
      b2 = st.button("STRENGTH")
      if b2 :
            st.audio("https://github.com/JVJayarah3/about_me/blob/main/video/strength.mp3?raw=true",format='audio/ogg')

      st.empty()
      """
      
      """
      b3 = st.button("WEAKNESS")
      if b3:
        st.audio("https://github.com/JVJayarah3/about_me/blob/main/video/weakness.mp3?raw=true",format='audio/ogg')

      st.empty()
      """
      
      """   
      b4 = st.button("PROJECTION")
      if b4:
        st.audio("https://github.com/JVJayarah3/about_me/blob/main/video/projection.mp3?raw=true",format='audio/ogg')

     
