import streamlit as st

# --- Page configuration ---
st.set_page_config(page_title="MathCraft Hub", layout="centered", page_icon="🧠")

# --- App Header ---
st.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(90deg, #4b6cb7, #182848); border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; margin: 0;">🧠 MathCraft Learning Hub</h1>
    <p style="color: #d1d1d1; font-style: italic;">Explore interactive math apps aligned to Michigan standards</p>
</div>
""", unsafe_allow_html=True)

# --- Section: App Directory ---
st.header("📚 Available Apps")

apps = {
    "Tessellation & Sequences": "https://mathcraft-tessellation.streamlit.app",
    "Irrational Numbers": "https://mathcraft-irrationalnumbers.streamlit.app",
    "4th Grade Area & Measurement": "https://mathcraft-area-pencils.streamlit.app",
    "Estimation & Accuracy": "https://mathcraft-estimation-lab.streamlit.app",
    "Graphing Transformations": "https://mathcraft-transformations.streamlit.app",
}

for app_name, app_url in apps.items():
    st.markdown(f"🔗 **[{app_name}]({app_url})**")

# --- Optional Section: Description / Footer ---
st.markdown("---")
st.markdown("""
*Developed by Xavier Honablue • Math, Data, & Imagination  
Contact: honablue@umich.edu | GitHub: [xhonablue-source](https://github.com/xhonablue-source)*
""")
