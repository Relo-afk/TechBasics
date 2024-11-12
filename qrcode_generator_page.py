import os
import time

import streamlit as st
import segno



def qrcode_generator_page():
    st.title ("QR CODE GENERATOR🔍")

    st.image ("https://t4.ftcdn.net/jpg/02/18/18/55/360_F_218185587_P4zituDtWJOfClUKL6merI0BgLMIxoeC.jpg")

    #text input box

    url = st.text_input("Enter the link you want to encode")
    color = st.color_picker("Pick a color for your QR Code", "#00f900")
    button = st.button
    def generate_qrcode(url, color):
        #if directory does not exist create it
        directory_path ='images'
        os.makedirs(directory_path, exist_ok=True)

        qrcode = segno.make_qr(url)
        qrcode.to_pil(scale=10,
                       dark=color).save("images/qrcode_streamlit.png")
    if button and url:
        with st.spinner("Generating"):
            time.sleep(2)
        generate_qrcode(url, color)
        st.image("images/qrcode_streamlit.png")

    st.button("GENERATE")

