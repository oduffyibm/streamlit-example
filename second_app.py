import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("This app is awesome")
st.subheader("And this is the subheader")

st.write("Hello **world**")

st.divider()

data = {'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'Activity': ['run', 'scream', 'laugh', 'jump', 'talk']}

df = pd.DataFrame(data)

st.dataframe(df)




