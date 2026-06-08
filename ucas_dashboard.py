# UCAS Dashboard using Streamlit

# 1. Data Preparation

# 1.1 Prepare workstation
# Import required libraries and packages
import os
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
# Inject custom CSS to hide the top-right toolbar, github icons, and status widget
st.markdown(
    """
    <style>
    div[data-testid="stToolbar"] {
        display: none !important;
    }
    .stAppDeployButton {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
import pandas as pd
import numpy as np
import plotly.express as px
# Set working directory to the folder containing this script (works locally and on Streamlit Cloud)
desired_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(desired_directory)

# 1.2 Import dataset
# Load the UCAS applications data
df = pd.read_csv(os.path.join(desired_directory, 'Reapplication status.csv'))

# 1.3 Clean the data
# Function to clean the data
def clean_data(df):
    """"
    This function uses the df as input and performs the following cleaning steps:
    1. Strip whitespace and remove line breaks from column names, and convert them to title case.
    2. Ensure 'Applicants' column is numeric, coercing errors to NaN.
    3. Convert the 'Year' column to an integer year (e.g. 2018) for use in Streamlit visualisations.
    4. Drop rows that contain the value 'All' in any column.
    5. Convert non-numeric values to title case for consistency and visual appeal.
    6. If a string value equals the word 'And', convert it to lowercase
    7. If a string value contains 'Uk', replace with 'UK'
    8. If a string value contains 'Eu', replace with 'EU'
    9. Drop rows that contain null or missing values.
    The function uses try/except statements to catch and print any errors that occur during the cleaning process.
    """
    try:
        # Step 1: Clean column names
        df.columns = df.columns.str.strip().str.replace('\n', '').str.title()
        
        # Step 2: Ensure 'Applicants' column is numeric
        if 'Applicants' in df.columns:
            df['Applicants'] = pd.to_numeric(df['Applicants'], errors='coerce')
        else:
            return None
        
        # Step 3: Ensure 'Year' column is numeric
        if 'Year' in df.columns:
            df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        else:
            return None

        # Step 4: Drop rows containing 'All'
        df = df[~df.apply(lambda row: row.astype(str).str.contains('All').any(), axis=1)]

        # Step 5: Convert non-numeric values to title case for consistency and visual appeal
        df = df.map(lambda x: x.title() if isinstance(x, str) else x)

        # Step 6: Convert 'And' to lowercase
        df = df.map(lambda x: x.replace('And', 'and') if isinstance(x, str) else x)

        # Step 7: Replace 'Uk' with 'UK' anywhere in a string (e.g. 'Rest Of Uk' -> 'Rest Of UK')
        df = df.map(lambda x: x.replace('Uk', 'UK') if isinstance(x, str) else x)

        # Step 8: Replace 'Eu' with 'EU' anywhere in a string (e.g. 'Other Eu' -> 'Other EU')
        df = df.map(lambda x: x.replace('Eu', 'EU') if isinstance(x, str) else x)
        
        # Step 9: Drop rows with null or missing values
        df = df.dropna()
        
        return df
    
    except Exception as e:
        print(f"The data file contains errors. Please check and try again: {e}")
        return None

# Apply the cleaning function.
df = clean_data(df)
if df is None:
    st.error("Data cleaning failed. Please check the CSV file and try again.")
    st.stop()

# 1.4 Create simpler categories for visualisations
# Function to create simpler categories for visualisations
def simpler_cats(df):
    """"
    This function uses the df as input and adds new columns 
    that simplify the Age Group, Gender and Domicile categories. 
    The function uses try/except statements to catch and print any 
    errors that occur during the cleaning process.
    """
    try:
        # New Category based Age Group: values are 'Mature' or 'Traditional'.
        if 'Age Group' in df.columns:
            df['Maturity'] = df['Age Group'].apply(lambda x: 'Mature' if x in ['35 and Over', '30 - 34', '25 - 29'] else 'Traditional')
        else:
            print("Error: 'Age Group' column not found.")
            return None

        # New Category based on Gender: values are 'Male', 'Female' or 'Other'.
        if 'Gender' in df.columns:
            df['Male/Female'] = df['Gender'].apply(lambda x: 'Male' if 'Man' in x else ('Female' if 'Woman' in x else 'Other'))
        else:
            print("Error: 'Gender' column not found.")
            return None
        
        # New Category based on Domicile: values are 'UK', 'EU', 'Not-EU'.
        if 'Domicile' in df.columns:
            uk_regions = ['England', 'Scotland', 'Northern Ireland', 'Wales']
            df['Location'] = df['Domicile'].apply(lambda x: 'UK' if any(region in x for region in uk_regions) else ('EU' if 'EU' in x else 'Not-EU'))
        else:
            print("Error: 'Domicile' column not found.")
            return None

        return df
    
    except Exception as e:
        print(f"The data file contains errors. Please check and try again: {e}")
        return None

# Apply the simpler categories function.
df = simpler_cats(df)
if df is None:
    st.error("Failed to create categories. Please check the CSV file and try again.")
    st.stop()

# 2. To meet assignment requirements, remove records where the year is 2017, 2018, 2019 or 2020.
df = df[~df['Year'].isin([2017, 2018, 2019, 2020])]

# 3. Create Streamlit dashboard and visualisations

# Set the title of the dashboard
st.title("UCAS Dashboard")
st.write("This dashboard explores recent UK university application trends. Use the dropdown menu to view applications by student age, gender, and domicile (country the student applied from)).")
st.write("Use the filters to explore your findings.")
st.write("Data source: [UCAS 2026 Applicant Cycle](https://www.ucas.com/data-and-analysis/undergraduate-statistics-and-reports/ucas-undergraduate-releases/applicant-releases-for-2026-cycle/2026-cycle-applicant-figures-15-october-deadline).")

# 4. Add text with dynamic content that updates based on user selections

total_applications = sum(df['Applicants'])

# Legend selector: choose which category to split the chart by
legend_options = {
    'Age Group': 'Age Group',
    'Gender': 'Gender',
    'Domicile': 'Domicile',
}
st.sidebar.markdown("### Choose a metric")
selected_legend = st.sidebar.selectbox("", list(legend_options.keys()))
legend_col = legend_options[selected_legend]

# Sub-filters: show filters for all dimensions except the selected legend
st.sidebar.markdown("---")
st.sidebar.markdown("**Filter your chart**")

# Define which sub-filters apply to each legend selection
sub_filter_options = {
    'Age Group': [('Maturity', 'Maturity')],
    'Gender': [('Male/Female', 'Male/Female')],
    'Domicile':  [('Domicile', 'Domicile')],
}

# Build the filtered dataframe based on user sub-filter selections
filtered_df = df.copy()
for label, col in sub_filter_options[selected_legend]:
    unique_vals = sorted(filtered_df[col].dropna().unique().tolist())
    selected_vals = st.sidebar.multiselect(label, unique_vals, default=unique_vals)
    if selected_vals:
        filtered_df = filtered_df[filtered_df[col].isin(selected_vals)]

# Group by Year and the selected legend column, then pivot so each legend value becomes a column
# Convert Year to string to avoid comma formatting on x-axis (e.g. 2,018)
chart_df = (
    filtered_df.groupby(['Year', legend_col])['Applicants']
    .sum()
    .unstack(legend_col)
    .fillna(0)
)
chart_df.index = chart_df.index.astype(str)

# KPI summary cards
yearly_totals = filtered_df.groupby('Year')['Applicants'].sum().sort_index()
total_filtered = int(filtered_df['Applicants'].sum())

if len(yearly_totals) >= 2:
    latest_year = yearly_totals.index[-1]
    prev_year = yearly_totals.index[-2]
    latest_total = int(yearly_totals.iloc[-1])
    prev_total = int(yearly_totals.iloc[-2])
    yoy_change = (latest_total - prev_total) / prev_total * 100 if prev_total > 0 else 0
    yoy_abs = latest_total - prev_total
else:
    latest_year = yearly_totals.index[-1] if len(yearly_totals) > 0 else "N/A"
    latest_total = int(yearly_totals.iloc[-1]) if len(yearly_totals) > 0 else 0
    yoy_change = None
    yoy_abs = None

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric("Total Applicants (filtered)", f"{total_filtered:,}")
kpi2.metric(f"Applicants in {latest_year}", f"{latest_total:,}")
if yoy_change is not None:
    kpi3.metric(
        label=f"Year-on-Year Change ({prev_year} → {latest_year})",
        value=f"{yoy_change:+.1f}%",
        delta=f"{yoy_abs:+,} applicants"
    )
else:
    kpi3.metric("Year-on-Year Change", "N/A")

st.markdown("---")

# Line chart: trend over time
st.subheader(f"Trend Over Time by: '{selected_legend}'")
if chart_df.empty:
    st.warning("No data matches the selected filters.")
else:
    fig_line = px.line(
        chart_df,
        markers=True,
        labels={'value': 'Applicants', 'index': 'Year', 'variable': selected_legend}
    )
    st.plotly_chart(fig_line, use_container_width=True)

# Bar chart: year-on-year grouped comparison
st.subheader(f"Year-on-Year Comparison by: '{selected_legend}'")
if chart_df.empty:
    st.warning("No data matches the selected filters.")
else:
    bar_df = filtered_df.groupby(['Year', legend_col])['Applicants'].sum().reset_index()
    bar_df['Year'] = bar_df['Year'].astype(str)
    fig_bar = px.bar(
        bar_df,
        x='Year',
        y='Applicants',
        color=legend_col,
        barmode='group',
        labels={'Applicants': 'Applicants', 'Year': 'Year', legend_col: selected_legend}
    )
    st.plotly_chart(fig_bar, use_container_width=True)

st.markdown("---")

# Data table with export
st.subheader(f"Data Table: '{selected_legend}'")
if chart_df.empty:
    st.warning("No data matches the selected filters.")
else:
    st.dataframe(chart_df.style.format("{:,.0f}"))

    # Export button: convert filtered table to CSV and offer as download
    csv = chart_df.reset_index().to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download table as CSV",
        data=csv,
        file_name=f"ucas_applications_by_{selected_legend.lower().replace(' ', '_')}.csv",
        mime="text/csv"
    )
