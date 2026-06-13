import streamlit as st
import json
import random
from data.cities import CITIES_DATA
from components.city_card import render_city_card
from components.filters import render_filters
from components.hero import render_hero
from components.ai_chat import render_ai_chat

# ─── Page Config ────────────────────────────────────────────────
st.set_page_config(
    page_title="WorldVista – Dunyo Shaharlari",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Load CSS ────────────────────────────────────────────────────
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ─── Session State ───────────────────────────────────────────────
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "selected_city" not in st.session_state:
    st.session_state.selected_city = None
if "search_query" not in st.session_state:
    st.session_state.search_query = ""
if "selected_continent" not in st.session_state:
    st.session_state.selected_continent = "Barchasi"
if "selected_budget" not in st.session_state:
    st.session_state.selected_budget = "Barchasi"
if "selected_season" not in st.session_state:
    st.session_state.selected_season = "Barchasi"

# ─── Navigation ──────────────────────────────────────────────────
def navigate(page, city=None):
    st.session_state.current_page = page
    if city:
        st.session_state.selected_city = city

# ─── NAV BAR ─────────────────────────────────────────────────────
st.markdown("""
<div class="navbar">
  <div class="nav-logo">🌍 WorldVista</div>
  <div class="nav-tagline">Dunyoni kashf eting</div>
</div>
""", unsafe_allow_html=True)

col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([1,1,1,1])
with col_nav1:
    if st.button("🏠 Asosiy", use_container_width=True,
                 type="primary" if st.session_state.current_page == "home" else "secondary"):
        navigate("home")
with col_nav2:
    if st.button("🗺️ Shaharlar", use_container_width=True,
                 type="primary" if st.session_state.current_page == "cities" else "secondary"):
        navigate("cities")
with col_nav3:
    fav_count = len(st.session_state.favorites)
    if st.button(f"❤️ Sevimlilar ({fav_count})", use_container_width=True,
                 type="primary" if st.session_state.current_page == "favorites" else "secondary"):
        navigate("favorites")
with col_nav4:
    if st.button("🤖 AI Maslahat", use_container_width=True,
                 type="primary" if st.session_state.current_page == "ai" else "secondary"):
        navigate("ai")

st.markdown("<hr class='nav-divider'>", unsafe_allow_html=True)

# ─── PAGES ───────────────────────────────────────────────────────

# HOME PAGE
if st.session_state.current_page == "home":
    render_hero()

    st.markdown("<div class='section-title'>🔥 Trending Shaharlar</div>", unsafe_allow_html=True)
    trending = [c for c in CITIES_DATA if c.get("trending")][:6]
    cols = st.columns(3)
    for i, city in enumerate(trending):
        with cols[i % 3]:
            render_city_card(city, navigate)

    st.markdown("<div class='section-title'>🌏 Kontinentlar bo'yicha</div>", unsafe_allow_html=True)
    continents = ["Osiyo", "Yevropa", "Amerika", "Afrika", "Avstraliya"]
    cont_cols = st.columns(5)
    for i, cont in enumerate(continents):
        with cont_cols[i]:
            emoji_map = {"Osiyo":"🌏","Yevropa":"🏰","Amerika":"🗽","Afrika":"🦁","Avstraliya":"🦘"}
            count = len([c for c in CITIES_DATA if c["continent"] == cont])
            if st.button(f"{emoji_map[cont]}\n{cont}\n({count} shahar)",
                        use_container_width=True, key=f"cont_{cont}"):
                st.session_state.selected_continent = cont
                navigate("cities")

    st.markdown("<div class='section-title'>💡 Tasodifiy Tavsiya</div>", unsafe_allow_html=True)
    if st.button("🎲 Yangi shahar kashf et!", use_container_width=True):
        random_city = random.choice(CITIES_DATA)
        navigate("detail", random_city)
        st.rerun()

# CITIES PAGE
elif st.session_state.current_page == "cities":
    st.markdown("<div class='page-title'>🗺️ Barcha Shaharlar</div>", unsafe_allow_html=True)

    # Filters
    search, continent, budget, season = render_filters()

    # Filter logic
    filtered = CITIES_DATA
    if search:
        filtered = [c for c in filtered if
                   search.lower() in c["name"].lower() or
                   search.lower() in c["country"].lower() or
                   search.lower() in c["description"].lower()]
    if continent != "Barchasi":
        filtered = [c for c in filtered if c["continent"] == continent]
    if budget != "Barchasi":
        filtered = [c for c in filtered if c["budget"] == budget]
    if season != "Barchasi":
        filtered = [c for c in filtered if season in c.get("best_seasons", [])]

    st.markdown(f"<div class='result-count'>📍 {len(filtered)} shahar topildi</div>", unsafe_allow_html=True)

    if not filtered:
        st.markdown("""
        <div class='no-results'>
            <div style='font-size:3rem'>🔍</div>
            <div>Hech narsa topilmadi. Filtrlarni o'zgartiring.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        cols = st.columns(3)
        for i, city in enumerate(filtered):
            with cols[i % 3]:
                render_city_card(city, navigate)

# DETAIL PAGE
elif st.session_state.current_page == "detail" and st.session_state.selected_city:
    city = st.session_state.selected_city

    if st.button("← Orqaga"):
        navigate("cities")
        st.rerun()

    # Hero section
    st.markdown(f"""
    <div class='detail-hero' style='background: linear-gradient(135deg, {city.get("color1","#1a1a2e")} 0%, {city.get("color2","#16213e")} 100%)'>
        <div class='detail-hero-content'>
            <div class='detail-emoji'>{city["emoji"]}</div>
            <h1 class='detail-title'>{city["name"]}</h1>
            <p class='detail-subtitle'>{city["country"]} · {city["continent"]}</p>
            <div class='detail-badges'>
                <span class='badge badge-budget-{city["budget"].lower()}'>{city["budget"]}</span>
                <span class='badge badge-safety'>⭐ {city["rating"]}/10</span>
                <span class='badge badge-climate'>🌡️ {city.get("climate","Yaxshi")}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"<div class='detail-description'>{city['description']}</div>", unsafe_allow_html=True)

        st.markdown("<div class='detail-section-title'>🏛️ Ko'rishga arzidigan joylar</div>", unsafe_allow_html=True)
        for place in city.get("attractions", []):
            st.markdown(f"""
            <div class='attraction-item'>
                <span class='attraction-icon'>{place["icon"]}</span>
                <div>
                    <div class='attraction-name'>{place["name"]}</div>
                    <div class='attraction-desc'>{place["desc"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div class='detail-section-title'>🍽️ Milliy Taomlar</div>", unsafe_allow_html=True)
        food_cols = st.columns(3)
        for i, food in enumerate(city.get("foods", [])):
            with food_cols[i % 3]:
                st.markdown(f"<div class='food-chip'>{food}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='info-card'>", unsafe_allow_html=True)
        info_items = [
            ("💰", "Byudjet", city["budget"]),
            ("📅", "Eng yaxshi fasl", ", ".join(city.get("best_seasons", []))),
            ("🌡️", "Iqlim", city.get("climate", "Mo'tadil")),
            ("🗣️", "Til", city.get("language", "Ingliz")),
            ("💱", "Valyuta", city.get("currency", "USD")),
            ("✈️", "Viza", city.get("visa", "Kerak")),
            ("⏱️", "Tavsiya etilgan muddat", city.get("duration", "3-5 kun")),
        ]
        for icon, label, value in info_items:
            st.markdown(f"""
            <div class='info-row'>
                <span class='info-icon'>{icon}</span>
                <div>
                    <div class='info-label'>{label}</div>
                    <div class='info-value'>{value}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Favorite button
        is_fav = city["name"] in [f["name"] for f in st.session_state.favorites]
        fav_label = "❤️ Sevimlilardan chiqar" if is_fav else "🤍 Sevimlilarga qo'sh"
        if st.button(fav_label, use_container_width=True):
            if is_fav:
                st.session_state.favorites = [f for f in st.session_state.favorites if f["name"] != city["name"]]
                st.toast(f"{city['name']} sevimlilardan olib tashlandi", icon="💔")
            else:
                st.session_state.favorites.append(city)
                st.toast(f"{city['name']} sevimlilarga qo'shildi!", icon="❤️")
            st.rerun()

        st.markdown("<div class='tips-card'>", unsafe_allow_html=True)
        st.markdown("<div class='tips-title'>💡 Foydali Maslahatlar</div>", unsafe_allow_html=True)
        for tip in city.get("tips", []):
            st.markdown(f"<div class='tip-item'>• {tip}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# FAVORITES PAGE
elif st.session_state.current_page == "favorites":
    st.markdown("<div class='page-title'>❤️ Sevimli Shaharlarim</div>", unsafe_allow_html=True)

    if not st.session_state.favorites:
        st.markdown("""
        <div class='empty-favorites'>
            <div style='font-size:4rem'>💔</div>
            <div style='font-size:1.2rem; margin-top:1rem'>Hali hech qanday shahar qo'shilmagan</div>
            <div style='color:#888; margin-top:0.5rem'>Shaharlar sahifasiga o'tib, yoqtirganlaringizni qo'shing</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🗺️ Shaharlarga o'tish", use_container_width=True):
            navigate("cities")
            st.rerun()
    else:
        st.markdown(f"<div class='result-count'>❤️ {len(st.session_state.favorites)} ta sevimli shahar</div>", unsafe_allow_html=True)
        cols = st.columns(3)
        for i, city in enumerate(st.session_state.favorites):
            with cols[i % 3]:
                render_city_card(city, navigate)

        if st.button("🗑️ Barchasini o'chirish", type="secondary"):
            st.session_state.favorites = []
            st.rerun()

# AI PAGE
elif st.session_state.current_page == "ai":
    render_ai_chat()

# ─── Footer ──────────────────────────────────────────────────────
st.markdown("""
<div class='footer'>
    <div>🌍 WorldVista — Dunyoni kashf eting</div>
    <div style='font-size:0.8rem; color:#888; margin-top:0.3rem'>
        AI yordamida yaratilgan · Anthropic Claude bilan ishlaydi
    </div>
</div>
""", unsafe_allow_html=True)
