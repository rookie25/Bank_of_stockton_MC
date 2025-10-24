# Bank of Stockton Credit Risk Monte Carlo Simulation
## Complete 10-Day Project Guide

---

## 📋 PROJECT OVERVIEW

**Project Title:** Monte Carlo Credit Risk Analysis for Bank of Stockton  
**Duration:** 10 days  
**Difficulty:** Intermediate  
**Final Deliverable:** Interactive dashboard with economic scenario analysis and risk metrics

### Project Objectives
1. Build a Monte Carlo simulation to assess credit risk
2. Analyze potential losses under different economic scenarios
3. Create professional visualizations and dashboard
4. Provide actionable risk management insights

### Key Questions This Project Answers
- What are the expected credit losses under normal conditions?
- How severe could losses become in a recession?
- Is the bank adequately capitalized for potential risks?
- Which loan segments drive the most risk?
- What is our confidence level in these predictions?

---

## 📊 DATA SOURCES

### Primary Data Source
- **FDIC Call Reports**: https://cdr.ffiec.gov/public/ManageFacsimiles.aspx
- **Bank Identifier**: Bank of Stockton (FDIC Cert #1536)
- **Time Period**: Last 12-16 quarters (3-4 years)

### Required Call Report Schedules
1. **Schedule RC-C**: Loan and lease portfolio breakdown
2. **Schedule RC-N**: Past due and nonaccrual loans
3. **Schedule RI-B**: Charge-offs and recoveries
4. **Schedule RC**: Balance sheet totals
5. **Schedule RC-R**: Regulatory capital

### Economic Data Sources
- **FRED (Federal Reserve Economic Data)**: https://fred.stlouisfed.org/
  - Unemployment rate (CAUR for California)
  - GDP growth (GDP)
  - Federal funds rate (DFF)
  - 10-year Treasury rate (DGS10)

### Key Metrics from Bank of Stockton
- Total Assets: $4.6 billion
- Total Loans: $2.9 billion
- NPL Ratio: 0.20%
- Tier 1 Capital Ratio: 17.92%
- Net Interest Margin: 3.37%

---

## 📅 10-DAY DETAILED ROADMAP

## PHASE 1: CORE MONTE CARLO (Days 1-2)

### DAY 1: Data Collection & Setup

#### Morning Tasks (2-3 hours)
**1. Project Setup**
```
Create folder structure:
/BankOfStockton_CreditRisk/
  ├── /data/
  │   ├── /raw/
  │   ├── /processed/
  │   └── /external/
  ├── /code/
  ├── /visualizations/
  ├── /reports/
  └── README.md
```

**2. Data Collection**
- Navigate to https://cdr.ffiec.gov/public/
- Search for "Bank of Stockton" or use FDIC Cert #1536
- Download Call Reports for Q1 2021 - Q1 2025 (16 quarters)
- Save PDFs or Excel files in `/data/raw/`

#### Afternoon Tasks (2-3 hours)
**3. Data Extraction**
Create a spreadsheet with these columns:
- Quarter (e.g., 2024-Q1)
- Total Loans (Schedule RC-C, Line 12)
- Non-performing Loans (Schedule RC-N, sum of 90+ days)
- Gross Charge-offs (Schedule RI-B, Part A)
- Recoveries (Schedule RI-B, Part A)
- Net Charge-offs (Charge-offs minus Recoveries)
- Provisions (Schedule RI, Line 4)

**4. Calculate Key Metrics**
```
For each quarter calculate:
- NPL Ratio = NPL / Total Loans
- Gross Charge-off Rate = (Charge-offs / Total Loans) × 4
- Recovery Rate = Recoveries / Charge-offs
- Net Charge-off Rate = Net Charge-offs / Total Loans × 4
```

**Day 1 Deliverable:** ✅ Clean dataset with 16 quarters of credit metrics

---

### DAY 2: Build Basic Monte Carlo Engine

#### Morning Tasks (3 hours)
**1. Statistical Analysis**
```python
Calculate from your data:
- Mean loss rate (μ): ~0.10%
- Standard deviation (σ): ~0.05%
- Minimum historical rate: ~0.02%
- Maximum historical rate: ~0.25%
- Distribution type: Test for Normal vs. LogNormal
```

**2. Choose Your Tools**
- **Option A (Excel)**: Use Data Analysis Toolpak
- **Option B (Python)**: pandas, numpy, scipy, matplotlib
- **Option C (R)**: tidyverse, ggplot2

#### Afternoon Tasks (3 hours)
**3. Build First Simulation**
```
Pseudo-code for basic Monte Carlo:
1. Set parameters:
   - Number of simulations = 1,000
   - Loan portfolio = $2,900 million
   - Loss rate ~ Normal(μ=0.10%, σ=0.05%)

2. For each simulation i from 1 to 1,000:
   - Generate random loss_rate[i]
   - Calculate loss[i] = loss_rate[i] × portfolio
   - Store result

3. Analyze results:
   - Mean expected loss
   - 5th, 25th, 50th, 75th, 95th percentiles
   - Maximum and minimum losses
```

**4. Create First Visualization**
- Histogram of 1,000 loss outcomes
- Mark mean and 95% confidence level
- Title: "Credit Loss Distribution - Base Case"

**Day 2 Deliverable:** ✅ Working Monte Carlo with 1,000 simulations and histogram

---

## PHASE 2: ECONOMIC SCENARIOS (Days 3-4)

### DAY 3: Economic Data Integration

#### Morning Tasks (2 hours)
**1. Collect Economic Data**
From FRED, download quarterly data (2021-2025):
- California unemployment rate (CAUR)
- US GDP growth rate
- Federal funds effective rate
- Optional: Housing price index for Stockton MSA

**2. Align with Bank Data**
- Match quarters with your loss data
- Create combined dataset with bank + economic variables

#### Afternoon Tasks (4 hours)
**3. Correlation Analysis**
```
Steps:
1. Create scatter plots:
   - X-axis: Unemployment rate
   - Y-axis: Loss rate
   
2. Calculate correlation coefficient

3. Build regression model:
   Loss_Rate = α + β × Unemployment_Rate
   
4. Document the relationship strength (R-squared)
```

**4. Build Economic-Driven Loss Model**
```
Enhanced loss model:
Base_Loss_Rate = 0.10%
Unemployment_Impact = β × (Current_Unemployment - 4%)
Total_Loss_Rate = Base_Loss_Rate + Unemployment_Impact + Random_Component
```

**Day 3 Deliverable:** ✅ Economic model linking unemployment to credit losses

---

### DAY 4: Three Economic Scenarios

#### Morning Tasks (3 hours)
**1. Define Scenarios**

**Baseline Scenario (Most Likely)**
- Unemployment: 4-5%
- GDP Growth: 2%
- Duration: 8 quarters
- Probability weight: 60%

**Adverse Scenario (Mild Recession)**
- Unemployment: 7-8%
- GDP Growth: -1%
- Duration: 8 quarters
- Probability weight: 30%

**Severely Adverse Scenario (Deep Recession)**
- Unemployment: 10-12%
- GDP Growth: -4%
- Duration: 8 quarters
- Probability weight: 10%

#### Afternoon Tasks (3 hours)
**2. Run Scenario Simulations**
```
For each scenario:
1. Set economic parameters
2. Run 1,000 simulations
3. Calculate loss distribution
4. Store results separately
```

**3. Create Scenario Comparison**
- Table comparing expected losses
- Overlapping histograms
- Box plots showing ranges

**Day 4 Deliverable:** ✅ Three complete economic scenarios with comparative analysis

---

## PHASE 3: ENHANCED SIMULATION (Days 5-6)

### DAY 5: Portfolio Segmentation

#### Morning Tasks (3 hours)
**1. Break Down Loan Portfolio**
Based on Schedule RC-C:
```
Total Portfolio: $2,900 million
├── Commercial Real Estate (CRE): $1,300M (45%)
├── Commercial & Industrial (C&I): $870M (30%)
├── Agricultural Loans: $435M (15%)
└── Consumer Loans: $290M (10%)
```

**2. Segment-Specific Risk Parameters**
```
Loan Type        | Base Loss | Volatility | Unemployment Beta
-----------------|-----------|------------|------------------
CRE              | 0.08%     | Medium     | 0.6
C&I              | 0.15%     | High       | 0.8
Agricultural     | 0.12%     | High       | 0.4
Consumer         | 0.20%     | Low        | 1.0
```

#### Afternoon Tasks (3 hours)
**3. Segmented Simulation**
- Run simulation for each loan segment
- Aggregate total portfolio losses
- Analyze contribution to total risk

**4. Create Portfolio Risk Dashboard**
- Pie chart of loan composition
- Bar chart of losses by segment
- Risk contribution analysis

**Day 5 Deliverable:** ✅ Portfolio-level segmented risk analysis

---

### DAY 6: Correlations & Advanced Metrics

#### Morning Tasks (3 hours)
**1. Implement Correlation Matrix**
```
Correlation Matrix:
         CRE    C&I    Agri   Consumer
CRE      1.0    0.6    0.3    0.2
C&I      0.6    1.0    0.4    0.3
Agri     0.3    0.4    1.0    0.2
Consumer 0.2    0.3    0.2    1.0
```

**2. Correlated Simulation**
- Use Cholesky decomposition or copulas
- Generate correlated random variables
- Re-run all scenarios with correlations

#### Afternoon Tasks (3 hours)
**3. Calculate Risk Metrics**
```
Key Metrics to Calculate:
- Expected Loss (EL): Mean of distribution
- Unexpected Loss (UL): Standard deviation
- Value at Risk (VaR) 95%: 95th percentile
- Value at Risk (VaR) 99%: 99th percentile
- Conditional VaR (CVaR): Average of worst 5%
- Economic Capital: VaR(99%) - EL
```

**4. Create Risk Metrics Summary**
Professional risk report table with all metrics

**Day 6 Deliverable:** ✅ Complete simulation with correlations and professional risk metrics

---

## PHASE 4: PROFESSIONAL VISUALIZATIONS (Days 7-8)

### DAY 7: Core Visualizations

#### Full Day Tasks (6 hours)
Create these essential charts:

**1. Loss Distribution Histogram**
```
Components:
- Overlay all three scenarios
- Different colors with transparency
- Mark mean, VaR(95%), VaR(99%)
- Professional labels and legend
```

**2. Scenario Comparison Dashboard**
```
4-panel dashboard:
├── Panel 1: Expected losses bar chart
├── Panel 2: Probability density functions
├── Panel 3: Cumulative distribution functions
└── Panel 4: Key metrics table
```

**3. Portfolio Risk Heatmap**
```
Matrix showing:
- Rows: Loan types
- Columns: Scenarios
- Colors: Risk levels (green to red)
- Values: Expected losses
```

**4. Time Series Projection**
```
8-quarter forecast showing:
- Expected loss trajectory
- 95% confidence bands
- Scenario paths
```

**Day 7 Deliverable:** ✅ Four professional-quality visualizations

---

### DAY 8: Interactive Dashboard

#### Morning Tasks (3 hours)
**1. Choose Platform**
- **Excel**: Use slicers and pivot tables
- **Tableau Public**: Free, professional
- **Python**: Streamlit or Plotly Dash
- **Power BI**: If available

**2. Design Layout**
```
Dashboard Structure:
┌─────────────────────────────────┐
│     Executive Summary           │
├──────────┬──────────────────────┤
│ Controls │   Main Display        │
│          │                      │
│ Scenario │   Loss Distribution   │
│ Selector │                      │
│          ├──────────────────────┤
│ Params   │   Risk Metrics       │
│          │                      │
└──────────┴──────────────────────┘
```

#### Afternoon Tasks (3 hours)
**3. Add Interactivity**
- Scenario dropdown selector
- Parameter sliders (if applicable)
- Hover tooltips with details
- Export functionality

**4. Testing & Refinement**
- Test all interactions
- Verify calculations update
- Ensure mobile responsiveness (if web-based)

**Day 8 Deliverable:** ✅ Fully functional interactive dashboard

---

## PHASE 5: UNIQUE INSIGHT & DELIVERY (Days 9-10)

### DAY 9: Deep Dive Analysis

#### Morning Tasks (3 hours)
**Choose ONE unique angle:**

**Option A: Agricultural Risk Focus**
```
Analysis points:
- Drought scenario impact on ag loans
- Correlation with commodity prices
- Climate change risk assessment
- Water rights valuation impact
```

**Option B: Regional Economic Dependencies**
```
Analysis points:
- Stockton port activity correlation
- Central Valley economic indicators
- Housing market specific risks
- Tech industry spillover from Bay Area
```

**Option C: Peer Comparison**
```
Analysis points:
- Compare to similar sized CA banks
- Benchmark risk levels
- Best practices identification
- Competitive positioning
```

#### Afternoon Tasks (3 hours)
**2. Deep Analysis**
- Gather additional data for chosen topic
- Run specialized analysis
- Create 2-3 unique visualizations
- Document key findings

**Day 9 Deliverable:** ✅ Unique insight with supporting analysis

---

### DAY 10: Polish & Package

#### Morning Tasks (3 hours)
**1. Executive Summary (1 page)**
```
Structure:
- Background (2 sentences)
- Methodology (3 sentences)
- Key Findings (3-5 bullets)
- Risk Assessment (1 paragraph)
- Recommendations (3 bullets)
- Confidence Statement
```

**2. Key Findings Document**
```
Must include:
1. Expected losses by scenario
2. Capital adequacy assessment
3. Main risk drivers identified
4. Your unique insight
5. Confidence levels and limitations
```

#### Afternoon Tasks (3 hours)
**3. Final Package Assembly**
```
Deliverables checklist:
□ Executive summary (PDF)
□ Interactive dashboard
□ Technical documentation
□ Raw data files
□ Code/formulas used
□ Presentation slides (optional)
□ README file
```

**4. Documentation**
```
README should include:
- Project overview
- Data sources
- Methodology
- How to run simulation
- Key assumptions
- Limitations
- Future improvements
```

**Day 10 Deliverable:** ✅ Complete, polished project package

---

## 📊 TECHNICAL SPECIFICATIONS

### Monte Carlo Simulation Parameters
```
Base Configuration:
- Iterations: 1,000 minimum (10,000 preferred)
- Time horizon: 8 quarters
- Confidence levels: 90%, 95%, 99%
- Random seed: Set for reproducibility
```

### Statistical Distributions
```
Options to consider:
- Normal: Simple, symmetric
- LogNormal: Prevents negative values
- Beta: Bounded between 0 and 1
- Triangular: Good for scenarios
```

### Correlation Implementation
```python
# Pseudo-code for correlation
import numpy as np

# Define correlation matrix
corr_matrix = np.array([[1.0, 0.6, 0.3, 0.2],
                        [0.6, 1.0, 0.4, 0.3],
                        [0.3, 0.4, 1.0, 0.2],
                        [0.2, 0.3, 0.2, 1.0]])

# Cholesky decomposition
L = np.linalg.cholesky(corr_matrix)

# Generate correlated random numbers
uncorrelated = np.random.normal(0, 1, (1000, 4))
correlated = uncorrelated @ L.T
```

---

## 📈 EXPECTED RESULTS

### Baseline Scenario
- Expected Loss: $3-5 million
- VaR (95%): $6-8 million
- VaR (99%): $8-10 million

### Adverse Scenario
- Expected Loss: $10-15 million
- VaR (95%): $18-22 million
- VaR (99%): $25-30 million

### Severely Adverse Scenario
- Expected Loss: $25-40 million
- VaR (95%): $45-60 million
- VaR (99%): $70-85 million

### Capital Adequacy Assessment
- Current Capital: $826 million
- Worst Case Loss: ~$85 million
- Capital Coverage: ~10x (Very Strong)

---

## ⚡ SHORTCUTS & QUICK WINS

### If Behind Schedule
1. **Day 5**: Skip portfolio segmentation, use total portfolio only
2. **Day 6**: Skip correlations, use independent risks
3. **Day 9**: Skip unique insight, focus on core analysis
4. **Reduce simulations**: 500 instead of 1,000

### If Ahead of Schedule
1. Add backtesting using 2020-2022 data
2. Implement additional economic variables
3. Create video walkthrough
4. Add machine learning predictions
5. Build automated report generation

### Time-Saving Tools
- **Excel Templates**: Use built-in Monte Carlo add-ins
- **Python Libraries**: Use existing risk libraries (pyfolio, riskfolio)
- **Online Calculators**: For quick statistical calculations
- **ChatGPT/Claude**: For code debugging and formula help

---

## 🎯 SUCCESS CRITERIA

Your project is successful if you can confidently answer:

1. ✅ **"What are normal expected losses?"**
   - Answer: $3-5 million quarterly

2. ✅ **"How bad could it get in a recession?"**
   - Answer: $25-40 million in severe scenario

3. ✅ **"Is the bank well-capitalized?"**
   - Answer: Yes, capital exceeds worst-case by 10x

4. ✅ **"What drives the risk?"**
   - Answer: Unemployment + loan composition

5. ✅ **"How confident are we?"**
   - Answer: 95% confident losses won't exceed $X

---

## 📚 RESOURCES & REFERENCES

### Data Sources
- FDIC Bank Find: https://banks.data.fdic.gov/
- Call Reports: https://cdr.ffiec.gov/public/
- FRED Economic Data: https://fred.stlouisfed.org/
- UBPR Reports: https://cdr.ffiec.gov/public/ManageFacsimiles.aspx

### Technical References
- Basel III Framework
- CECL (Current Expected Credit Losses) methodology
- Federal Reserve Stress Testing Methodology
- Monte Carlo Methods in Finance (Glasserman)

### Tools & Software
- **Excel**: Data Analysis Toolpak, @RISK add-in
- **Python**: pandas, numpy, scipy, matplotlib, seaborn
- **R**: tidyverse, ggplot2, quantmod
- **Visualization**: Tableau Public, Power BI, Plotly

### Learning Resources
- Coursera: "Credit Risk Modeling in Python"
- YouTube: "Monte Carlo Simulation Explained"
- Medium: Articles on bank risk analysis
- GitHub: Search for "credit risk monte carlo"

---

## 🔧 TROUBLESHOOTING GUIDE

### Common Issues & Solutions

**Problem**: Can't find specific Call Report data
- **Solution**: Use UBPR reports as alternative source

**Problem**: Simulation gives negative losses
- **Solution**: Use LogNormal distribution or max(0, loss)

**Problem**: Results seem unrealistic
- **Solution**: Check units (millions vs billions), verify percentages

**Problem**: Correlation matrix not positive definite
- **Solution**: Use nearest positive definite matrix algorithm

**Problem**: Dashboard too slow
- **Solution**: Pre-calculate results, use sampling for display

---

## 📝 SAMPLE CODE SNIPPETS

### Basic Monte Carlo in Python
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
n_simulations = 1000
loan_portfolio = 2900  # millions
mean_loss_rate = 0.001  # 0.10%
std_loss_rate = 0.0005  # 0.05%

# Simulation
np.random.seed(42)
loss_rates = np.random.normal(mean_loss_rate, std_loss_rate, n_simulations)
losses = loss_rates * loan_portfolio

# Analysis
expected_loss = np.mean(losses)
var_95 = np.percentile(losses, 95)
var_99 = np.percentile(losses, 99)

# Visualization
plt.figure(figsize=(10, 6))
plt.hist(losses, bins=50, alpha=0.7, color='blue', edgecolor='black')
plt.axvline(expected_loss, color='red', linestyle='--', label=f'Expected Loss: ${expected_loss:.1f}M')
plt.axvline(var_95, color='orange', linestyle='--', label=f'VaR 95%: ${var_95:.1f}M')
plt.xlabel('Loss ($ Millions)')
plt.ylabel('Frequency')
plt.title('Credit Loss Distribution - Monte Carlo Simulation')
plt.legend()
plt.show()
```

### Basic Monte Carlo in Excel
```
Cell Formulas:
A1: "Simulation #"
B1: "Loss Rate"
C1: "Loss Amount"

A2: 1
A3: 2 (drag down to 1000)

B2: =NORM.INV(RAND(), 0.001, 0.0005)
C2: =MAX(0, B2*2900)

Summary Statistics:
Expected Loss: =AVERAGE(C2:C1001)
VaR 95%: =PERCENTILE(C2:C1001, 0.95)
VaR 99%: =PERCENTILE(C2:C1001, 0.99)
```

---

## 💼 PRESENTATION TEMPLATE

### Slide Structure (10 slides)
1. **Title Slide**: Project name, your name, date
2. **Executive Summary**: 3 key findings
3. **Problem Statement**: Why credit risk matters
4. **Methodology**: Monte Carlo approach
5. **Data Sources**: FDIC, economic data
6. **Base Results**: Loss distribution
7. **Scenario Analysis**: Three scenarios compared
8. **Risk Metrics**: VaR, CVaR, capital adequacy
9. **Unique Insight**: Your special finding
10. **Recommendations**: 3-5 action items

---

## ✅ FINAL CHECKLIST

### Before Submission
- [ ] All data sources documented
- [ ] Code/formulas commented
- [ ] Visualizations have titles and labels
- [ ] Executive summary is clear and concise
- [ ] Results are sanity-checked
- [ ] Dashboard is functional
- [ ] README is complete
- [ ] Files are organized
- [ ] Backup created

### Quality Checks
- [ ] Numbers make business sense
- [ ] Visualizations tell a story
- [ ] Technical approach is sound
- [ ] Limitations acknowledged
- [ ] Professional presentation

---

## 🎓 LEARNING OUTCOMES

By completing this project, you will have:
1. Built a real Monte Carlo simulation
2. Analyzed actual bank data
3. Created professional risk metrics
4. Developed economic scenarios
5. Produced executive-ready visualizations
6. Demonstrated data science skills
7. Shown financial domain knowledge

---

## 🚀 EXTENSIONS & FUTURE WORK

### Potential Enhancements
1. Machine learning for default prediction
2. Stress testing automation
3. Real-time data integration
4. Multi-bank comparison tool
5. Regulatory capital optimizer
6. Climate risk scenarios
7. Behavioral modeling
8. Network contagion effects

### Career Applications
This project demonstrates skills valuable for:
- Risk Analyst positions
- Credit Risk Modeling roles
- Financial Data Scientist positions
- Consulting opportunities
- Regulatory compliance roles
- Portfolio management positions

---

## 📧 PROJECT SUPPORT

### When You Need Help
1. **Data Issues**: Verify source, check calculations
2. **Technical Problems**: Stack Overflow, documentation
3. **Statistical Questions**: Cross-validate with textbooks
4. **Banking Knowledge**: Federal Reserve publications
5. **Presentation**: Follow professional templates

### Remember
- **Progress > Perfection**: Better to finish simple than abandon complex
- **Document Everything**: Your future self will thank you
- **Ask for Feedback**: Share with peers or mentors
- **Celebrate Milestones**: Each day completed is progress

---

## 🎯 FINAL WORDS OF ENCOURAGEMENT

You're building a professional-grade risk analysis that real banks use daily. This project will:
- Showcase technical skills
- Demonstrate business acumen
- Prove you can handle complex data
- Show you can communicate results

Every major bank runs similar analyses. By completing this project, you're proving you can work at their level.

**Good luck! You've got this! 🚀**

---

*Last Updated: [Current Date]*
*Version: 1.0*
*Total Pages: 25*