import streamlit as st
from math import pi


st.header('Circumference of Cladding')
st.header(' Cir = 2πr + Lap + Play')
st.header('You Will Need To Enter')


col1, col2, = st.columns([1,3])

with col1:
    dia = size_a = st.text_input('Pipe Size in mm.')
    lag = size_a = st.text_input('Insulation Thickness in mm.')


btn = st.button('Calculate')
if btn:
#    dia = 168  ###DEBUG. Unmute dia
#    lag = 50   ###DEBUG. Unmute lag
#    st.header('---DEBUG---')


    wrkDia = int(dia) + (int(lag) * 2)

    if wrkDia < 120:
        lap = 20
    if wrkDia >= 120:
        lap = 30
    if wrkDia >= 450:
        lap = 50
    if wrkDia >= 2500:
        lap = 100
    
    if wrkDia < 120:
        play = 4
    if wrkDia >= 120:
        play = 5
    if wrkDia >= 500:
        play = 10
    if wrkDia >= 2500:
        play = 20  

    fullDia = wrkDia + play
    cir = pi * wrkDia
    fullCir = pi * fullDia 
    cirLap = fullCir + lap
    dia2 = int(dia)
    lag2 = int(lag)


#    st.header("--------------TOTALS-------------")
    st.header(f"{dia2}/{lag2} mm")
    #st.header(f"Thickness Of Insulation---------{lag}mm") 
    st.header(f"Diameter {fullDia} mm")

    st.header(f"Cir is %.0f mm " %cirLap)
    st.write(f"Includes {lap} mm of lap and {play} mm of play")



#    df = {'Pipe Size':[dia], 'Insulation':[lag], 'FullDiameter':[fullDia], 'Lap':[lap], 'Cut Size':[cirLap]}
#    #df
#    st.dataframe(df)


#    col1, col2, col3 = st.columns(3)

#    with col1:
#        st.radio('Choose a Catagory', ('Cladding', 'Insulation', 'Both'))
#        st.radio('Choose a Catagory', ('Hotwork', 'Coldwork', 'Both'))
#    with col2:
#        st.radio('Choose a Catagory', ('Hotwork2', 'Coldwork2', 'Both2'))
#    with col3:
#        st.radio('Choose a Catagory', ('Copper', 'Carbon Steel', 'Stainless Steel', 'Dairy SS'))



#    cat = st.radio('Choose a Catagory', ('Cladding3', 'Insulation3'))
#    if cat:
#        st.write('You Chose ', cat)






