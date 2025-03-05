# 📊 Gas Price Forecasting Engine

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![R](https://img.shields.io/badge/R-4.0%2B-blue.svg)](https://www.r-project.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

This project implements a sophisticated approach to predicting US Average Gas Prices using multiple economic indicators and market variables. By analyzing monthly variables including Unemployment, CPI, Crude Oil prices, S&P 500 performance, and Energy ETFs (XLE and VDE), we provide accurate predictions for gas prices in the following month using both Linear Regression and Gradient Boosting models.

## 🔧 Software and Platform Requirements

The project utilizes both Python and R environments:

**Python Environment (Visual Studio Code):**
- yfinance: Yahoo Finance API data retrieval
- datetime: Date encoding operations
- pandas: Data preprocessing and cleaning

**R Environment (R Studio):**
- lubridate: Date handling
- xlsx & readxl: Data cleaning
- dplyr: Pipeline functionality
- ggplot2: Visualization
- caret: Model implementation

**Platform:** Mac OS

## 📁 Repository Structure

```
gas-price-forecasting/
├── src/                    # Source code
│   ├── models/            # ML model implementations
│   ├── utils/             # Utility functions
│   └── scripts/           # Data processing scripts
├── data/                  # Data files
│   ├── raw/              # Original API and downloaded data
│   ├── processed/        # Cleaned, transformed data
│   └── external/         # External source data
├── notebooks/            # Jupyter notebooks
├── visualizations/       # Generated graphics
├── docs/                # Documentation
└── requirements.txt     # Project dependencies
```

## 🚀 Instructions for Use

1. **Data Collection:**
   - Execute Script 1 (Python) to pull Yahoo Finance API data
   - Alternative: Use provided CSV files in `data/raw/API/`
   - Download additional data files from `data/raw/DOWNLOADS/`

2. **Data Preprocessing:**
   - Run Script 1.5 to combine and format downloaded data
   - Execute Script 2 in R Studio to create final dataset

3. **Analysis:**
   - Run Script 3 for model creation and analysis
   - Check `visualizations/` for output graphs

## 📊 Model Performance

Our dual modeling approach provides comprehensive price predictions:

- **Linear Regression:**
  - Captures long-term market trends
  - Analyzes variable correlations
  - Statistical significance testing

- **Gradient Boosting:**
  - Handles non-linear relationships
  - Feature importance ranking
  - Cross-validation results

## 📚 Data Sources

1. [U.S. Energy Information Administration (EIA)](https://www.eia.gov/energyexplained/gasoline/factors-affecting-gasoline-prices.php)
2. [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/)
3. [U.S. Regular Gas Prices Data](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=pet&s=emm_epmr_pte_nus_dpg&f=m)
4. [Yahoo Finance API](https://finance.yahoo.com/)

## 👥 Contributors

- Andre Chuabio
- Alexander Smithgall
- [Other team members]

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Yahoo Finance API for market data
- Federal Reserve Economic Data
- U.S. Energy Information Administration
- Open-source ML community

---

⭐️ If you find this project useful, please consider giving it a star! 
