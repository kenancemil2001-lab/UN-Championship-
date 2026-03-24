import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="UN Championship", page_icon="⚽", layout="centered")

# 2. Advanced CSS to match your Logo
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0a0a0a;
        color: #ffffff;
    }
    
    /* Header & Title Colors (Neon Cyan) */
    h1, h2, h3 {
        color: #00f2ff !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 0px 0px 15px rgba(0, 242, 255, 0.5);
    }
    
    /* Table Styling */
    .stTable {
        background-color: #161616;
        border: 1px solid #00f2ff;
        border-radius: 10px;
    }
    
    /* Custom divider line color */
    hr {
        border-top: 2px solid #00f2ff;
    }

    /* Info Box Styling */
    .stAlert {
        background-color: #161616;
        border: 1px solid #444;
        color: #00f2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Branding Section
st.title("🏆 UN CHAMPIONSHIP")
st.subheader("Gateway to Glory: Season One")

# Add your logo here (Replace with your direct GitHub link)
st.image("PASTE_YOUR_DIRECT_LOGO_LINK_HERE", width=200)

st.divider()

# 4. Standings Data
data = {
    "Rank": [1, 2, 3, 4],
    "Player": ["Kenan Uzunoglu", "Jay Jay Pereira", "Jason Davids", "Gordyntjie"],
    "Striker (2pt)": [0, 0, 0, 0],
    "Bonus (3pt)": [0, 0, 0, 0],
    "UN Wins": [0, 0, 0, 0]
}

df = pd.DataFrame(data)
# Calculation: Total Score = (Striker*2) + (Bonus*3) + (UN*10) -> Adjust UN points as needed!
df['Total Score'] = (df['Striker (2pt)'] * 2) + (df['Bonus (3pt)'] * 3) + (df['UN Wins'] * 10)
df = df.sort_values(by="Total Score", ascending=False)

st.write("### 📊 LIVE LEADERBOARD")
st.table(df)

st.info("Match Day Updates: Standings refresh automatically after every goal.")
