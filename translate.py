import streamlit as st
from googletrans import Translator
st.header("Machine Translation demo")
input_text = st.text_area("Please  Enter the text",value='')
option = st.selectbox('To which language you wish to translate:', ('Malayalam', 'Hindi', 'Tamil', ))
if st.button("Translate"):
    translator = Translator()
    translation = translator.translate(input_text, dest=option)
    st.write(translation.text)