import streamlit as st

# 페이지 설정: 넓은 레이아웃
st.set_page_config(layout="wide")

# 배경색을 노란색으로 설정
st.markdown(
    """
    <style>
    .main {
        background: yellow;
        background-attachment: fixed;
        padding: 2rem;
        color: black;
    }
    .main h1, .main h2, .main h3, .main p {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 페이지 제목
st.title("자기소개 페이지")

# 말하는 식의 자기소개
st.write("안녕하세요, 반갑습니다! 😊 저는 최해솔이라고 합니다. 20살의 대학생이에요. 🎓")
st.write("저는 청주교육대학교 실과교육과에 재학 중입니다. 실과교육과에서는 다양한 실습과 교육 방법을 배우고 있어요. 📚")
st.write("저는 손으로 만드는 것을 정말 좋아해요. ✂️ 공예, 요리, 그림 등 직접 만드는 활동이 제 취미입니다. 🎨")
st.write("저의 꿈은 멋진 교사가 되는 것입니다. 👩‍🏫 아이들을 가르치고, 그들의 미래를 밝게 이끌어주는 선생님이 되고 싶어요. 🌟")
