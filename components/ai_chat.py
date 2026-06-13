import streamlit as st
import anthropic
import json
from data.cities import CITIES_DATA


def get_city_context():
    """Build a compact city context for the AI."""
    cities_summary = []
    for city in CITIES_DATA:
        cities_summary.append({
            "name": city["name"],
            "country": city["country"],
            "continent": city["continent"],
            "budget": city["budget"],
            "rating": city["rating"],
            "best_seasons": city.get("best_seasons", []),
            "climate": city.get("climate", ""),
            "visa": city.get("visa", ""),
        })
    return json.dumps(cities_summary, ensure_ascii=False)


def render_ai_chat():
    """Renders the AI travel advisor chat interface."""
    st.markdown("<div class='page-title'>🤖 AI Sayohat Maslahatchisi</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='ai-intro'>
        <div class='ai-avatar'>🤖</div>
        <div class='ai-intro-text'>
            <div class='ai-intro-title'>Salom! Men sizning shaxsiy sayohat maslahatchingizman.</div>
            <div class='ai-intro-sub'>Byudjet, fasl, mamlakat yoki qiziqishlaringiz asosida eng mos shaharni tavsiya qilaman.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Quick prompts
    st.markdown("<div class='quick-prompts-title'>💡 Tez savollar:</div>", unsafe_allow_html=True)
    quick_cols = st.columns(2)
    quick_prompts = [
        "Arzon byudjet bilan Osiyoga sayohat qilmoqchiman",
        "Yozda Yevropada qayerga borish kerak?",
        "Oila bilan bolali sayohat uchun eng yaxshi shahar?",
        "Romantik juft sayohat uchun tavsiya bering",
        "Trekking va tog' sevuvchilar uchun qayer mos?",
        "Birinchi marta xorijga chiqdim, qayerdan boshlash kerak?",
    ]
    for i, prompt in enumerate(quick_prompts):
        with quick_cols[i % 2]:
            if st.button(f"💬 {prompt}", key=f"quick_{i}", use_container_width=True):
                if "chat_messages" not in st.session_state:
                    st.session_state.chat_messages = []
                st.session_state.chat_messages.append({"role": "user", "content": prompt})
                st.rerun()

    st.markdown("<hr style='margin: 1rem 0'>", unsafe_allow_html=True)

    # Chat history
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Display messages
    for msg in st.session_state.chat_messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class='chat-user-msg'>
                <div class='chat-msg-content'>{msg["content"]}</div>
                <div class='chat-user-avatar'>👤</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='chat-ai-msg'>
                <div class='chat-ai-avatar'>🤖</div>
                <div class='chat-msg-content'>{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)

    # Input
    col_input, col_btn = st.columns([5, 1])
    with col_input:
        user_input = st.text_input(
            "Savol yozing...",
            key="chat_input",
            placeholder="Masalan: Bahorgi sayohat uchun qaysi shahar mos?",
            label_visibility="collapsed",
        )
    with col_btn:
        send_clicked = st.button("📤 Yuborish", use_container_width=True, type="primary")

    if (send_clicked or user_input) and user_input:
        st.session_state.chat_messages.append({"role": "user", "content": user_input})

        # Call Anthropic API
        try:
            client = anthropic.Anthropic()
            city_context = get_city_context()

            system_prompt = f"""Sen WorldVista sayohat saytining AI maslahatchiisan. 
Foydalanuvchilarga dunyo shaharlari bo'yicha o'zbek tilida maslahat berasan.

Senda quyidagi shaharlar ma'lumotlari bor:
{city_context}

Qoidalar:
- Har doim o'zbek tilida javob ber
- Konkret shaharlar tavsiya qil (yuqoridagi ro'yxatdan)
- Byudjet, fasl, iqlim, viza talablarini hisobga ol
- Emoji'lardan foydalanib, jonli va qiziqarli javob yoz
- Har bir tavsiyada qisqacha sababini tushuntir
- Maksimal 3-4 ta shahar tavsiya qil
- Oxirida qo'shimcha savol berishni taklif qil"""

            messages = []
            for msg in st.session_state.chat_messages:
                messages.append({"role": msg["role"], "content": msg["content"]})

            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                system=system_prompt,
                messages=messages,
            )

            ai_reply = response.content[0].text
            st.session_state.chat_messages.append({"role": "assistant", "content": ai_reply})

        except Exception as e:
            error_msg = f"⚠️ Xatolik yuz berdi: {str(e)}\n\nIltimos, ANTHROPIC_API_KEY ni tekshiring."
            st.session_state.chat_messages.append({"role": "assistant", "content": error_msg})

        st.rerun()

    # Clear chat
    if st.session_state.chat_messages:
        if st.button("🗑️ Suhbatni tozalash", type="secondary"):
            st.session_state.chat_messages = []
            st.rerun()
