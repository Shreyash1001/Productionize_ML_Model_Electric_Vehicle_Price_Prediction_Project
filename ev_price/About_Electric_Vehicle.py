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

# Load the CSV file into a pandas DataFrame object
df = pd.read_csv(DATA_PATH)

dt = st.radio('Show in Dataset (Head/Tail)',('Head','Tail'))

if dt == 'Head':
    st.dataframe(df.head(10))
else:
    st.dataframe(df.tail(10))

ds = st.checkbox('Show the whole Dataset')
if ds:
    st.dataframe(df)

sh = st.selectbox('Check',('Select','Shape','Columns','Statistical Description'))
if sh == 'Shape':
    st.write(df.shape)
elif sh == 'Columns':
    st.write(df.columns)
elif sh == 'Select':
    pass # Do nothing
elif sh == 'Statistical Description':
    st.write(df.describe())
