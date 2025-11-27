import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key from Streamlit Secrets
genai.configure(api_key="AIzaSyC6zhNsBm0QFqTB59Ebma7Er0t7cmO_2Qs")

model = genai.GenerativeModel("gemini-2.5-pro")

st.title("🌾 Smart Farming Assistant")

prompt = st.text_input("Ask your farming question:")

if st.button("Get Advice"):
    if prompt.strip():
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                st.subheader("AI Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {str(e)}")


