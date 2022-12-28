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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include and some fruits pre-selected
# st.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruit_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.

st.dataframe(fruits_to_show)

#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')

fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

import requests as req

fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response.json()) # just writes the data to the screen

# take the json version of the response and normalize it 

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

#output it to the screen as a table

st.dataframe(fruityvice_normalized)
