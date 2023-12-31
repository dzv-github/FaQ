import streamlit as st
import openai

openai.api_key=st.secrets["api_key"]

st.title('AI_Flow')

with st.form("form"):
    user_input=st.text_input("Prompt")
    submit=st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt=[{
        "role":"system",
        "content":"Imagine the detail appearance of the input.Response it shortly around 20 words."
    }]

    gpt_prompt.append({
        "role":"user",
        "content":user_input
    })

    with st.spinner("Waiting..."):
        gpt_response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    # gpt_response =  openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role" : "system", "content" : "Imageine the detail appearance of the input.Response it shortly."},
    #         {"role" : "user", "content" : user_input}
    #     ]
    # )

        prompt=gpt_response["choices"][0]["message"]["content"]
    #st.write(prompt)
        dalle_response=openai.Image.create(
            prompt=prompt, 
            size="256x256"
        )

    st.image(dalle_response["data"][0]["url"])