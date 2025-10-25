# Bank of Stockton — Credit Risk Analysis (Monte Carlo Simulation)

### Project Overview
This project analyzes the credit-risk exposure of Bank of Stockton using publicly available FDIC Call Report data across 18 quarters (2021 Q1 – 2025 Q2).  
The main objective was to estimate potential future credit losses through Monte Carlo simulation, based on historical charge-off and recovery behavior.

---

### Objectives
- Extract and structure financial data from 18 quarterly PDF call reports.  
- Compute key risk metrics such as Net Charge-off Rate, Recovery Rate, and Provision Levels.  
- Visualize credit trends and identify stability or volatility in loan performance.  
- Use Monte Carlo simulation to model next-quarter loss scenarios.  
- Enhance realism via winsorization (outlier trimming) and t-distribution (fat-tail stress).  
- Export final results and visuals into professional Excel and PDF reports.

---

### Project Structure
```
Bank_of_stockton/
│
├── data/
│   ├── raw/               → original FDIC call report PDFs
│   ├── processed/         → cleaned CSV dataset (bank_metrics_processed.csv)
│
├── notebooks/
│   └── credit_risk.ipynb  → full analysis and simulation workflow
│
├── visualizations/
│   └── app.py             → optional Streamlit dashboard
│
├── reports/
│   ├── credit_risk_summary.xlsx
│   └── credit_risk_summary.pdf
│
└── README.md
```

---

### Methodology Summary

| Step | Task | Description |
|------|------|-------------|
| 1–3 | Data Extraction | Parsed PDFs to extract Total Loans, Charge-offs, Recoveries, Provisions, and Allowances. |
| 4–5 | Metric Derivation | Calculated Net Charge-offs, Net Charge-off Rate (annualized), and Recovery Rate. |
| 6–7 | Visualization | Plotted trends for loans, provisions, and loss behavior across quarters. |
| 8 | Interactive Dashboard (optional) | Streamlit-based app for exploratory visualization. |
| 9a | Monte Carlo Simulation | Simulated 10,000 future quarterly loss scenarios using historical mean (μ) and std. dev. (σ). |
| 9b | Enhanced Simulation | Applied winsorization + t-distribution (df = 5) for fat-tailed risk. |
| 10 | Reporting | Exported Excel + PDF summaries with key charts and results. |

---

### Key Results
- Expected Quarterly Loss (EL): ≈ $0.4 M  
- VaR 95 / 99 (Normal): ≈ $1.9 M / $2.9 M  
- VaR 95 / 99 (t-Dist): ≈ $2.4 M / $4.1 M  
- CVaR 99 (t-Dist): ≈ $5.3 M  
- Conclusion: Losses are minimal relative to total loans (~0.1 %), indicating a stable and well-reserved credit portfolio.

---

### Insights
- The bank’s loan portfolio remained stable around $4 B across 18 quarters.  
- Several quarters showed net recoveries, reflecting strong collection performance.  
- Provisioning policy is conservative — maintaining reserves even during low-loss periods.  
- Monte Carlo analysis quantified realistic risk bounds and confirmed robust credit quality.

---

### Tech Stack
**Languages & Libraries:**  
Python, pandas, numpy, matplotlib, plotly, scipy, streamlit, openpyxl, reportlab

**Tools:**  
Jupyter Notebook | VS Code | Git | Excel | PDF Reporting

---

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Bank_of_Stockton_Credit_Risk.git
   cd Bank_of_Stockton_Credit_Risk
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:
   ```bash
   jupyter notebook notebooks/credit_risk.ipynb
   ```
4. (Optional) Launch the Streamlit dashboard:
   ```bash
   python -m streamlit run visualizations/app.py
   ```

---

### Future Enhancements
- Integrate macro-economic factors (GDP, Unemployment, Fed Rate) for scenario modeling.  
- Automate quarterly updates via a lightweight ETL pipeline.  
- Deploy Streamlit dashboard as a web app with scheduled data refresh.

---

### Author
**Vishal C V**  
Email: [Add your email]  
MS Business Analytics | University of the Pacific  
Data Analytics | Credit Risk | Financial Modeling

---

### License
This project is released under the MIT License for educational and research use.
