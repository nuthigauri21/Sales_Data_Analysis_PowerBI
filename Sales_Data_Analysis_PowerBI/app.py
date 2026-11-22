from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "sales_data.csv"

st.set_page_config(page_title="Sales Analytics Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Data Analysis & Dashboard")
st.caption("Portfolio demo | Synthetic sample sales data | 2024–2025")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    return df.dropna(subset=["OrderDate"])

df = load_data()
with st.sidebar:
    st.header("Filters")
    years = sorted(df["OrderDate"].dt.year.unique().tolist())
    selected_years = st.multiselect("Year", years, default=years)
    regions = sorted(df["Region"].unique().tolist())
    selected_regions = st.multiselect("Region", regions, default=regions)
    categories = sorted(df["Category"].unique().tolist())
    selected_categories = st.multiselect("Category", categories, default=categories)

filtered = df[
    df["OrderDate"].dt.year.isin(selected_years)
    & df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
]

if filtered.empty:
    st.warning("No records match these filters. Select at least one year, region and category.")
    st.stop()

revenue = filtered["Revenue"].sum()
profit = filtered["Profit"].sum()
orders = filtered["OrderID"].nunique()
units = filtered["Quantity"].sum()
margin = profit / revenue * 100 if revenue else 0
a, b, c, d, e = st.columns(5)
a.metric("Total Revenue", f"₹{revenue:,.0f}")
b.metric("Total Profit", f"₹{profit:,.0f}")
c.metric("Profit Margin", f"{margin:.1f}%")
d.metric("Orders", f"{orders:,}")
e.metric("Units Sold", f"{units:,}")

st.divider()
monthly = filtered.assign(Month=filtered["OrderDate"].dt.to_period("M").astype(str)).groupby("Month", as_index=False).agg(
    Revenue=("Revenue", "sum"), Profit=("Profit", "sum"))
left, right = st.columns(2)
with left:
    st.subheader("Monthly Revenue & Profit")
    long_monthly = monthly.melt("Month", var_name="Metric", value_name="Amount")
    fig = px.line(long_monthly, x="Month", y="Amount", color="Metric", markers=True)
    fig.update_layout(xaxis_title="", yaxis_title="Amount (₹)", legend_title="")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Revenue by Category")
    cat = filtered.groupby("Category", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
    fig = px.bar(cat, x="Category", y="Revenue", color="Category")
    fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Revenue (₹)")
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Regional Performance")
    reg = filtered.groupby("Region", as_index=False).agg(Revenue=("Revenue", "sum"), Profit=("Profit", "sum"))
    fig = px.bar(reg, x="Region", y=["Revenue", "Profit"], barmode="group")
    fig.update_layout(xaxis_title="", yaxis_title="Amount (₹)", legend_title="")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Sales by Customer Segment")
    seg = filtered.groupby("CustomerSegment", as_index=False)["Revenue"].sum()
    fig = px.pie(seg, names="CustomerSegment", values="Revenue", hole=0.45)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Products by Revenue")
products = filtered.groupby("Product", as_index=False).agg(
    Revenue=("Revenue", "sum"), Profit=("Profit", "sum"), Units=("Quantity", "sum"))
st.dataframe(products.sort_values("Revenue", ascending=False).head(10), use_container_width=True, hide_index=True)

with st.expander("View filtered sales records"):
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.download_button("Download filtered data as CSV", filtered.to_csv(index=False).encode("utf-8"),
                       file_name="filtered_sales_data.csv", mime="text/csv")
