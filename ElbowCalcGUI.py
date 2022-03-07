import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



st.header('ENTER')

x = st.text_input('Working Diameter')

st.header('OR')


col1, col2, = st.columns([1,3])

with col1:
    dia = st.text_input('Bare Pipe size in mm.')
with col2:
    lag = st.text_input('Thickness of Insulation in mm.')


x = []
y = []
x = np.linspace(0,314, num=25)
y = np.sin(x*0.02)


a = x*3.14


#st.write(x, y)

df =  {'X / Diameter':y, 'Y / Circumfrence':x}
#st.dataframe(df)
#st.table(df)


st.line_chart(df)


with st.expander('X/y Mesurements for an Elbow'):
    st.table(df)


with open('example.py', 'rb') as file:
    st.download_button(label='Download table as a .CSV file', data=file, file_name = 'example.py', mime='py')


with st.expander('Elbow Pattern'):
    st.image('https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?cs=srgb&dl=pexels-pixabay-256381.jpg&fm=jpg')


with open('image.png', 'rb') as file:
    st.download_button(label='Download Pattern', data=file, file_name = 'image.png', mime='png')


    
    
    
    