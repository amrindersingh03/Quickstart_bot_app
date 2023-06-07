import streamlit as st
import openai

st.title('First_app')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
    # Use the OpenAI API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        temperature=0.7,
        max_tokens=100,
        n = 1,
        stop = None,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    st.info(response.choices[0].text.strip())

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')

    if submitted and openai_api_key:
        openai.api_key = openai_api_key
        generate_response(text)
