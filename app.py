import streamlit as st
from src.loadserver import LoadServer
from src.emailsender import EmailSender
import os
from PIL import Image
import time
import pandas as pd


ACCEPTED_EXTENTION = ['csv']
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
        body_type = st.selectbox('Message Body Type', ('Plain Text', 'HTML'))
        mail_body = st.text_area('Body')

        uploaded_files = st.file_uploader(
            "Choose file to attach", accept_multiple_files=True)
        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.getvalue()
                emailsender.add_attachment(bytes_data, uploaded_file.name)
            
            recipient_list = []
            recipient_file = st.file_uploader("Add recipient", type=ACCEPTED_EXTENTION)
            if recipient_file is not None:
                reciepient_df = pd.read_csv(recipient_file)
                st.write(reciepient_df.iloc[:,0])
                recipient_list = reciepient_df.iloc[:,0].values.tolist()
                # st.write(recipient_list)

            log_file = ''
            receiver_mail = st.text_input('Mail to')
            successful = 0
            unsuccessful = 0

            if st.button('SEND'):
                if body_type == 'Plain Text':
                    log_file, successful, unsuccessful = emailsender.send_email(
                        recipient_list, mail_subject, mail_body)
                else:
                    log_file, successful, unsuccessful = emailsender.send_html(
                        recipient_list, mail_subject, mail_body)

                st.write(f"### {successful} recived mail")
                st.write(f"### {unsuccessful} didn't recive mail")

            column_download_log, column_recipient_list, column_log_out = st.columns([
                                                                                    1, 1, 1])
            with column_download_log:
                download_log_status = st.download_button(
                    label="Download log",
                    data=log_file,
                    file_name='current_session.log',
                    mime='plain/text')

            with column_log_out:
                if st.button('DISCONNECT'):
                    emailsender.disconnect_server()
                    st.success("Successfully Disconneted from server")
                    st.stop()

    else:
        st.error(f'Please check for correct credential and try again')
        st.stop()
