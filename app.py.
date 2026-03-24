import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="UN Championship: Gateway to Glory", page_icon="⚽", layout="centered")

# 2. Custom CSS for "The Look" (Dark Mode + Neon)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Style the table for a pro look */
    .stTable {
        background-color: #1a1c24;
        border: 2px solid #00f2ff;
        border-radius: 10px;
    }
    h1, h2, h3 {
        color: #00f2ff !important;
        text-shadow: 2px 2px 5px #000;
        font-family: 'Arial Black', sans-serif;
    }
    .stMetric {
        background-color: #161b22;
        padding: 10px;
        border-radius: 5px;
        border-left: 5px solid #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Branding Header
st.title("🏆 UN CHAMPIONSHIP")
st.subheader("Season One: Gateway to Glory")

# Placeholder for your Logo and "The Ball"
# Replace these URLs with your actual image links later!
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/150/00f2ff/000000?text=UN+LOGO", caption="UN Official Logo")
with col2:
    st.write("### The Official Match Ball")
    st.image("https://via.placeholder.com/300/161b22/ffffff?text=GATEWAY+BALL", caption="Showcasing the Match Ball")

st.divider()

# 4. Live Leaderboard Data
data = {
    "Rank": [1, 2, 3, 4],
    "Player": ["Kenan Uzunoglu", "Jay Jay Pereira", "Jason Davids", "Gordyntjie"],
    "Striker (2pt)": [0, 0, 0, 0],
    "Bonus (3pt)": [0, 0, 0, 0],
    "UN Wins": [0, 0, 0, 0],
    "Total Score": [0, 0, 0, 0]
}

df = pd.DataFrame(data)

# Sort by Rank/Score
df = df.sort_values(by="Rank")

# Display Leaderboard
st.write("### 📊 Current Standings")
st.table(df)

# 5. Quick Rules Reference
with st.expander("📖 The Rules of the Game"):
    st.write("""
    * **Striker:** 2 Points (Ball through window)
    * **Bonus:** 3 Points (Special Skill Shot)
    * **UN:** Immediate Match Win
    """)

st.info("💡 Pro Tip: Send this link to the group chat so everyone can see their ranking in real-time!")
