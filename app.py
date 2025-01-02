import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Set the page configuration
st.set_page_config(
    page_title="YT or Website Summarizer",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Add a banner image at the top
st.image(
    "image.png",  # Replace with your banner image URL or local path
    use_container_width=True,
)

# Title and subtitle
st.title("📄 Content Summarizer")
st.subheader("Summarize  Content from YouTube or Any Website")

# Add a description with an icon
st.markdown(
    """
    Welcome to the **Content Summarizer**! Simply enter a YouTube or website URL, and our tool will provide you with a concise summary of the content.
    """
)

# Sidebar for Groq API Key and Guidance
with st.sidebar:
    st.header("🔑 Groq API Key")
    st.markdown(
        """
        To use this app, you'll need a **Groq API Key**. Follow the steps below to obtain one:
        
        1. **Sign Up**: Visit the [Groq Website](https://groq.com/) and sign up for an account.
        2. **Navigate to API Section**: Once logged in, go to the API section in your dashboard.
        3. **Generate API Key**: Click on "Generate New API Key" and copy the key.
        4. **Enter API Key Below**: Paste your API key into the input box below.
        """
    )
    groq_api_key = st.text_input("Enter your Groq API Key", value="", type="password")
    
    # Optional: Add a Groq logo or relevant image
    st.image(
        "https://your-image-url.com/groq-logo.png",  # Replace with your Groq logo URL or local path
        width=150,
    )

# Input for URL
st.markdown("---")  # Horizontal separator
url = st.text_input("🔗 Enter the YouTube or Website URL you want to summarize:")

# Initialize the language model
if groq_api_key.strip():
    llm = ChatGroq(model="llama-3.3-70b-versatile", groq_api_key=groq_api_key)
else:
    llm = None  # Will handle below

# Define the prompt template
prompt_template = """
Provide a summary of the following content in 300 words:
{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Button to trigger summarization
if st.button("📄 Summarize the Content"):
    if not groq_api_key.strip():
        st.error("⚠️ Please provide a valid Groq API key in the sidebar.")
    elif not url.strip():
        st.error("⚠️ Please enter a URL to summarize.")
    elif not validators.url(url):
        st.error("⚠️ The URL provided is not valid. Please enter a valid URL.")
    else:
        try:
            # Load content based on URL type
            if "youtube.com" in url or "youtu.be" in url:
                loader = YoutubeLoader.from_youtube_url(url)
                st.info("🔄 Loading content from YouTube...")
            else:
                loader = UnstructuredURLLoader(
                    urls=[url],
                    ssl_verify=False,
                    headers={
                        "User-Agent": (
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                            "Chrome/116.0.0.0 Safari/537.36"
                        )
                    },
                )
                st.info("🔄 Loading content from the website...")
            
            data = loader.load()
            
            # Ensure content exists
            if not data or not data[0].page_content.strip():
                st.error("⚠️ No content was found at the specified URL.")
            else:
                with st.spinner("📝 Summarizing the content..."):
                    # Set up and run the summarization chain
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    output_summary = chain.run({"input_documents": data})
                
                # Display the summary
                st.success("✅ Summary Generated Successfully!")
                st.write(output_summary)
                
                # Optional: Provide download option for the summary
                st.download_button(
                    label="📥 Download Summary",
                    data=output_summary,
                    file_name="summary.txt",
                    mime="text/plain",
                )
        
        except Exception as e:
            st.exception(f"🚨 An error occurred: {e}")

# Add a footer with your logo or additional information
st.markdown("---")
st.markdown(
    """
    © 2025 Your Company Name. All rights reserved.
    """
)
st.image(
    "https://your-image-url.com/footer-logo.png",  # Replace with your footer image URL or local path
    width=100,
)
