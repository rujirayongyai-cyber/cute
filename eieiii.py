import streamlit as st
import random

# ตั้งค่าหน้าเว็บให้ดูน่ารัก
st.set_page_config(page_title="มีเรื่องจะสารภาพ...", page_icon="😳")

# ตกแต่ง UI ด้วย CSS
st.markdown("""
    <style>
    .main {
        background: linear-gradient(160deg, #fd1d1d 0%, #fcb045 100%);
    }
    .text-white {
        color: white !important;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background-color: #ffffff;
        color: #ff4b4b;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# ใช้ session_state เพื่อคุมการเปลี่ยนหน้า
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if not st.session_state.clicked:
    st.markdown("<h1 class='text-white'>เฮ้ยเธอ... คือว่า 🫣</h1>", unsafe_allow_html=True)
    st.markdown("<p class='text-white'>เรามีความลับจะบอก เก็บไว้คนเดียวมานานละ</p>", unsafe_allow_html=True)

    st.write("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        if st.button("ความลับอะไร? บอกมาดิ๊ ✨"):
            st.session_state.clicked = True
            st.rerun()

    with col2:
        # ปุ่มนี้กดแล้วจะมีการแจ้งเตือนกวนๆ
        if st.button("ไม่อยากรู้ 🙄"):
            msgs = ["ไม่ได้นะ ต้องรู้ดิ!", "กดฝั่งซ้ายเดี๋ยวนี้!", "หยิ่งจัดดด", "แหมมมมม"]
            st.toast(random.choice(msgs))
else:
    # หน้าสารภาพรัก
    st.balloons()
    st.markdown("<h1 class='text-white'>เราชอบเธอนะเว้ยยย! ❤️</h1>", unsafe_allow_html=True)

    # สุ่มคำบอกชอบแบบเนียนๆ
    confessions = [
        "ไม่ได้อยากเป็นแค่คนรู้จักแล้วอ่ะ ชอบจริงๆ นะ 😳",
        "เนี่ย... ที่ทำหน้าเว็บมาก็เพื่อจะบอกคำเนี้ยแหละ 'ชอบนะ'",
        "ยิ้มบ่อยๆ นะ เราชอบดูเธอยิ้มที่สุดเลย",
        "ชอบมึงนะ... จบแยก! (เขินว่ะ 5555)",
        "ไม่รู้เริ่มตอนไหน แต่ตอนนี้ชอบไปแล้วทำไงได้อ่ะ 💘"
    ]

    st.markdown(f"<h2 class='text-white' style='margin-top: 50px;'>{random.choice(confessions)}</h2>",
                unsafe_allow_html=True)

    st.write("---")
    if st.button("เขินอ่ะดิ... กลับไปหน้าแรกไป๊!"):
        st.session_state.clicked = False
        st.rerun()