import streamlit as st
import google.generativeai as genai
from docx import Document
from io import BytesIO

st.set_page_config(page_title="Tạo Đề AI", layout="centered")
st.title("📝 ỨNG DỤNG TẠO ĐỀ THI THÔNG MINH ")

api_key = st.text_input("1. Dán API Key (...ZFDI) vào đây:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    mon = st.text_input("2. Tên môn học:", "Toán")
    noidung = st.text_area("3. Dán nội dung bài học vào đây:", height=250)
    
    if st.button("🔥 BẮT ĐẦU TẠO ĐỀ"):
        if noidung:
            with st.spinner("AI đang soạn bài..."):
                res = model.generate_content(f"Tạo 10 câu trắc nghiệm từ: {noidung}")
                st.markdown(res.text)
                doc = Document()
                doc.add_heading(f'ĐỀ THI: {mon.upper()}', 0)
                doc.add_paragraph(res.text)
                bio = BytesIO()
                doc.save(bio)
                st.download_button("📥 TẢI FILE WORD", bio.getvalue(), f"{mon}.docx")
              
