import requests
import streamlit
import snowflake.connector
from urllib.error import URLerror

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# create repeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return(fruityvice_normalized)

# New section to display fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
if not fruit_choice:
  streamlit.text_input("Please select a fruit to get information.")
else:
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
  back_from_function = get_fruityvicedata(fruit_choice)
  streamlit.dataframe(back_from_function)

except URLerror as e:

# Add end user to add a fruit in the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur("insert into fruit_load_list values ('" + ??? + "')")
         return "Thanks for adding" + new_fruit
      
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
     back_from_function = insert_row_snowflake(fruit_choice)
     streamlit.dataframe(back_from_function)

# Don't run anything past while we're troubleshoot
streamlit.stop()

# Snowflake-Python Connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchone()
streamlit.header("The fruit load contains:")
# Snowflake related functions
def get_fruit_load_list():
    with cnx.cursor as my_cur():
  my_cur.execute("select * from fruit_load_list")
  return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get fruit load list')
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list
    streamlit.datafame(my_data_rows)
