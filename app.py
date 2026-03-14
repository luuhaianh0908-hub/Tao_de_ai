import streamlit as st
import google.generativeai as genai

# Kiểm tra Key trong Secrets
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    # Cách cấu hình v1 tối giản nhất để không bao giờ lỗi
    genai.configure(api_key=api_key)
    # Ép dùng đúng model 1.5 flash
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Chưa cấu hình API Key trong Secrets!")
    st.stop()

st.title("📝 MÁY TẠO ĐỀ THI")

mon = st.text_input("1. Tên môn học:")
noidung = st.text_area("2. Nội dung bài học:", height=200)

if st.button("🔥 BẮT ĐẦU TẠO ĐỀ"):
    if not noidung:
        st.warning("Vui lòng dán nội dung bài học!")
    else:
        try:
            with st.spinner("AI đang soạn đề..."):
                # Dùng prompt đơn giản để AI tự hiểu
                prompt = f"Tạo một đề thi trắc nghiệm môn {mon} dựa trên nội dung sau: {noidung}"
                response = model.generate_content(prompt)
                st.markdown("### ĐỀ THI GỢI Ý:")
                st.write(response.text)
        except Exception as e:
            st.error(f"Lỗi: {e}")
            
