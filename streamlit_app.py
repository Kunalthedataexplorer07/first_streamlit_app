import streamlit as st

st.title('My Parents New Healthy Dinner')
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry OatMeal')
st.text('Kate, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')
st.text('Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.dataframe(my_fruit_list)
