import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

header = st.container()
dataset = st.container()
model_training = st.container()

with header:
     st.title('welcome to my page')
     
with dataset:
     st.header('youtube dataset')
     
     youtube_data = pd.read_csv('https://raw.githubusercontent.com/milletan/what-the-popular-youtube-video-category/main/data%20-%20Sheet1.csv')
     st.write(youtube_data.head())
     
     st.subheader('Youtube video Category with most viewed times')
     data = pd.DataFrame({'Category': ['how-to-do','cooking','music','fitness','vlog'],'Viewtimes': ['1000','2000','15000','4000','3000']})
                   
     st.write(data)
     
     fig, ax = plt.subplots()
     ax.bar(data.Category,data.Viewtimes)
     st.pyplot(fig)
                                  
with model_training:
    st.header('most popular')
    st.text('music')
