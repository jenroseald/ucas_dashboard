# UCAS Applications Dashboard

An interactive data dashboard built with Python and Streamlit, exploring trends in UK university applications using publicly available UCAS data.

---

## Overview

This dashboard visualises UCAS undergraduate application data, allowing users to explore how application volumes have changed over time across different student characteristics including age group, gender, and domicile (country of origin).

**Data source:** [UCAS Undergraduate Statistics and Reports](https://www.ucas.com/data-and-analysis/undergraduate-statistics-and-reports)

---

## Features

- **KPI summary cards** — total applicants, latest year total, and year-on-year percentage change
- **Interactive line chart** — applicant trends over time, coloured by selected metric
- **Bar chart** — year-on-year grouped comparison by selected metric
- **Dynamic filters** — sub-filters update based on the selected metric (e.g. filter by Maturity when viewing Age Group)
- **Data table** — formatted view of the aggregated data
- **CSV export** — download the filtered table as a CSV file

---

## Project Structure

```
ucas_dashboard/
│
├── ucas_dashboard.py          # Main Streamlit dashboard application
├── Reapplication status.csv   # Source data (UCAS applications)
├── requirements.txt           # Python package dependencies
└── README.md                  # Project documentation
```

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/ucas_dashboard.git
   cd ucas_dashboard
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**
   ```bash
   streamlit run ucas_dashboard.py
   ```

   The dashboard will open automatically in your browser at `http://localhost:8501`.

---

## Dependencies

| Package    | Purpose                          |
|------------|----------------------------------|
| Streamlit  | Web dashboard framework          |
| Pandas     | Data loading, cleaning, analysis |
| NumPy      | Numerical operations             |
| Plotly     | Interactive charts               |

---

## Data

The dataset contains UCAS undergraduate application records with the following fields:

| Column               | Description                                      |
|----------------------|--------------------------------------------------|
| Year                 | Application year                                 |
| Reapplication Status | Whether the applicant is a first-timer or reapplier |
| Age Group            | Age band of the applicant                        |
| Gender               | Gender of the applicant                          |
| Domicile             | Country/region the applicant applied from        |
| Applicants           | Number of applicants                             |

**Note:** Records prior to 2021 and rows containing aggregate totals (marked 'All') are excluded from the dashboard.

---

## Acknowledgements

- Data provided by [UCAS](https://www.ucas.com)
- Built using [Streamlit](https://streamlit.io), [Plotly](https://plotly.com/python/), and [Pandas](https://pandas.pydata.org/)
