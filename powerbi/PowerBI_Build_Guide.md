# Power BI Dashboard Build Guide

## Model setup
- Import `outputs/cleaned_sales_data.csv`.
- Rename table to `Sales`.
- Set `OrderDate` to Date; `Quantity` to Whole Number; `UnitPrice`, `Discount`, `Revenue`, `Cost`, `Profit` to Decimal Number.
- Create the Date table from `Date_Table.dax`, mark it as the date table, and relate it to Sales.
- Add all measures from `DAX_Measures.dax`.

## Page 1 — Executive Overview
- KPI Cards: Total Revenue, Total Profit, Profit Margin %, Total Orders, Units Sold.
- Line chart: Date[Year Month] vs Total Revenue and Total Profit.
- Clustered bar: Category vs Total Revenue.
- Bar chart: Region vs Total Revenue.
- Slicers: Date[Year], Region, Category, SalesChannel.

## Page 2 — Product Performance
- Bar chart: Product vs Total Revenue (sort descending).
- Matrix: Category > Product with Total Revenue, Total Profit, Profit Margin %, Units Sold.
- Scatter chart: Total Revenue vs Total Profit by Product.
- Slicers: Category, Product, Date.

## Page 3 — Regional Performance
- Filled map or bar chart: City/Region by Total Revenue (map availability may vary).
- Clustered column: Region with Total Revenue and Total Profit.
- Matrix: Region > City with Total Orders, Revenue, Profit.
- Slicers: Region, Date.

## Page 4 — Customer & Channel
- Donut: CustomerSegment by Total Revenue.
- Column chart: SalesChannel by Total Revenue and Total Orders.
- Donut: PaymentMode by Total Orders.
- Slicers: CustomerSegment, SalesChannel, PaymentMode, Date.

## Design suggestions
- Use a consistent 16:9 canvas, light neutral background, one accent color, and clear titles.
- Format Revenue/Profit as Indian Rupee currency; Profit Margin and growth as percentages.
- Use display units in thousands/millions where helpful.
- Add informative tooltips and enable cross-filtering.
- Add a small note: "Demo analysis using synthetic sample data."

## Insight checklist
When your report is built, answer:
1. Which month had the highest revenue?
2. Which category and product contributed the most revenue?
3. Which region had the highest revenue and profit?
4. Which customer segment generated the most revenue?
5. Is revenue growing year over year?
6. Which category has the strongest profit margin?

Do not write conclusions before checking the actual visuals/measures.
