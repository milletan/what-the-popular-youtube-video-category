import streamlit as st
import pandas as pd
import altair as alt

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
     
     st.subheader('Youtube video Category with most viewed times')
     data = pd.DataFrame(youtube_data)
     'Category': ['how-to-do','cooking','music','fitness','vlog']
     'Viewtimes': ['1000000','20000000','100000000','4000000',3000000'],
     })
     st.write(data)
     st.write(alt.Chart(data).mark_bar().encode(
     x=alt.X('Category', sort=None),
     y='Viewtimes',
     ))
    
                                           
with model_training:
    st.header('most popular')
    st.text('music')
