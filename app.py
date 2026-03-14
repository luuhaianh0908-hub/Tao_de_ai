import streamlit as st
import google.generativeai as genai

st.title("📚 Tạo đề thi AI")

# lấy API key từ secrets
api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

mon_hoc = st.text_input("Tên môn học")
so_cau = st.slider("Số câu hỏi", 5, 20, 10)
noi_dung = st.text_area("Nội dung bài học")

if st.button("🚀 Tạo đề thi"):

    if not mon_hoc or not noi_dung:
        st.warning("Hãy nhập đầy đủ thông tin")
    else:

        prompt = f"""
Tạo {so_cau} câu hỏi trắc nghiệm môn {mon_hoc}
từ nội dung sau:

{noi_dung}

Mỗi câu có 4 đáp án A B C D.
Cuối đề ghi đáp án.
"""

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            st.subheader("📄 Đề thi")
            st.write(response.text)

        except Exception as e:
            st.error(e)