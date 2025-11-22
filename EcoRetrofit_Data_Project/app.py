import streamlit as st
import pandas as pd
import plotly.express as px
from setup_database import get_client
from analysis_ai import analyze_efficiency, recommend_retrofits

st.set_page_config(page_title="EcoRetrofit Dashboard", layout="wide")

st.title("🏡 EcoRetrofit: Smart Home & BIM Analytics")
st.markdown("""
**Integration of IoT Data, AI, and Construction Engineering.**
This dashboard analyzes sensor data from ClickHouse to propose high-impact retrofit solutions.
""")

# Sidebar
st.sidebar.header("Configuration")
st.sidebar.info("Connected to ClickHouse Cloud")

# Main Data Load
client = get_client()
if not client:
    st.error("Could not connect to ClickHouse. Check .env file.")
    st.stop()

# 1. Overview Metrics
st.header("1. Real-Time Energy Monitoring")
query = "SELECT home_id, timestamp, energy_consumption_kwh, temperature FROM smart_home_sensors ORDER BY timestamp"
df = client.query_df(query)

# Interactive Chart
fig = px.line(df, x='timestamp', y='energy_consumption_kwh', color='home_id', title="Energy Consumption Over Time")
st.plotly_chart(fig, use_container_width=True)

# 2. AI Analysis
st.header("2. AI-Driven Inefficiency Detection")
if st.button("Run Anomaly Detection"):
    with st.spinner("Running Isolation Forest on ClickHouse Data..."):
        summary, anomalies = analyze_efficiency()
        st.success("Analysis Complete!")

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Energy Summary")
            st.dataframe(summary)
        with col2:
            st.subheader("Detected Anomalies")
            st.metric("Total Anomalous Events", len(anomalies))
            st.dataframe(anomalies.head(10))

        # 3. Recommendations
        st.header("3. Retrofit Recommendations (BIM/Engineering)")
        recs = recommend_retrofits(summary)

        for i, row in recs.iterrows():
            with st.expander(f"Recommendation for {row['home_id']}"):
                st.write(f"**Action:** {row['recommendation']}")
                st.write(f"**Reasoning:** {row['reason']}")
                st.write(f"**Est. Investment:** ${row['estimated_cost']}")

# 4. Future BIM Integration
st.markdown("---")
st.header("🔮 Future Module: Autodesk BIM Integration")
st.info("""
**concept:** This data pipeline can feed directly into **Autodesk Revit** via the Revit API or Dynamo.
- **Workflow:**
    1. ClickHouse identifies 'Drafty' zones.
    2. Python script updates the 'Thermal Resistance' parameter of Wall elements in the Revit model.
    3. Architect visualizes the new Energy Rating in 3D.
""")
