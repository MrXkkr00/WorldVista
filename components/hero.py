import streamlit as st
import random
from data.cities import CITIES_DATA


def render_hero():
    """Renders the homepage hero section with animated stats."""
    total_cities = len(CITIES_DATA)
    continents = len(set(c["continent"] for c in CITIES_DATA))
    countries = len(set(c["country"] for c in CITIES_DATA))

    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-bg-text">TRAVEL</div>
        <div class="hero-content">
            <div class="hero-badge">✈️ Sayohat Kashfiyotchisi</div>
            <h1 class="hero-title">
                Dunyo Shaharlari<br>
                <span class="hero-title-accent">Sizni Kutmoqda</span>
            </h1>
            <p class="hero-subtitle">
                {total_cities}+ shahar, {continents} kontinent, {countries} mamlakat —<br>
                Orzuingizdagi sayohatni rejalashtiring
            </p>
            <div class="hero-stats">
                <div class="hero-stat">
                    <div class="hero-stat-num">{total_cities}+</div>
                    <div class="hero-stat-label">Shahar</div>
                </div>
                <div class="hero-stat-divider"></div>
                <div class="hero-stat">
                    <div class="hero-stat-num">{continents}</div>
                    <div class="hero-stat-label">Kontinent</div>
                </div>
                <div class="hero-stat-divider"></div>
                <div class="hero-stat">
                    <div class="hero-stat-num">{countries}</div>
                    <div class="hero-stat-label">Mamlakat</div>
                </div>
                <div class="hero-stat-divider"></div>
                <div class="hero-stat">
                    <div class="hero-stat-num">🤖</div>
                    <div class="hero-stat-label">AI Maslahat</div>
                </div>
            </div>
        </div>
        <div class="hero-cities-float">
            {"".join([f'<div class="float-city">{c["emoji"]} {c["name"]}</div>' for c in random.sample(CITIES_DATA, min(8, len(CITIES_DATA)))])}
        </div>
    </div>
    """, unsafe_allow_html=True)
