import streamlit as st

a = ("Benfica.jpeg")
b = ("Benfica2.jpeg")
c = ("Benfica3.jpeg")
d = ("Benfica4.jpeg")
e = ("Herunterladen.jpeg")
f = ("OIP.jpeg")

col1, col2, col3 = st.columns (3)
col4, col5, col6 = st.columns (3)

with col1:
    st.image(a)
with col2:
    st.image(b)
with col3:
    st.image(c)
with col4:
    st.image(d)
with col5:
    st.image(e)
with col6:
    st.image(f)

