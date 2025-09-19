# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smootie:cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!
  """
)


# Add a Name Box for Smoothie Orders

name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be:", name_on_order)


# option = st.selectbox(
#     "What is your favorite fruit?",
#     ('Banana','Strawberries', "Peaches")
#)

# st.write("You favorite fruit is:", option)


# # To use a Snowpark COLUMN function named "col" we need to import it into our app
# from snowflake.snowpark.functions import col
# #Display the Fruit Options List in Your Streamlit in Snowflake (SiS) App
# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))
# st.dataframe(data=my_dataframe, use_container_width=True)

# Add a Multiselect
# from snowflake.snowpark.functions import col
#session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.session()

my_dataframe = session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:', my_dataframe ,max_selections = 5
)

# st.write(ingredients_list)
# st.text(ingredients_list)

#  # Cleaning Up Empty Brackets
# if ingredients_list:
#     st.write(ingredients_list)
#     st.text(ingredients_list)

# Changing the LIST to a STRING

# if ingredients_list:
#     st.write(ingredients_list)
#     st.text(ingredients_list)
#     ingredients_string = ''
#     for fruit_chosen in ingredients_list:
#         ingredients_string += fruit_chosen

#  Improve the String Output
if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)
    ingredients_string = ''
    
    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ''
        
    # st.write(ingredients_list)   

# Build a SQL Insert Statement & Test It
    # my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
    #         values ('""" + ingredients_string + """')"""
#  Writing the NAME_ON_ORDER Entry to the Snowflake Table
    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name_on_order + """')"""
    
    #st.write(my_insert_stmt)
    #st.stop()

#  Insert the Order into Snowflake

# if ingredients_string:
#     session.sql(my_insert_stmt).collect()
    
#     st.success('Your Smoothie is ordered!', icon="✅")  

# Add a Submit Button
time_to_insert = st.button('Submit Order')

if time_to_insert:
    session.sql(my_insert_stmt).collect()
    
    st.success('Your Smoothie is ordered!', icon="✅") 

import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response.json())
