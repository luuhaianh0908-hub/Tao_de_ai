import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Tạo đề thi AI", page_icon="📚")

st.title("📚 Tạo đề thi tự động bằng AI")

# Lấy API key
api_key = st.secrets.get("API_KEY")

if not api_key:
    st.error("Chưa có API KEY. Hãy thêm vào secrets.")
    st.stop()

genai.configure(api_key=api_key)

# Nhập dữ liệu
mon_hoc = st.text_input("Tên môn học")

so_cau = st.slider(
    "Số câu hỏi",
    5,
    30,
    10
)

noi_dung = st.text_area(
    "Dán nội dung bài học vào đây",
    height=200
)

# Nút tạo đề
if st.button("🚀 Tạo đề thi"):

    if not mon_hoc or not noi_dung:
        st.warning("Hãy nhập đầy đủ thông tin.")
    else:

        prompt = f"""
Tạo đề kiểm tra môn {mon_hoc}

Nội dung bài học:
{noi_dung}

Yêu cầu:
- Tạo {so_cau} câu hỏi trắc nghiệm
- 4 đáp án A B C D
- Không giải thích
- Cuối đề ghi đáp án
"""

        try:

            model = genai.GenerativeModel("gemini-1.5-flash-latest")

            response = model.generate_content(prompt)

            st.subheader("📄 Đề thi được tạo")

            st.write(response.text)

            st.download_button(
                "📥 Tải đề thi",
                response.text,
                file_name="de_thi.txt"
            )

        except Exception as e:
            st.error(f"Lỗi: {e}")