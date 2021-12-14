import streamlit as st
from src.loadserver import LoadServer
from src.emailsender import EmailSender
import os
from PIL import Image

accepted_file_extention = ['csv','xml']

PWD = os.path.dirname(os.path.abspath(__file__))
st.title("Email Service Clone")

left_side, right_side = st.columns([1, 3])

with left_side:
    path = os.path.join(PWD, 'static', 'pictures', 'email_background.png')
    image = Image.open(path)
    st.image(image)

with right_side:
    st.subheader("Login Page")

    # st.write('Email')
    id = st.text_input("Email ID")
    pw = st.text_input('Password',type='password')
    st.button('Login')

    if id=="admin" and pw == "root":
        validation = True

    else:
        validation = False
    
    if validation:
        st.write('Login Successfull.')
        st.subheader("Email Editor:")
        mail_sub = st.text_input('Subject')
        body_type = st.selectbox('Message Body Type',('Plain Text','HTML'))
        mail_body = st.text_area('Body')
        
        uploaded_file = st.file_uploader("Choose recipient file",type=accepted_file_extention)
        if uploaded_file is not None:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)

    # for validation failure
    else:
        st.write("Login Failed. Kindly try again.")