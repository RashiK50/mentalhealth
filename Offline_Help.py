import streamlit as st
import requests, json 
import os
from dotenv import load_dotenv

load_dotenv()

GMAP_API_KEY = os.getenv("GMAP_API_KEY")

api_key = "Your_API_KEY"

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

def gmap(query, api_key):
    r = requests.get(url + 'query=' + query +'&key=' + api_key) 
    x = r.json() 
    y = x['results'] 
    for i in range(len(y)): 
        return(y[i]['name']) 

st.link_button("Offline Support Group","https://vandrevalafoundation.com/")

st.divider()

st.subheader("You can also search for nearby mental health help centres")
query=st.text_input("Search here")
if query:
    response = gmap(query, api_key)
    st.write(response)
