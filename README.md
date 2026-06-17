# UCAS Dashboard (M.Halpin / CETM25 / June 2026) — User README

**Product name:** UCAS Applicant Trends Dashboard  
**Version:** 1.0 (Prototype)  
**Access:** [https://mjhalpin.streamlit.app](https://mjhalpin.streamlit.app)  
**Data source:** [UCAS 2026 Cycle Applicant Figures — 15 October Deadline](https://www.ucas.com/data-and-analysis/undergraduate-statistics-and-reports/ucas-undergraduate-releases/applicant-releases-for-2026-cycle/2026-cycle-applicant-figures-15-october-deadline)

---

## What This Dashboard Does

This dashboard presents UK university application trends from 2023, 2024 and 2025, drawn from UCAS (the Universities and Colleges Admissions Service) annual applicant data. It allows users to explore how the number of applicants has changed over time, broken down by:

- **Age group** (17 and under, 18, 19, 20, 21 - 24, 25 - 29, 30 - 34, 35 and over)
- **Gender** (Male, Female, I prefer not to day, I use another term)
- **Domicile** (the country the student applied from, e.g. England, Scotland, EU, Non-EU)

The dashboard is designed to be used by junior government officials to present data stories to professional data journalists and members of the public. No data science knowledge is required to use it.

---

## Who This README Is For

This guide is written for **junior government officials** who need to open, use, and share the dashboard. No coding or technical knowledge is needed.

---

## Part 1: Accessing the Dashboard

The dashboard is available via its public web address:

**[https://mjhalpin.streamlit.app](https://mjhalpin.streamlit.app)**

Simply open this link in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari). No login, installation or download is required.

> **Note:** The dashboard may take up to 30 seconds to load on first visit if it has been inactive. This is normal — please wait for it to appear.

---

## Part 2: Using the Dashboard

### The Main Screen

When the dashboard loads, you will see:

- A **title** and brief description at the top
- Three **summary figures** (KPI cards) showing total applicants, the most recent year's total, and the year-on-year percentage change
- A **line chart** showing applicant trends over time
- A **bar chart** showing a side-by-side year comparison
- A **data table** at the bottom with a download button

---

### The Filter Panel (Sidebar)

On the left-hand side of the screen, there is a filter panel.

> **On a mobile device:** The filter panel is hidden by default. Tap the **arrow (›)** in the top-left corner of the screen to open it.

The filter panel has two parts:

**1. Choose a Metric**
Use the dropdown at the top to choose how you want to break down the charts:
- **Age Group** — splits data by applicant age ranges
- **Gender** — splits data by Male, Female, or Other
- **Domicile** — splits data by where the applicant applied from

**2. Filter Your Chart**
Once you have chosen a metric, a filter appears below it. Use this to show or hide specific categories. For example, if you chose "Gender", you can tick or untick Male, Female, and Other to include or exclude them from the charts.

All charts and summary figures update automatically when you change a filter.

---

### Reading the Charts

**Line chart — Trend Over Time**
Shows how applicant numbers changed across 2023, 2024 and 2025 for each category. Hover your mouse over any point on the line to see the exact figure.

**Bar chart — Year-on-Year Comparison**
Shows the same data as horizontal bars, grouped by year, making it easier to compare categories side by side.

**Data table**
Shows the underlying numbers behind the charts. You can scroll left and right if there are many columns.

---

### Downloading the Data

At the bottom of the page, beneath the data table, there is a **"Download table as CSV"** button.

Clicking this will save the currently displayed data as a spreadsheet file (`.csv`) that can be opened in Microsoft Excel or similar software.

> The downloaded file will only contain the data currently visible based on your filter selections.

> This data is sourced from UCAS open public data and is free to reuse and share with attribution to the original source. Contact the developer to request alternative accessible formats.

---

## Part 3: Updating the Data

> **This section is for authorised staff only.** Members of the public and journalists do not need to update the data.

The dashboard data is stored securely in Google Cloud Storage (GCS). When a new UCAS dataset is available each year, authorised staff can update the dashboard by uploading the new data file directly to the GCS bucket. No coding or technical knowledge is required.

### What You Will Need
- The updated CSV file downloaded from [UCAS Data and Analysis](https://www.ucas.com/data-and-analysis)
- Authorised access to the Google Cloud Storage bucket for this project (provided by the developer)

### Important: The CSV Must Follow This Structure

The CSV file **must** contain the following columns with these exact names (spelling and capitalisation matter):

| Column name | Example values |
|---|---|
| `Year` | 2023, 2024, 2025 |
| `Applicants` | 45320 |
| `Age Group` | 17, 18–19, 20–21, 25–29, 35 and Over |
| `Gender` | Man, Woman, I prefer not to say, I use another term |
| `Domicile` | England, Scotland, Wales, Northern Ireland, Other EU, Non-EU |
| `Reapplicant Status` | First time applicant, Reapplicant |

> If the column names or values differ from the above, the dashboard may display an error. Contact the developer if this occurs.

### Steps to Update

1. Save your new CSV file using the exact filename: `Reapplication status.csv`
2. Log in to the [Google Cloud Console](https://console.cloud.google.com) using your authorised account
3. Navigate to **Cloud Storage** and open the bucket provided to you by the developer
4. Click **Upload files** and select your new `Reapplication status.csv` file
5. Confirm the upload — the existing file will be replaced
6. The live dashboard at [https://mjhalpin.streamlit.app](https://mjhalpin.streamlit.app) will automatically reflect the updated data within a few minutes

> If you do not have access to the Google Cloud Storage bucket, contact the developer to request access before proceeding.

---

## Part 4: Troubleshooting

| Problem | What to do |
|---|---|
| The dashboard is blank or shows a loading spinner | Wait up to 30 seconds and refresh the page |
| "Data cleaning failed" error message | Check that the CSV file matches the column structure in Part 3 |
| Filters are not visible | On mobile, tap the arrow (›) in the top-left to open the sidebar |
| Charts show "No data matches the selected filters" | You have deselected all filter options — tick at least one to restore the chart |
| The download button does not work | Try a different browser (Chrome or Edge recommended) |
| Data does not appear to have updated after upload | Wait a few minutes and refresh the page; if the problem persists, contact the developer |

---

## Part 5: Technical Information for IT Staff

| Item | Detail |
|---|---|
| Language | Python 3.9+ |
| Framework | Streamlit |
| Key libraries | Pandas, Plotly Express, NumPy |
| Hosting | Streamlit Community Cloud (free tier) |
| Data storage | Google Cloud Storage (secure, access-controlled) |
| Data file | CSV (comma-separated values) |
| Browser support | Chrome, Edge, Firefox, Safari (latest versions) |
| Mobile support | Yes — responsive layout, sidebar collapses on small screens |
| Authentication | None for viewers (public access); GCS access controlled by service account |
| Data export | CSV download (filtered view only) |

---

## Accessibility

This dashboard has been designed with accessibility in mind:

- Charts include hover tooltips for screen reader support
- Colour schemes have been reviewed against WCAG 2.1 accessibility guidelines
- The layout stacks vertically on mobile devices for ease of reading
- No specialist software or plugins are required to access the dashboard

---

## Contact and Support

This is a **prototype dashboard**. For questions, feedback or data update requests, please contact the developer.

---

## Data Attribution

Data source: UCAS (2026) *2026 cycle applicant figures — 15 October deadline*. Available at: https://www.ucas.com

This dataset is compiled from open data sources already in the public domain. It is free to download, reuse and distribute with attribution to the original source.

---

*README version 1.1 | June 2026*
