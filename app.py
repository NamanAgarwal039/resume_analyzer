import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pypdf import PdfReader

# 1. Load environment variables (for local use)
load_dotenv()


if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
else:
    api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)


def get_working_model():
    try:
        model_list = genai.list_models()
        for m in model_list:
            if 'generateContent' in m.supported_generation_methods:
                if 'flash' in m.name: return m.name
                if 'pro' in m.name: return m.name
        return "models/gemini-pro"
    except Exception:
        return "models/gemini-pro"

# 4. Function to extract text from PDF
def get_pdf_text(uploaded_file):
    text = ""
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text()
    return text

# 5. Function to query Gemini
def get_gemini_response(input_prompt, pdf_text, job_description):
    model_name = get_working_model()
    model = genai.GenerativeModel(model_name)
    full_prompt = f"{input_prompt}\n\nResume Text:\n{pdf_text}\n\nJob Description:\n{job_description}"
    response = model.generate_content(full_prompt)
    return response.text

# 6. Streamlit UI
st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
st.title("AI Resume Analyzer")
st.text("Improve your resume ATS score with Gemini AI")

jd = st.text_area("Paste the Job Description (JD)", height=150)
uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type="pdf")
submit = st.button("Analyze Resume")

input_prompt = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and software engineering. 
Your task is to evaluate the resume against the provided job description. 
Please provide your response in the following clear structure:

1. **Match Percentage**: Give a score out of 100% based on keywords and skills match.
2. **Missing Keywords**: List the specific important keywords from the JD that are missing in the resume.
3. **Profile Summary**: A brief evaluation of the candidate's profile.
"""

if submit:
    if uploaded_file is not None and jd:
        with st.spinner("Analyzing..."):
            try:
                resume_text = get_pdf_text(uploaded_file)
                response = get_gemini_response(input_prompt, resume_text, jd)
                st.subheader("ATS Analysis Result:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please upload a PDF resume and paste the Job Description.")
