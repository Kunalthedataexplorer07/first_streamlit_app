import streamlit as st
import pandas as pd
import requests as req
import snowflake.connector
from urllib.error import URLError

st.title('My Parents New Healthy Dinner')
st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry OatMeal')
st.text('Kate, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')
st.text('Avacado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include and some fruits pre-selected
# st.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruit_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.

st.dataframe(fruits_to_show)

# create a repeatable code (function)
def get_fruityvice_data (this_fruit_choice):
    fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')

try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information. ")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)

except URLError as e:
  st.error()
    

  # fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
  
# st.write('The user entered ', fruit_choice)
#import requests as req
# fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# st.text(fruityvice_response.json()) # just writes the data to the screen

# take the json version of the response and normalize it 

# fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

#output it to the screen as a table

# st.dataframe(fruityvice_normalized)

# Added snowflake connector lib

# import snowflake.connector
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_row = my_cur.fetchall()
st.header("Fruit Load list contains:")

# Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")
        return my_cur.fetchall()
# Add button to load the fruit list
if st.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    st.dataframe(my_data_row)

#Dont run anything past here while we are troubleshooting

st.stop()
    
# Allow user to add fruits to the list

add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thank you for adding ',add_my_fruit)

#This will not work correctly, but just go with it for now 
my_cur.execute("INSERT INTO fruit_load_list values ('from streamlit')")
