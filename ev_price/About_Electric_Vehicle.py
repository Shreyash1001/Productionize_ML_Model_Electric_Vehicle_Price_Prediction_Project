import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", page_icon="🔌",layout="wide")
st.title(':black[Electric Vehicle Price Prediction]')
st.header(':red[Innomatics Research Labs]')
st.caption('Project By PRASAD JADHAV')

df = pd.read_csv('electric_vehicle_clean.csv')

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
    " "
elif sh == 'Statistical Description':
    st.write(df.describe())