

import streamlit as st

st.header('YouTube Tutorial')
st.code('https://www.youtube.com/watch?v=0U43e_ssW8k')
st.title('Streamlit Functions and Examples')

st.write(' ')
# Display Text
#   Title / Header / Subheader / Text / Caption / Code / Markdown
st.write('# Display Text - Title / Header / Subheader / Text / Caption / Code / Markdown')

st.write(' ')
st.write(' ')

st.title('This is the "Title"')
st.header('The Header')
st.subheader('subheader')
st.text('Raw Text')
st.caption('caption')
st.code('for i in range(20): print i')
st.markdown('# *Heading using markdown*')
st.write('<h3>This is normal writing</h3>', unsafe_allow_html = True)


st.write(' ')

# Display interactive wigets
#   button / download button / checkbox / radio / selectbox / multiselect / slider / select_slider
st.write('# Display interactive wigets')
st.write('### button / download button / checkbox / radio / selectbox / multiselect / slider / select_slider')
st.write(' ')

btn = st.button('Click')

if btn:
    st.write('I was clicked')


with open('image.png', 'rb') as file:
    st.download_button(label='Download an Image', data=file, file_name = 'image.png', mime='png')

with open('example.py', 'rb') as file:
    st.download_button(label='Download This Page', data=file, file_name = 'example.py', mime='py')

ch = st.checkbox('I agree with terms and conditions')
if ch:
    st.write("No you Don't  !!!!!!")


r = st.radio('Choose a Catagory', ('Buisiness', 'Politics', 'Sports'))
if r:
    st.write('You Chose ', r)


st.selectbox('Choose a Catagory',  ['Buisiness', 'Politics', 'Sports'])


st.multiselect('Choose a Catagory',  ['Buisiness', 'Politics', 'Sports'])


sl = st.slider('Choose a range', 0,  100)

st.write('You chose ', sl)

st.select_slider('Choose ', ['Jack', 'John', 'Mary', 'Alex', 'Rob'])

size = st.select_slider('Choose ', ['1"', '2"', '3"', '4"', '5"'])
st.write('You chose ', size)



# text_input / number_input / text_area / time_input / date_input / color_picker / file_uploader
st.write('# Text_input / number_input / text_area / time_input / date_input / color_picker / file_uploader')


col1, col2, = st.columns([1,3])

with col1:
    st.text_input('Enter your name')
with col2:
    st.text_area('Your message')


st.number_input('Your age')
st.time_input('Time')
st.date_input('Date')
st.color_picker('Color')
st.file_uploader('Upload Your File')



# Display Media
st.write('# Display Media')

st.image('https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?cs=srgb&dl=pexels-pixabay-256381.jpg&fm=jpg')

#st.audio(https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?cs=srgb&dl=pexels-pixabay-256381.jpg&fm=jpg)

st.video('https://www.youtube.com/watch?v=0U43e_ssW8k')



# Display Data
#   Dataframe / Table / Metric
st.write('### Display Data - Dateframe / Table / Metric')



df =  {'name':['Jack', 'John', 'Mary', 'Alex', 'Rob'], 'age':[25, 55, 34, 21, 30]}
df

st.dataframe(df)

st.table(df)

st.metric('Temperature', "24 'C", 6)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Temperature', "24 'C", -4)
with col2:
    st.metric('Temperature', "20 'C", -8)
with col3:
    st.metric('Temperature', "32 'C", 4)



# Layouts
#   Sidebar / Columns / Expander
st.write('# Layouts - Sidebar / Columns / Expander')
st.write('### ')



with st.expander('Click Here'):
    st.image('https://images.pexels.com/photos/256381/pexels-photo-256381.jpeg?cs=srgb&dl=pexels-pixabay-256381.jpg&fm=jpg')


st.sidebar.title('This is a "Sidebar"')
st.sidebar.button('CLICK ME')




# Display progtress and status
#   spinner / baloons / error / warning / info / success / exception
st.write('# Display progress and status')
st.write('### spinner / baloons / error / warning / info / success / exception')

st.progress(70)


st.success('Thank You !')
st.info('info')
st.warning('Warning')
st.error('Ooops')
e = RuntimeError('Something Wrong')
st.exception(e)



import time
with st.spinner('Wait for 3 seconds...'):
    time.sleep(3)
st.write('Thank You !')



#st.balloons()



















