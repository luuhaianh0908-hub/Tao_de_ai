import streamlit as st
import google.generativeai as genai

# --- CẤU HÌNH ---
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    
    # ĐÂY LÀ CÁCH ÉP V1 CHUẨN NHẤT:
    genai.configure(
        api_key=api_key,
        client_options={'api_version': 'v1'}
    )
    
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chưa cấu hình API Key!")
    st.stop()

# --- GIAO DIỆN ---
st.title("📝 MÁY TẠO ĐỀ")
mon = st.text_input("Tên môn học:")
noidung = st.text_area("Nội dung bài học:")

if st.button("🔥 TẠO ĐỀ"):
    try:
        # Gọi lệnh tạo nội dung (không thêm gì ở đây nữa để tránh lỗi)
        res = model.generate_content(f"Tạo đề thi môn {mon}: {noidung}")
        st.markdown(res.text)
    except Exception as e:
        st.error(f"Lỗi: {e}")
        
