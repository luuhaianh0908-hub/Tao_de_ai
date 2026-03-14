import streamlit as st
import google.generativeai as genai
from docx import Document
from io import BytesIO

# --- CẤU HÌNH ---
if "GEMINI_API_KEY" in st.secrets:
    MY_API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=MY_API_KEY)
    model = genai.GenerativeModel(
    model_name='gemini-1.5-flash'
    )
    
else:
    st.error("Chưa cấu hình API Key trong phần Secrets của Streamlit!")
    st.stop()

# --- GIAO DIỆN (Tất cả dòng dưới đây phải sát lề trái, không có dấu cách ở đầu) ---
st.set_page_config(page_title="Máy Tạo Đề")
st.title("📝 TẠO ĐỀ THI THÔNG MINH")

mon = st.text_input("1. Tên môn học:")
noidung = st.text_area("2. Dán nội dung bài học vào đây:", height=200)

if st.button("🔥 BẮT ĐẦU TẠO ĐỀ"):
    if not noidung:
        st.warning("Bạn chưa nhập nội dung!")
    else:
        try:
            with st.spinner("AI đang tạo đề..."):
                prompt = f"Tạo đề thi trắc nghiệm môn {mon} từ nội dung: {noidung}"
                res = model.generate_content(prompt, request_options={"api_version": "v1"})
                st.markdown(res.text)
        except Exception as e:
            st.error(f"Lỗi: {e}")
            
