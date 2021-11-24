import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
     st.title('welcome to my page')
     st.text('in this project i analyse youtube video')
     
with dataset:
     st.header('youtube dataset')
     st.text('i created this dataset')
     
     youtube_data = pd.read_csv("data - Sheet1.csv")
     st.write(data - Sheet1.head())
     
with features:
     st.header('the features i created')
     
     
     
with model_training:
    st.header('most popular')
    st.text('music')
