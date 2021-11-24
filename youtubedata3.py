import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
     fig = plt.figure(figsize=(7,5))
     
     names = ["how-to-do","vlog","fitness","cooking","music"]
     Viewtimes = [1000000, 3000000, 4000000, 200000000, 100000000]
     positions = [0, 1, 2, 3, 4]
     
     plt.bar(positions, Viewtimes, witdh=0.5, color=g)
     
     plt.xticks(positions, Viewtimes)
     
     plt.show()
     
with model_training:
    st.header('most popular')
    st.text('music')
