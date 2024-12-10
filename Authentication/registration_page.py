import streamlit as st
import datetime
import pandas as pd
from helpers import connect_to_collection

def registration_page():
    placeholder = st.empty()

    with placeholder.form("registration"):
        st.subheader("REGISTER USER")
        username = st.text_input("User Name*")
        password = st.text_input("Password*", type="password")
        repeat_password = st.text_input("Repeat Password*", type="password")
        name = st.text_input("Enter Name")
        age = st.number_input("Enter Age", min_value=18, step=1)
        pet = st.text_input("Enter Plant Name")
        submit_button = st.form_submit_button("Register")

    if submit_button:
        # define the database
        db_name = 'streamlit_registration_data'
        # define the collection
        collection_name = 'userinfo'
        collection = connect_to_collection(db_name, collection_name)

        # write some dummy data to the collection so it does not error
        dummy_data = {"user_name": "test"}
        collection.insert_one(dummy_data)

        # read the data from the collection and identify user names
        user_data = pd.DataFrame(list(collection.find()))
        usernames = list(user_data.user_name)

        if len(username) < 1 and len(password) < 1:
            st.error("ENTER USERNAME AND PASSWORD", icon="⚠️")
        elif len(username) < 1:
            st.error("ENTER USERNAME", icon="⚠️")
        elif len(password) < 1:
            st.error("ENTER PASSWORD", icon="⚠️")
        elif password != repeat_password:
            st.warning("PASSWORDS DONT MATCH", icon="⚠️")
        elif username in usernames:
            st.warning("USERNAME ALREADY EXISTS", icon="🔥")
        else:
            # create a document with the data we want to write to this collection
            document = {"user_name": username,
                        "password": password,
                        "name": name,
                        "age": age,
                        "pet": pet,
                        "created_at": datetime.datetime.now()}

            # write this document to the collection
            collection.insert_one(document)

            # clear everything and set credential check flag to True
            placeholder.empty()
            # option 2,
            st.title(f"Welcome New User")
            # place an image
            st.image(
                "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2t6NXR3NGhsNW90NHU5MnB5anliMHlxdm40NDczaW1jeTdpZ3lvZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1iLVjz6PbgRuOOxa/giphy.gif")