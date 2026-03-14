import streamlit as st
import google.generativeai as genai

# 1. Lấy API Key từ Secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    # Ép dùng đúng tên model chính thức
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Lỗi: Chưa dán API Key vào mục Secrets!")
    st.stop()

# 2. Giao diện đơn giản
st.title("📝 MÁY TẠO ĐỀ THI")

mon = st.text_input("Tên môn học:")
noidung = st.text_area("Nội dung bài học:", height=200)

if st.button("BẮT ĐẦU TẠO ĐỀ"):
    if not noidung:
        st.warning("Vui lòng nhập nội dung!")
    else:
        try:
            with st.spinner("Đang xử lý..."):
                # Gửi yêu cầu đơn giản
                response = model.generate_content(f"Tạo 5 câu hỏi trắc nghiệm môn {mon}: {noidung}")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Lỗi hệ thống: {e}")
            
