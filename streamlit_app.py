import streamlit
import pandas
streamlit.title('My Parents new healthy diner');
streamlit.header('Breakfast menu');
streamlit.text('🥣Omega 3 & Blueberry Oatmeal');
streamlit.text('🥗Kale, Spinach & Rocket Smoothie');
streamlit.text('🐔Hard-boiled Free-range Egg');
streamlit.text('🥑Avacade, 🍞Toast');

streamlit.header('🍌🥭Build your own smoothie🥝🍇');
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");
streamlit.dataframe(my_fruit_list);
