import streamlit as st
from qr_decode import qr_decode
from qrcode_generator_page import qrcode_generator_page

st.set_page_config(page_title="QR Code App",
                   page_icon= ":smile:" )

options = ['Create QR code', 'Decode QR code', 'About Me']
page_selection = st.sidebar.selectbox("Menu",
                                    options)

st.write(page_selection)

if page_selection== "Create QR code":
    qrcode_generator_page()
elif page_selection=="Decode QR code":
    qr_decode()
elif page_selection== "About Me":
    st.write("Hi! I am Refiye! :smile:")
    #st.image("data:image/")

