import streamlit as st
import random
import time

# 1. ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Wait for it...", page_icon="⏳")

# 2. CSS ตกแต่ง (เพิ่มความละมุน)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .text-white {
        color: white !important;
        text-align: center;
        font-family: 'Kanit', sans-serif;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ควบคุมสถานะ
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'

# --- เริ่มการทำงาน ---

if st.session_state.stage == 'intro':
    st.markdown("<h1 class='text-white'>มีคนฝากข้อความมาให้เธอ... ✉️</h1>", unsafe_allow_html=True)
    st.write(" ")
    if st.button("เปิดอ่านข้อความ"):
        st.session_state.stage = 'loading'
        st.rerun()

elif st.session_state.stage == 'loading':
    st.markdown("<h2 class='text-white'>กำลังดึงข้อมูลจากหัวใจ...</h2>", unsafe_allow_html=True)

    # ลูกเล่นที่ 1: Progress Bar ดึงเชง
    progress_bar = st.progress(0)
    status_text = st.empty()

    steps = [
        "กำลังหาคำพูด...",
        "รวบรวมความกล้า 20%...",
        "เขินอยู่ แป๊บนึงนะ 50%...",
        "ใกล้ความจริงแล้ว... 80%...",
        "เตรียมตัวนะ! 100%"
    ]

    for i, step in enumerate(steps):
        status_text.markdown(f"<p class='text-white'>{step}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) * 20)
        time.sleep(1.5)  # ยิ่งใส่ตัวเลขเยอะ ยิ่งจบช้า

    st.session_state.stage = 'confess'
    st.rerun()

elif st.session_state.stage == 'confess':
    # ลูกเล่นที่ 2: Typewriter Effect (ข้อความค่อยๆ ขึ้น)
    st.markdown("<h1 class='text-white'>ความในใจคือ...</h1>", unsafe_allow_html=True)

    message_placeholder = st.empty()
    full_message = "จริงๆ แล้ว... เราชอบเธอมาตั้งนานแล้วนะเว้ยยย ❤️"
    typed_message = ""

    for char in full_message:
        typed_message += char
        message_placeholder.markdown(f"<h2 class='text-white'>{typed_message}</h2>", unsafe_allow_html=True)
        time.sleep(0.1)  # ความเร็วในการพิมพ์

    time.sleep(1)  # หยุดรอให้ซึ้งแป๊บนึง
    st.balloons()

    # สุ่มประโยคปิดท้าย
    st.markdown("---")
    st.markdown("<p class='text-white'>สารภาพแล้วนะ... โล่งอกชะมัด 😳</p>", unsafe_allow_html=True)

    if st.button("อ่านอีกรอบไหม?"):
        st.session_state.stage = 'intro'
        st.rerun()