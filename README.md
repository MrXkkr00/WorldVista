# 🌍 WorldVista – Dunyo Shaharlari Sayohat Saytii

Streamlit bilan qurilgan to'liq funksional sayohat kashfiyot platformasi.
AI maslahatchi (Claude), 20+ shahar, filter, sevimlilar — barchasi bir joyda.

---

## 🖼️ Funksiyalar

| Bo'lim | Tavsif |
|--------|--------|
| 🏠 Asosiy | Trend shaharlar, kontinent bo'yicha tanlash, tasodifiy tavsiya |
| 🗺️ Shaharlar | Barcha shaharlar, qidiruv, 4 ta filter (kontinent, byudjet, fasl) |
| 🏙️ Shahar Detayli | Ko'rishga arzidigan joylar, taomlar, amaliy maslahatlar, viza ma'lumoti |
| ❤️ Sevimlilar | Yoqtirgan shaharlaringizni saqlash |
| 🤖 AI Maslahat | Claude AI bilan o'zbek tilida shaxsiy sayohat maslahati |

---

## 🚀 GitHub va Streamlit Cloud'da Ishlatish

### 1-Qadam: GitHub'ga Yuklash

```bash
# GitHub'da yangi repo yarating (masalan: worldvista-travel)
# Keyin quyidagi buyruqlarni bajaring:

git init
git add .
git commit -m "🌍 WorldVista initial commit"
git branch -M main
git remote add origin https://github.com/SIZNING_USERNAMINGIZ/worldvista-travel.git
git push -u origin main
```

### 2-Qadam: Streamlit Cloud'da Deploy qilish

1. **[share.streamlit.io](https://share.streamlit.io)** ga kiring
2. Google yoki GitHub akkauntingiz bilan kirng
3. **"New app"** tugmasini bosing
4. Quyidagilarni kiriting:
   - **Repository:** `SIZNING_USERNAMINGIZ/worldvista-travel`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. **"Advanced settings"** → **Secrets** bo'limiga kiring
6. Quyidagini qo'shing:

```toml
ANTHROPIC_API_KEY = "sk-ant-SIZNING_KALITINGIZ"
```

7. **"Deploy!"** tugmasini bosing ✅

### 3-Qadam: Anthropic API Kalitini Olish

1. [console.anthropic.com](https://console.anthropic.com) ga kiring
2. **API Keys** → **Create Key**
3. Kalitni nusxa oling va Streamlit Secrets'ga qo'ying

---

## 📁 Fayl Tuzilmasi

```
worldvista-travel/
├── app.py                    # Asosiy Streamlit ilovasi
├── requirements.txt          # Python kutubxonalari
├── .streamlit/
│   └── config.toml          # Streamlit konfiguratsiyasi
├── assets/
│   └── style.css            # Barcha CSS uslublari
├── data/
│   ├── __init__.py
│   └── cities.py            # 20+ shahar ma'lumotlari
└── components/
    ├── __init__.py
    ├── city_card.py         # Shahar kartochkasi
    ├── filters.py           # Qidiruv va filter
    ├── hero.py              # Bosh sahifa hero
    └── ai_chat.py           # AI suhbat
```

---

## 🛠️ Lokal Ishga Tushirish (ixtiyoriy)

```bash
# Python 3.9+ kerak
pip install -r requirements.txt

# API kalitini o'rnating
export ANTHROPIC_API_KEY="sk-ant-SIZNING_KALITINGIZ"

# Streamlit ni ishga tushiring
streamlit run app.py
```

Brauzerda: `http://localhost:8501`

---

## ➕ Yangi Shahar Qo'shish

`data/cities.py` faylida yangi shahar qo'shing:

```python
{
    "name": "Shahar Nomi",
    "country": "Mamlakat",
    "continent": "Osiyo",          # Osiyo / Yevropa / Amerika / Afrika / Avstraliya
    "emoji": "🏙️",
    "description": "Tavsif...",
    "rating": 8.5,                 # 1-10
    "budget": "O'rtacha",          # Arzon / O'rtacha / Qimmat
    "climate": "Mo'tadil",
    "language": "...",
    "currency": "...",
    "visa": "...",
    "duration": "3-5 kun",
    "best_seasons": ["Bahor", "Kuz"],
    "color1": "#1a1a2e",           # Karta gradient rangi 1
    "color2": "#e94560",           # Karta gradient rangi 2
    "trending": True,              # True = bosh sahifada ko'rinadi
    "attractions": [
        {"name": "Joy", "desc": "Tavsif", "icon": "🏛️"},
    ],
    "foods": ["🍜 Taom 1", "🍛 Taom 2"],
    "tips": ["Maslahat 1", "Maslahat 2"],
}
```

---

## 📜 Litsenziya

MIT License – Erkin foydalaning va o'zgartiring.
