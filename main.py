import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Headline Generator",
    page_icon=":memo:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (not recommended for production)
GOOGLE_API_KEY = "AIzaSyCO7WIRmXTQUPeiARLTklKLufkZRfjfg4U"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("Headline Generator")

# User input
user_content = st.text_area("Paste your full content here")

# Combine user input with the prompt for generating headlines using various copywriting frameworks
if st.button("Generate Headlines"):
    prompt = f"""
    Based on the following content, generate the best possible headlines using different copywriting frameworks. Here are the content and frameworks:

    Content:
    {user_content}

    Frameworks:
    1. **AIDA (Attention, Interest, Desire, Action)**
       - Description: Grabs attention, sparks interest, creates desire, and prompts action.
       - Example: "Unlock Your Dream Job in Just 30 Days: Discover the Proven System That Top Professionals Use!"
    2. **PAS (Problem, Agitation, Solution)**
       - Description: Identifies a problem, amplifies it, and presents a solution.
       - Example: "Tired of Sleepless Nights? Discover How Our Revolutionary Pillow Can Change Your Life!"
    3. **Before-After-Bridge**
       - Description: Describes the current situation, the improved situation, and how to bridge the gap.
       - Example: "Before: Struggling with Excess Weight? After: Enjoy a Leaner, Healthier Body! Bridge: Try Our New Diet Plan and Start Your Transformation Today!"
    4. **FAB (Features, Advantages, Benefits)**
       - Description: Lists features, explains advantages, and highlights benefits.
       - Example: "Our Smartwatch (Feature) Tracks Your Sleep Patterns (Advantage) So You Can Wake Up Feeling Refreshed Every Morning (Benefit)!"
    5. **4P (Promise, Picture, Proof, Push)**
       - Description: Makes a promise, helps the reader visualize the outcome, provides proof, and encourages immediate action.
       - Example: "Achieve a Flawless Smile (Promise) with Our Advanced Whitening Kit (Picture). Trusted by Thousands (Proof) – Order Now and See Results in Just One Week (Push)!"
    6. **Numbered List**
       - Description: Uses a numbered list to create urgency or highlight key points.
       - Example: "5 Reasons Why You Should Invest in Cryptocurrencies"
    7. **How-To**
       - Description: Offers a solution or guidance on a specific topic.
       - Example: "How to Build a Successful Personal Brand"
    8. **Question**
       - Description: Peaks curiosity and encourages clicks.
       - Example: "Are You Making These Common Grammar Mistakes?"
    9. **Comparison**
       - Description: Contrasts two ideas or items to create intrigue.
       - Example: "iPhone vs. Android: Which is Best for You?"
    10. **Benefit-Focused**
        - Description: Highlights the advantages of a product or service.
        - Example: "Boost Your Productivity with These Time-Saving Tips"
    11. **Problem-Solution**
        - Description: Identifies a problem and offers a solution.
        - Example: "Tired of Back Pain? Try This Yoga Routine"
    12. **Testimonial**
        - Description: Uses a quote or endorsement to build credibility.
        - Example: "Customer Raves: Our Skincare Products Changed My Life"
    13. **Intrigue**
        - Description: Creates curiosity and makes readers want to know more.
        - Example: "You Won't Believe What Happened Next..."
    14. **Keyword-Optimized**
        - Description: Incorporates relevant keywords for SEO purposes.
        - Example: "Best SEO Tools for Small Businesses in 2024"
    15. **Urgent/Time-Sensitive**
        - Description: Creates a sense of urgency or limited availability.
        - Example: "Last Chance to Save 50% on Our Summer Sale!"

    Provide fifteen distinct headlines that use these frameworks to effectively capture attention and engage the reader.
    """
    
    with st.spinner("Generating headlines..."):
        # Generate headlines using the Gemini-Pro model
        response = model.generate_content([prompt])
        headlines = response.text

    # Display the headlines
    st.subheader("Generated Headlines")
    st.write(headlines)
