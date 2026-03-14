import streamlit as st
import google.generativeai as genai

st.title("📚 Tạo đề thi AI")

# lấy API key
genai.configure(api_key=st.secrets["API_KEY"])

mon_hoc = st.text_input("Tên môn học")
so_cau = st.slider("Số câu hỏi", 5, 20, 10)
noi_dung = st.text_area("Nội dung bài học")

if st.button("Tạo đề thi"):

    if not mon_hoc or not noi_dung:
        st.warning("Nhập đủ thông tin")
    else:

        prompt = f"""
Tạo {so_cau} câu hỏi trắc nghiệm môn {mon_hoc}

Nội dung:
{noi_dung}

Yêu cầu:
- mỗi câu có 4 đáp án A B C D
- cuối đề ghi đáp án
"""

        try:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)

            st.write(response.text)

        except Exception as e:
            st.error(e)