import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Dataset", page_icon="🔌",layout="wide")
st.title(':black[Electric Vehicle Price Prediction]')
st.header(':red[Innomatics Research Labs]')
st.caption('Project By Shreyash Tare')


FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

DATA_PATH = os.path.join(dir_of_interest, "data", "electric_vehicle_clean.csv")

dt = st.radio('Show in Dataset (Head/Tail)',('Head','Tail'))

if dt == 'Head':
    st.dataframe(DATA_PATH.head(10))
else:
    st.dataframe(DATA_PATH.tail(10))

ds = st.checkbox('Show the whole Dataset')
if ds:
    st.dataframe(DATA_PATH)

sh = st.selectbox('Check',('Select','Shape','Columns','Statistical Description'))
if sh == 'Shape':
    st.write(DATA_PATH.shape)
elif sh == 'Columns':
    st.write(DATA_PATH.columns)
elif sh == 'Select':
    " "
elif sh == 'Statistical Description':
    st.write(DATA_PATH.describe())