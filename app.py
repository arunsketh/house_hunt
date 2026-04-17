import streamlit as st
import os
import pandas as pd
from sqlite3 import connect

st.title("🏡 HomeHunt Dashboard")

# Sidebar for API Keys
with st.sidebar:
    st.header("Settings")
    firecrawl_key = st.text_input("Firecrawl API Key", type="password")

st.info("HomeHunt is a CLI tool. This dashboard will eventually run the underlying logic.")

# Placeholder for showing results from the SQLite DB
if st.button("Refresh Results"):
    try:
        conn = connect('homehunt.db')
        df = pd.read_sql_query("SELECT * FROM properties", conn)
        st.dataframe(df)
    except:
        st.warning("No database found yet. Run a search first!")
