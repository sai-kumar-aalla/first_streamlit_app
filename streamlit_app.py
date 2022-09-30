import streamlit

streamlit . title('my parent new healthy diner')

streamlit.header('breakfast menu')
streamlit.text('omega 3 & blueberry Oatmeal')
streamlit . text ('kale,spinach & rocket smoothie')
streamlit . text ('hard-boiled free-range egg')
streamlit . text ('avocado toast')

streamlit.header('bulid your own fruit smoothie')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazon.com/dabw/fruit_macors.txt"
streamlit.dataframe(my_friut_list)

