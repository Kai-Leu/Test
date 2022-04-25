import redis
import streamlit as st
import socket
import logging
import sys
import threading
import time

UDP_IP = '127.0.0.1'
UDP_PORT = 1709 
#Lampe E1 Schlafzimmer 1716
#UDP_PORT = 1627 #Schalter S12 Schlafzimmer
#RUN = 1


r = redis.Redis()

#r.set('name', 'wert') für das Setzen; auch direkt über Redis-Client möglich.

name1 = r.get('daniel').decode('UTF-8')
print(name1)


name2 = r.get('kairi').decode('UTF-8')
print(name2)


r.set('felix', 'dozierender')
name3 = r.get('felix').decode('UTF-8')
print(name3)


name4 = r.get('livio').decode('UTF-8')
print(name4)


name5 = r.get('filipe').decode('UTF-8')
print(name5)


name6 = r.get('marcel').decode('UTF-8')
print(name6)


name7 = r.get('sven').decode('UTF-8')
print(name7)


#print(r.get('marco'))

name8 = r.get('marco').decode('UTF-8')
print(name8)



st.title("Übung Redis")

section = st.sidebar.radio("Auswahl:" , ('Sidebar 1: Übungen', 'Sidebar 2: Anlagenmodell'))

if section == "Sidebar 1: Übungen":

    st.header("Ü1: Hinzufügen ins Redis")
    st.write("Über den Redis-Client wurden die Personen definiert.")



    st.header("Ü2: Alle in der Klasse")
    st.write(name1, name2, name3, name4, name5, name6, name7, "und", name8)

    st.header("Ü3: Ausgabe der Einzelnen")
    if st.button('Daniel'):
        st.write("Das Geschlecht ist:", name1)

    if st.button('Kairi'):
        st.write("Das Geschlecht ist:", name2)




if section == "Sidebar 2: Anlagenmodell":

    st.header("Ü4: Redis und Streamlit")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def Lichtschalter_E1(message):
        sock.sendto(bytes(message, "UTF-8"), (UDP_IP, UDP_PORT))

    if st.button('Leuchte E1: Einschalten'):
        Lichtschalter_E1('1')
        r.set('Lichtschalter', 'EIN')

    if st.button ('Leuchte E1: Ausschalten'):
        Lichtschalter_E1('0')
        r.set('Lichtschalter', 'AUS')


""""
    import Connector


    def main():
        if st.button('Einschalten E1'):
            togglelamp(1716)

    if __name__ == "__main__":
        main()

"""

#ÄNDERUNG VON Filipe Ineichen
