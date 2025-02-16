import google.generativeai as genai
import streamlit as st

genai.configure(api_key="Your_API_KEY")

st.subheader("Want someone to hear you out?")
st.write("**We are here for you Call on, +91 9152987821 or +91-9315767849**")

st.divider()

st.link_button("Counseling", "https://www.betterlyf.com/")
st.link_button("Online Support Group", "https://icallhelpline.org/")
st.link_button("Therapy", "https://www.amahahealth.com/therapy-psychiatry/lpexpt/2b3/?utm_source=google&medium=cpc&utm_campaign=tele_therapy_bofl_psychologist_phrase_27aug24&utm_term=psychologist+online&campaignid=21638803118&adgroupid=172216427648&adid=711218718866&gad_source=1&gclid=CjwKCAiAhP67BhAVEiwA2E_9g8OyFXoT3sByCl2tRFEtucDtYC1oytydbA-uO3ZwM_SmFP6lV5WOnBoCKu0QAvD_BwE&ispm=true")

st.divider()

def mhealth(what):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Correct API usage
    response = model.generate_content(
        f"I'm facing {what}. Can you please help me overcome it and handle me with care and concern? Try to cheer me up."
    )
    return response.text

st.subheader("**Get personalized help based on what you're facing**")
what = st.text_input("Describe the issues/symptoms you're experiencing:")

if what:
    response = mhealth(what)
    st.write(response)
