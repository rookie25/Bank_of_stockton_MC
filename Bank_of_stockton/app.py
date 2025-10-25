# --- Streamlit Credit Risk Dashboard (Fix A: robust path handling) ---

from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------- PATH SETUP -----------------
# Resolve the project root (parent folder of this script)
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "processed" / "bank_metrics_processed.csv"

# Check file existence
if not DATA.exists():
    st.error(f"❌ Data file not found at: {DATA}\n"
             "Please rerun Step 6 in Jupyter to regenerate 'bank_metrics_processed.csv'.")
    st.stop()

# ----------------- LOAD DATA -----------------
df = pd.read_csv(DATA)

# Sort quarters chronologically
quarters = sorted(df["Quarter"].unique(),
                  key=lambda q: (int(q.split("-")[0]), int(q.split("-")[1][1])))
df["Quarter"] = pd.Categorical(df["Quarter"], categories=quarters, ordered=True)
df = df.sort_values("Quarter")

# ----------------- PAGE LAYOUT -----------------
st.set_page_config(page_title="Bank of Stockton Credit Risk Dashboard", layout="wide")
st.title("🏦 Bank of Stockton — Credit Risk Dashboard")

metric_map = {
    "Total Loans": "Total_Loans",
    "Net Charge-off Rate (annualized)": "Net_CO_Rate",
    "Recovery Rate": "Recovery_Rate",
    "Provision": "Provision",
    "Net Charge-offs": "Net_ChargeOffs",
}

col1, col2 = st.columns([2, 1])

# ----------------- METRIC SELECTION -----------------
with col2:
    metric_label = st.selectbox("Select metric", list(metric_map.keys()), index=1)
    sel = metric_map[metric_label]
    latest = df.iloc[-1][sel]
    st.metric("Latest value",
              f"{latest:,.4f}" if "Rate" in metric_label else f"{latest:,.0f}")

with col1:
    fig = px.line(df, x="Quarter", y=sel, markers=True,
                  title=f"{metric_label} Over Time",
                  hover_data=["Total_Loans", "Provision", "Net_ChargeOffs"])
    st.plotly_chart(fig, use_container_width=True)

# ----------------- COMPARATIVE VIEW -----------------
st.markdown("### Provision vs. Net Charge-offs")
fig2 = px.line(df, x="Quarter", y=["Provision", "Net_ChargeOffs"],
               markers=True, title="Provision vs. Net Charge-offs")
fig2.update_layout(legend_title_text="")
st.plotly_chart(fig2, use_container_width=True)

# ----------------- DATA TABLE -----------------
st.markdown("---")
st.dataframe(df)
