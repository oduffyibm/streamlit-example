import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("This app is awesome")
st.subheader("And this is the subheader")

st.write("Hello **world**")

st.divider()

st.markdown("Hello **World** in markdown")


st.write("The code for this app is")
st.code("""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

st.title("This app is awesome")
st.subheader("And this is the subheader")

st.write("Hello **world**")
st.write_stream("The quick brown fox jumps over the lazy dog")

Hello again
""")








