import streamlit as st


def render_filters():
    """Renders search and filter controls. Returns (search, continent, budget, season)."""
    with st.container():
        st.markdown("<div class='filter-bar'>", unsafe_allow_html=True)

        col1, col2, col3, col4 = st.columns([3, 2, 2, 2])

        with col1:
            search = st.text_input(
                "🔍 Shahar yoki mamlakat qidiring",
                value=st.session_state.get("search_query", ""),
                placeholder="Masalan: Tokio, Yaponiya, osiyoo...",
                key="search_input",
                label_visibility="collapsed",
            )
            st.session_state.search_query = search

        with col2:
            continent = st.selectbox(
                "Kontinent",
                ["Barchasi", "Osiyo", "Yevropa", "Amerika", "Afrika", "Avstraliya"],
                index=["Barchasi", "Osiyo", "Yevropa", "Amerika", "Afrika", "Avstraliya"].index(
                    st.session_state.get("selected_continent", "Barchasi")
                ),
                key="continent_select",
                label_visibility="collapsed",
            )
            st.session_state.selected_continent = continent

        with col3:
            budget = st.selectbox(
                "Byudjet",
                ["Barchasi", "Arzon", "O'rtacha", "Qimmat"],
                index=["Barchasi", "Arzon", "O'rtacha", "Qimmat"].index(
                    st.session_state.get("selected_budget", "Barchasi")
                ),
                key="budget_select",
                label_visibility="collapsed",
            )
            st.session_state.selected_budget = budget

        with col4:
            season = st.selectbox(
                "Fasl",
                ["Barchasi", "Bahor", "Yoz", "Kuz", "Qish"],
                index=["Barchasi", "Bahor", "Yoz", "Kuz", "Qish"].index(
                    st.session_state.get("selected_season", "Barchasi")
                ),
                key="season_select",
                label_visibility="collapsed",
            )
            st.session_state.selected_season = season

        st.markdown("</div>", unsafe_allow_html=True)

    return search, continent, budget, season
