Automatic Resume Analyzer
The Automatic Resume Analyzer is a Streamlit application designed to analyze resumes uploaded in PDF format. Leveraging the Google Gemini API, the application performs natural language processing (NLP) and image analysis to provide insights into the suitability of a candidate's profile for specific job roles.

Purpose:
Hiring processes often involve manual review of numerous resumes, which can be time-consuming and subjective. This application aims to automate and enhance the resume review process by:
 Professional Evaluation: Providing HR professionals with a brief evaluation of whether a candidate's profile aligns with a given job description.
 Critique and Suggestions: Offering feedback on areas where a resume may be lacking and suggesting improvements to enhance the candidate's profile.
 Percentage Match: Calculating the percentage match between the content of the resume and the requirements specified in the job description.
 Features
 PDF to Image Conversion: Converts the uploaded PDF resume into an image format (JPEG) using pdf2image, facilitating image-based analysis.
 Google Gemini API Integration: Utilizes the Google Gemini API through the google.generativeai Python client to generate content based on the input provided and the converted resume image.
 Interactive Web Interface: Built using Streamlit, allowing users to upload resumes, input job descriptions, and select from multiple analysis options through buttons.
