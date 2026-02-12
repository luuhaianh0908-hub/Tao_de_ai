import streamlit as st
import google.generativeai as genai
from docx import Document
from io import BytesIO

# --- CẤU HÌNH ---
# Bạn dán mã API của bạn vào giữa hai dấu ngoặc kép ở dưới nhé
MY_API_KEY = "AIzaSyC_TED5HV8YSeu7_2K3pQRwRUubzyBZFDI"

st.set_page_config(page_title="Máy Tạo Đề AI", layout="centered")
st.title("📝 TẠO ĐỀ THI THÔNG MINH")

# Tự động kết nối bằng mã đã dán sẵn
if MY_API_KEY and MY_API_KEY != "AIzaSyC_TED5HV8YSeu7_2K3pQRwRUubzyBZFDI":
    try:
        genai.configure(api_key=MY_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        mon = st.text_input("1. Tên môn học:", "Lịch sử")
        noidung = st.text_area("2. Dán nội dung bài học vào đây:", height=250)
        
        if st.button("🔥 BẮT ĐẦU TẠO ĐỀ"):
            if not noidung:
                st.warning("Bạn chưa dán nội dung bài học kìa!")
            else:
                with st.spinner("AI đang soạn đề, đợi tí nhé..."):
                    res = model.generate_content(f"Tạo 10 câu trắc nghiệm từ: {noidung}")
                    st.markdown(res.text)
                    
                    # Tạo file Word tự động
                    doc = Document()
                    doc.add_heading(f'ĐỀ THI MÔN: {mon.upper()}', 0)
                    doc.add_paragraph(res.text)
                    bio = BytesIO()
                    doc.save(bio)
                    st.download_button("📥 TẢI FILE WORD VỀ MÁY", bio.getvalue(), f"De_{mon}.docx")
    except Exception as e:
        st.error(f"Có lỗi rồi: {e}")
else:
    st.error("Bạn chưa dán mã API vào code rồi! Hãy quay lại GitHub để dán nhé.")
  
