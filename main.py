import streamlit as st
import pandas as pd
import numpy as np

st.title("Je t'aime")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text('chargement...')
data = load_data(1000)
data_load_state.text("donnée mise en cache")
with st.sidebar :
    if st.checkbox ("Donnée brute") :
        st.subheader('donnée')
        st.write(data)

st.subheader('un histogramme')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

hour_to_filter = st.slider("Heure",0,23,17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader('une carte')
st.map(filtered_data)