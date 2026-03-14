import streamlit as st
import google.generativeai as genai

# --- CẤU HÌNH API ---
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Khai báo model đơn giản nhất, thư viện 0.8.3 sẽ tự chạy v1
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Lỗi: Chưa dán API Key vào mục Secrets!")
    st.stop()

# --- GIAO DIỆN ---
st.title("📝 MÁY TẠO ĐỀ THI")
mon = st.text_input("1. Tên môn học:")
noidung = st.text_area("2. Nội dung bài học:", height=200)

if st.button("🔥 BẮT ĐẦU TẠO ĐỀ"):
    if not noidung:
        st.warning("Bạn chưa nhập nội dung!")
    else:
        try:
            with st.spinner("AI đang soạn đề..."):
                # Dòng lệnh tạo nội dung chuẩn nhất hiện nay
                response = model.generate_content(f"Tạo đề thi trắc nghiệm môn {mon}: {noidung}")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}")
        
