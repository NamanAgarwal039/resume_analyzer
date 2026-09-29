AI Resume Analyzer

An interactive Streamlit web application that analyzes PDF resumes against job descriptions using Google's Gemini AI. The app acts as an Applicant Tracking System (ATS) scanner to calculate a match percentage, identify missing keywords, and provide a detailed profile evaluation.

📁 Repository Structure

.
├── app.py                # Main Streamlit application file
├── requirements.txt      # Required Python packages
├── .env                  # Environment variables file (local API key)
└── README.md             # Project documentation

🚀 Features

PDF Resume Extraction: Extracts text seamlessly from uploaded PDF resumes using pypdf.

Dynamic Gemini Model Fallback: Automatically searches for and selects available Gemini models (favoring Flash or Pro models).

ATS Match Score: Provides an estimated compatibility percentage based on skills and experience.

Missing Keywords Identification: Lists important terms and skills present in the Job Description but absent from the resume.

Profile Summary: Generates a concise summary highlighting strengths and growth areas for the applicant.

🛠️ Requirements

Create a requirements.txt file containing the following dependencies:

streamlit
google-generativeai
python-dotenv
pypdf


⚙️ Setup & Installation

1. Prerequisites

Make sure you have Python 3.8 or higher installed and a Google Gemini API Key (you can get one from Google AI Studio).

2. Installation Steps

Clone the repository:

git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer


Create and activate a virtual environment:

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up environment variables:
Create a .env file in the root directory:

GOOGLE_API_KEY="your_actual_gemini_api_key_here"


(Note: If deploying on Streamlit Community Cloud, add GOOGLE_API_KEY under your app's Secrets settings instead).

💻 Running the Application

Launch the Streamlit app with:

streamlit run app.py


Open your browser at http://localhost:8501.

Paste the target Job Description.

Upload your Resume (PDF format).

Click Analyze Resume to receive the ATS breakdown.
