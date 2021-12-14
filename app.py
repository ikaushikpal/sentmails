import streamlit as st
from src.loadserver import LoadServer
from src.emailsender import EmailSender
import os
from PIL import Image
import time


ACCEPTED_EXTENTION = ['csv','xml']
emailsender = EmailSender()
loadserver = LoadServer()
loadserver.parse_json()
PWD = os.path.dirname(os.path.abspath(__file__))
st.title("Email Service Clone")


# with left_side:
#     path = os.path.join(PWD, 'static', 'pictures', 'email_background.png')
#     image = Image.open(path)
#     st.image(image)

# with right_side:
email_id = st.text_input("Email ID")
password = st.text_input('Password', type='password')
emailsender.add_user_credential(email_id, password)

server = st.selectbox('Select proper SMTP server',
                      loadserver.service_names)
host = loadserver.json[server]['server']
port = loadserver.json[server]['port']

state = st.checkbox('CONNECT')

if state:
    if emailsender.connect_server(host, port):
        st.success(f'Successfully connected to {host}:{port}')
        mail_subject = st.text_input('Subject')
        body_type = st.selectbox('Message Body Type',('plain','html'))
        mail_body = st.text_area('Body')
        emailsender.build_message(mail_subject, mail_body, body_type)
        
        uploaded_files = st.file_uploader("Choose file to attach")
        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.getvalue()
                emailsender.add_attachment(bytes_data, uploaded_file.name)
        
            st.write(f"{[uploaded_file.name for uploaded_file in uploaded_files]}")
    # for validation failure
    else:
        st.error(f'Please check for correct credential and try again')
