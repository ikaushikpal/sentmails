import streamlit as st
from src.loadserver import LoadServer
from src.emailsender import EmailSender
import os
from PIL import Image
import time


emailsender = EmailSender()
loadserver = LoadServer()
loadserver.parse_json()
MSG_STATE = True
PWD = os.path.dirname(os.path.abspath(__file__))
st.title("Email Service Clone")


def print_message(msg):
    st.write(msg)


# left_side, right_side = st.columns([1, 2])

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
# c1, c2, c3 = st.columns([1, 1, 1])

# with c2:
state = st.button('CONNECT')

if state:
    if emailsender.connect_server(host, port):
        st.success(f'Successfully connected to {host}:{port}')
    else:
        st.error(f'Please check for correct credential and try again')
