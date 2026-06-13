import streamlit as st


def render_city_card(city: dict, navigate_fn):
    """Renders a city card with click-to-detail navigation."""
    is_fav = city["name"] in [f["name"] for f in st.session_state.get("favorites", [])]
    budget_colors = {
        "Arzon": "#27ae60",
        "O'rtacha": "#f39c12",
        "Qimmat": "#e74c3c",
    }
    budget_color = budget_colors.get(city["budget"], "#888")

    st.markdown(f"""
    <div class='city-card'>
        <div class='city-card-header' style='background: linear-gradient(135deg, {city.get("color1","#1a1a2e")} 0%, {city.get("color2","#16213e")} 100%)'>
            <div class='city-emoji'>{city["emoji"]}</div>
            <div class='city-header-info'>
                <div class='city-name'>{city["name"]}</div>
                <div class='city-country'>{city["country"]} · {city["continent"]}</div>
            </div>
            {'<div class="fav-heart">❤️</div>' if is_fav else ''}
        </div>
        <div class='city-card-body'>
            <p class='city-desc'>{city["description"][:120]}...</p>
            <div class='city-meta'>
                <span class='meta-badge' style='background:{budget_color}22; color:{budget_color}; border:1px solid {budget_color}'>
                    💰 {city["budget"]}
                </span>
                <span class='meta-badge meta-rating'>
                    ⭐ {city["rating"]}/10
                </span>
                <span class='meta-badge meta-season'>
                    📅 {city.get("best_seasons", ["Yil bo'yi"])[0]}
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"Ko'rish →", key=f"btn_{city['name']}_{id(city)}", use_container_width=True):
        navigate_fn("detail", city)
        st.rerun()
