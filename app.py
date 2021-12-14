import streamlit as st

st.title("Email Service Clone")

c1, c2 = st.columns([1,1])

with c1:
    # 
    pass

with c2:
    st.subheader("Login Page")
    st.write()

    # st.write('Email')
    id = st.text_input("Email ID")
    pw = st.text_input('Password')
    st.button('Login')

    if id=="admin" and pw == "root":
        validation = True

    else:
        validation = False
    
    if validation:
        with c2:
            st.subheader('Successfull.')