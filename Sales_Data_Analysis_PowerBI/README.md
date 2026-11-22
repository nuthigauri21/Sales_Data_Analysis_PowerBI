# Sales Data Analysis & Dashboard (Power BI)

A portfolio-ready sales analytics project aligned with the resume project:
- Process sales data with Python, Pandas and NumPy
- Perform data cleaning and exploratory analysis
- Create KPI and trend outputs
- Build an interactive Power BI dashboard for revenue, profit, growth, product and regional performance

## Dataset
`data/sales_data.csv` contains 5,000 **synthetic** order records from 2024–2025. It is generated for learning and portfolio demonstration; it is not real company data.

Main fields:
- OrderID, OrderDate, CustomerID, CustomerSegment
- Region, City, Category, Product
- Quantity, UnitPrice, Discount, Revenue, Cost, Profit
- PaymentMode, SalesChannel

## 1. Setup
Install Python 3.10+ and open a terminal in this project folder:

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# If activation is blocked, use:
.venv\Scripts\activate.bat

pip install -r requirements.txt
```

## 2. Run Python analysis
```bash
python src/analyze_sales.py
```
This validates and cleans the dataset, prints business KPIs, and writes:
- `outputs/cleaned_sales_data.csv`
- `outputs/monthly_sales.csv`
- `outputs/category_performance.csv`
- `outputs/region_performance.csv`
- `outputs/sales_dashboard_preview.png`

## 3. Build the Power BI report
1. Open **Power BI Desktop**.
2. Select **Home → Get data → Text/CSV**.
3. Import `outputs/cleaned_sales_data.csv` (or `data/sales_data.csv` if you have not run Python).
4. Select **Transform Data**. Confirm `OrderDate` is Date; numeric columns are Decimal Number/Whole Number.
5. Choose **Close & Apply**.
6. Create the DAX measures in `powerbi/DAX_Measures.dax`.
7. Create a Date table using the DAX in `powerbi/Date_Table.dax`, mark it as the Date table, and relate `Date[Date]` to `Sales[OrderDate]`.
8. Suggested report pages and visuals are in `powerbi/PowerBI_Build_Guide.md`.
9. Save as `Sales_Data_Analysis_Dashboard.pbix`.

## 4. Recommended dashboard pages
- Executive Overview: Revenue, Profit, Profit Margin, Orders, Quantity; monthly revenue/profit trend
- Product Analysis: revenue/profit by category and product; quantity and discount analysis
- Regional Analysis: revenue and profit by region/city; region slicer
- Customer & Channel: customer segment, sales channel and payment mode

## 5. Suggested project story for interviews
"I used Python and Pandas to clean and explore a 5,000-row sales dataset, calculated revenue and profitability metrics, and prepared a clean dataset for Power BI. I then designed an interactive dashboard to track KPIs and compare monthly, product, regional, customer-segment and channel performance."

Only claim steps you have actually completed. The included dataset is synthetic; state that clearly in interviews.

## 6. Folder structure
```text
Sales_Data_Analysis_PowerBI/
├── data/
├── outputs/
├── powerbi/
├── src/
├── requirements.txt
└── README.md
```


## 7. Run as a web app from GitHub (Streamlit Community Cloud)

This repository includes `app.py`, a browser-based interactive dashboard built with Streamlit.
GitHub stores the code; Streamlit Community Cloud runs the app.

### Test locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
Open the local URL shown in the terminal (usually `http://localhost:8501`).

### Deploy from GitHub
1. Create a GitHub repository, for example `sales-data-analysis-dashboard`.
2. Upload/push the **contents** of this extracted project folder to the repository root. Ensure `app.py`, `requirements.txt`, and `data/sales_data.csv` are visible at the top level / expected folders.
3. Sign in to Streamlit Community Cloud at https://share.streamlit.io/ using your GitHub account and authorize access.
4. Choose **Create app** → select your repository, branch (usually `main`), and main file path `app.py`.
5. Deploy. Streamlit will install packages from `requirements.txt` and provide a public app URL.

### Important: GitHub Pages vs Streamlit
- GitHub Pages hosts static websites; it does not execute this Python/Streamlit app.
- Use Streamlit Community Cloud to run the interactive Python dashboard from your GitHub repository.
- The Power BI `.pbix` report is a separate artifact created in Power BI Desktop. GitHub can store the `.pbix` file, but cannot execute it. To publish a Power BI report online, use Power BI Service and its sharing/embedding options.
- The included dataset is synthetic demo data, not actual company sales data.
