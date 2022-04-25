import redis
import streamlit as st

sensoren = {
    1600:"Helligkeit",
    1601:"Windstärke",
    1602:"Regenmenge",
    1618:"Schalter Wohnen",
    1623:"Schalter 1 Keller",
    1624:"Schalter 2 Keller"}

st.title("Projektarbeit")
r = redis.Redis()
selectbox1 = st.sidebar.selectbox('Navigation:',('SmartHome','Lichtsteuerung','Garage','Wetter'))

#######################################################################

if selectbox1 == 'SmartHome':
    sensorbox = st.selectbox("Sensoren",sensoren.values())
    if sensorbox:
        for i in sensoren:
            if sensorbox == sensoren[i]:
                sensorist = r.get(i).decode()
                st.write(sensorbox, sensorist)



#######################################################################                
if selectbox1 == 'Lichtsteuerung':
    btnon = st.button("Lampe Ein")
    if btnon:
        r.set("1714","1")
    btnoff = st.button("Lampe Aus")
    if btnoff:
        r.set("1714","0")
if selectbox1 == 'Garage':
    st.balloons()
#######################################################################
if selectbox1 == 'Wetter':        
    btnmarkise_raus = st.button("Markise raus")
    if btnmarkise_raus:
        r.set("1707","1")
        r.set("1706","0")
    btnmarkise_rein = st.button("Markise rein")
    if btnmarkise_rein:
        r.set("1706","1")
        r.set("1707","0")

#######################################################################



