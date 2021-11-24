import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
model_training = st.container()

with header:
     st.title('welcome to my page')
     st.text('in this project i analyse youtube video')
     
with dataset:
     st.header('youtube dataset')
     st.text('i created this dataset')
     
     youtube_data = pd.read_csv('https://raw.githubusercontent.com/milletan/what-the-popular-youtube-video-category/main/data%20-%20Sheet1.csv')
     st.write(youtube_data.head())
     
     st.subheader('Youtube video category with most viewed times')
     View_times_dist = pd.DataFrame(youtube_data['View_times'].value_counts()).head(50)
     st.bar_chart(View_times_dist)
     
with model_training:
    st.header('most popular')
    st.text('music')
