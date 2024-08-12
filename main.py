import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="SEO Keyword Generator",
    page_icon=":mag_right:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("SEO Keyword Generator")

# User input
user_topic = st.text_area("Enter your main topic or focus keyword")

# Combine user input with the prompt for generating SEO keywords
if st.button("Generate Keywords"):
    prompt = f"""
    Generate a list of low competition SEO keywords related to the topic '{user_topic}'. Provide a mix of short-tail and long-tail keywords that have low competition and high potential for ranking well.
    """

    with st.spinner("Generating SEO keywords..."):
        # Generate keywords using the Gemini-Pro model
        response = model.generate_content([prompt])
        keywords = response.text

    # Display the keywords
    st.subheader("Generated SEO Keywords")
    st.write(keywords)