from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "sales_data.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

def main():
    df = pd.read_csv(INPUT)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    numeric = ["Quantity", "UnitPrice", "Discount", "Revenue", "Cost", "Profit"]
    for col in numeric:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Basic quality checks and cleaning
    df = df.drop_duplicates(subset=["OrderID"])
    df = df.dropna(subset=["OrderID", "OrderDate", "Product", "Region"])
    df[numeric] = df[numeric].fillna(0)
    df = df[(df["Quantity"] >= 0) & (df["Revenue"] >= 0)]
    df["Year"] = df["OrderDate"].dt.year
    df["Month"] = df["OrderDate"].dt.month
    df["MonthName"] = df["OrderDate"].dt.strftime("%b")
    df["YearMonth"] = df["OrderDate"].dt.to_period("M").astype(str)
    df.to_csv(OUT / "cleaned_sales_data.csv", index=False)

    monthly = df.groupby("YearMonth", as_index=False).agg(
        Revenue=("Revenue", "sum"), Profit=("Profit", "sum"),
        Orders=("OrderID", "nunique"), Quantity=("Quantity", "sum"))
    monthly.to_csv(OUT / "monthly_sales.csv", index=False)

    category = df.groupby("Category", as_index=False).agg(
        Revenue=("Revenue", "sum"), Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum"), Orders=("OrderID", "nunique"))
    category.to_csv(OUT / "category_performance.csv", index=False)

    region = df.groupby("Region", as_index=False).agg(
        Revenue=("Revenue", "sum"), Profit=("Profit", "sum"),
        Orders=("OrderID", "nunique"))
    region.to_csv(OUT / "region_performance.csv", index=False)

    revenue = df["Revenue"].sum()
    profit = df["Profit"].sum()
    orders = df["OrderID"].nunique()
    margin = profit / revenue * 100 if revenue else 0
    print("\\nSALES PERFORMANCE SUMMARY")
    print(f"Total Revenue : ₹{revenue:,.2f}")
    print(f"Total Profit  : ₹{profit:,.2f}")
    print(f"Profit Margin : {margin:.2f}%")
    print(f"Total Orders  : {orders:,}")
    print(f"Units Sold    : {df['Quantity'].sum():,}")
    print("\\nTop categories by revenue:")
    print(category.sort_values("Revenue", ascending=False).head(5).to_string(index=False))
    print("\\nTop regions by revenue:")
    print(region.sort_values("Revenue", ascending=False).head(5).to_string(index=False))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    axes[0].plot(monthly["YearMonth"], monthly["Revenue"], marker="o")
    axes[0].set_title("Monthly Revenue Trend")
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("Revenue (₹)")
    axes[0].tick_params(axis="x", rotation=75)
    axes[1].bar(category["Category"], category["Revenue"])
    axes[1].set_title("Revenue by Category")
    axes[1].set_ylabel("Revenue (₹)")
    axes[1].tick_params(axis="x", rotation=25)
    fig.tight_layout()
    fig.savefig(OUT / "sales_dashboard_preview.png", dpi=160)
    print(f"\\nAnalysis complete. Files saved to: {OUT}")

if __name__ == "__main__":
    main()
