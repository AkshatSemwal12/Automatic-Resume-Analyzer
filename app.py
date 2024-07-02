
from dotenv import load_dotenv
load_dotenv() #loading all the environmentv variables

import streamlit as st
import base64
import os 
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model=genai.GenerativeModel("gemini-pro-vision")
# Function to load gemini pro model and get response

def get_gemini_response(input, pdf_content, prompt):
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text


def input_pdf_setup(uploaded_file):
    # CONVERTS PDF TO IMAGE
    if uploaded_file is not None:
        images=pdf2image.convert_from_bytes(uploaded_file.read())
        first_page=images[0]
        img_byte_arr=io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr=img_byte_arr.getvalue()
        
        pdf_parts =[{"mime_type":"image/jpeg","data":base64.b64encode(img_byte_arr).decode()}]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Automatic Resume Analyzer")
st.header("Automatic Resume Analyzer")
input_text=st.text_area("Job Description: Write the job description below ",key="input")
uploaded_file=st.file_uploader("Upload your resume in PDF format",type=['pdf'])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1=st.button("Tell me about the resume")

submit2=st.button("How can the profile be improvised?")

submit3=st.button("Percentage match")


input_prompt1='''
 You are an experienced HR with Tech experience in any one of the field of Data Science or
 Full Stack web development or Big Data Engineering or DEVOPS or Data Analyst 
 your task it review the provided resume against the job description for these profiles
 Share your brief professional evaluation on whether the candidates's profile aligns with the given job role.
'''

input_prompt2='''
 You are an experienced HR with Tech experience in any one of the field of Data Science or
 Full Stack web development or Big Data Engineering or DEVOPS or Data Analyst, your task it review
 the provided resume against the job description for these profiles
 Act as a critique of the resume and share a brief on what is lacking in the profile and what must be added to make the profile better.
'''

input_prompt3='''
 You are an experienced HR with Tech experience in any one of the field of Data Science or
 Full Stack web development or Big Data Engineering or DEVOPS or Data Analyst
 Give me the percentage match that the resume has with the given job description.
'''

if submit1:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("Here is the response:")
        st.write(response)
    else:
        st.write("Please upload the resume to get a summary of the resume.")

elif submit2:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("Here is the response:")
        st.write(response)
    else:
        st.write("Please upload the resume above to get to know about the improvisations.")

elif submit3:
    if uploaded_file is not None:
      pdf_content= input_pdf_setup(uploaded_file)
      response=get_gemini_response(input_prompt3,pdf_content,input_text)
      st.subheader("Here is the response:")
      st.write(response)
    else:
      st.write("Please upload the resume above to get the percentage match.")