📄 Content Summarizer

A powerful Streamlit app that summarizes content from YouTube videos and websites using LangChain and the Groq API. This app extracts key insights from lengthy content, saving you time and effort.
🚀 Features

    🌐 Summarize Content: Process URLs from YouTube and websites to generate concise summaries.
    🧠 Powered by AI: Utilizes advanced AI models via the Groq API for accurate results.
    💻 User-Friendly Interface: Intuitive and simple-to-use design built with Streamlit.
    📥 Downloadable Summaries: Save summaries as text files for later use.

🖥️ Demo


Replace assets/screenshot.jpg with your screenshot's path.
🛠️ Setup Instructions
1. Clone the Repository

git clone https://github.com/hassan-2050/Content-Summarizer.git
cd Content-Summarizer

2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure API Key

    Obtain your Groq API Key from Groq API Website.

    Create a .env file in the project root and add your key:

    GROQ_API_KEY=your_groq_api_key

📝 Usage Instructions
1. Run the Application

Launch the Streamlit app:

streamlit run app.py

2. Input Your URL

    Enter a YouTube or website URL into the text box.
    Click "Summarize the Content" to generate a summary.

3. View and Download Summary

    The summary will be displayed on the screen.
    Use the Download Summary button to save the results.

🌟 Features in Detail
🔑 API Key Management

The app uses the Groq API for summarization. Keep your API key secure by using a .env file, which is automatically excluded from Git via .gitignore.
📄 Supported URLs

    YouTube Videos: Extract transcripts and generate summaries.
    Websites: Parse text content for summarization.

🚦 Error Handling

    Validates URLs before processing.
    Provides user-friendly error messages for invalid or unsupported URLs.

🧑‍💻 Contributing

Contributions are welcome! To contribute:

    Fork this repository.
    Create a new branch (feature/your-feature).
    Commit your changes (git commit -m "Add new feature").
    Push to the branch (git push origin feature/your-feature).
    Open a pull request.

📋 To-Do

Add support for other media types (e.g., PDFs).
Enhance summarization with more AI models.

    Add multi-language support.

🖼️ Screenshots
Input URL

Generated Summary

🛡️ License

This project is licensed under the MIT License.
📞 Contact

For questions, suggestions, or collaborations, feel free to reach out:

    Email: hassan@example.com
    GitHub: Hassan's GitHub