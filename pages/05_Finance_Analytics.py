import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine, text
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Finance Dashboard | Technify ERP",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── LIGHT THEME & FONT REPLICATION (MATCHED) ──────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;500;600;700;800;900&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif !important;
        background-color: #f8fafc !important; /* Pristine Light Background */
        color: #0f172a !important; /* Slate 900 Text */
    }
    .block-container {
        padding: 2rem 2.5rem 1rem 2.5rem !important;
        max-width: 100% !important;
    }

    /* Spacing & Layout Tuning */
    .element-container { margin-bottom: 0 !important; padding-bottom: 0 !
