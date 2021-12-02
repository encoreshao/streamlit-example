import altair as alt
import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt
from Portfolio import *
from ETF import *

im = Image.open("1566968153508.png")
st.set_page_config(page_title='Tensor Data Platform',  layout='wide', page_icon=im)  # this needs to be the first Streamlit command



st.sidebar.image('1566968153508.png', width=200)
st.sidebar.title('Tensor Data Platform')
st.sidebar.markdown('Alpha')
st.sidebar.header('Navigation')

options = st.sidebar.radio('Select a page:', 
    ['Home', 'Portfolio Information', 'Categories Information', 'ETF Information'])

st.sidebar.markdown('---')
st.sidebar.write('Tensor Investment Corporation')

#layout
if options=="Home":
    st.write("Tensor Investment Corporation")
if options == 'Portfolio Information':
    set_Portfolio()
if options == 'ETF Information':
    set_ETF()





