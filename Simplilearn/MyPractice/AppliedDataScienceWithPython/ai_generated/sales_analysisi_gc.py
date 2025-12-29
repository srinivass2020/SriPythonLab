"""
Project statement:
AAL, established in 2000, is a well-known brand in Australia, particularly recognized for its clothing business. It has opened branches in various states, metropolises, and tier-1 and tier-2 cities across the country.
The brand caters to all age groups, from kids to the elderly.
Currently experiencing a surge in business, AAL is actively pursuing expansion opportunities. To facilitate informed investment decisions, the CEO has assigned the responsibility to the head of AAL’s sales and marketing (S&M) department. The specific tasks include:
1)	Identify the states that are generating the highest revenues.
2)	Develop sales programs for states with lower revenues. The head of sales and marketing has requested your assistance with this task.
Analyze the sales data of the company for the fourth quarter in Australia, examining it on a state-by-state basis. Provide insights to assist the company in making data-driven decisions for the upcoming year.
*Enclosed is the CSV (AusApparalSales4thQrt2020.csv) file that covers the said data.

Perform the following steps:
As a data scientist, you must perform the following steps on the enclosed data:
1.	Data wrangling
2.	Data analysis
3.	Data visualization
4.	Report generation
1.	Data wrangling
a.	Ensure that the data is clean and free from any missing or incorrect entries.
○	Inspect the data manually to identify missing or incorrect information using the functions isna() and notna().
b.	Based on your knowledge of data analytics, include your recommendations for treating missing and incorrect data (dropping the null values or filling them).
c.	Choose a suitable data wrangling technique—either data standardization or normalization. Execute the preferred normalization method and present the resulting data. (Normalization is the preferred approach for this problem.)
d.	Share your insights regarding the application of the GroupBy() function for either data chunking or merging, and offer a recommendation based on your analysis.
2.	Data analysis
a.	Perform descriptive statistical analysis on the data in the Sales and Unit columns. Utilize techniques such as mean, median, mode, and standard deviation for this analysis.
b.	Identify the group with the highest sales and the group with the lowest sales based on the data provided.
c.	Identify the group with the highest and lowest sales based on the data provided.
d.	Generate weekly, monthly, and quarterly reports to document and present the results of the analysis conducted.
(Use suitable libraries such as NumPy, Pandas, and SciPy for performing the analysis.)
3.	Data visualization
a.	Use suitable data visualization libraries to construct a dashboard for the head of sales and marketing. The dashboard should encompass key parameters:
o	State-wise sales analysis for different demographic groups (kids, women, men, and seniors).
o	Group-wise sales analysis (Kids, Women, Men, and Seniors) across various states.
o	Time-of-the-day analysis: Identify peak and off-peak sales periods to facilitate strategic planning for S&M teams. This information aids in designing programs like hyper-personalization and Next Best Offers to enhance sales.
b.	Ensure the visualization is clear and accessible for effective decision-making by the head of sales and marketing (S&M).
The dashboard must contain daily, weekly, monthly, and quarterly charts.
(Any visualization library can be used for this purpose. However, since statistical analysis is being done, Seaborn is preferred.)
c.	Include your recommendation and indicate why you are choosing the recommended visualization package.
4.	Report generation
a)	Use JupyterLab Notebook for generating reports, which includes tasks such as data wrangling, analysis, and visualization. Please note that JupyterLab enables you to integrate code seamlessly with graphs and plots.
b)	Use Markdown in suitable places while presenting your report.
c)	Use suitable graphs, plots, and analysis reports in the report, along with recommendations. Note that various aspects of analysis require different graphs and plots.
○	Use a box plot for descriptive statistics.
○	Use the Seaborn distribution plot for any other statistical plotting.
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

DATA_PATH = r'/Simplilearn/resources/AusApparalSales4thQrt2020.csv'
def load_data(path=DATA_PATH):
    return pd.read_csv(path)

def check_missing_values(df):
    """
    Report missing values, drop rows missing critical columns, fill others.
    Returns the cleaned dataframe.
    """
    # summary
    missing_counts = df.isna().sum()
    missing_pct = (df.isna().mean() * 100).round(2)
    summary = pd.DataFrame({'missing_count': missing_counts, 'missing_pct': missing_pct})
    print("\nMissing values summary:")
    print(summary[summary['missing_count'] > 0])

    # Drop rows missing critical fields
    critical = [c for c in ['Date', 'Sales'] if c in df.columns]
    if critical:
        before = len(df)
        df = df.dropna(subset=critical).reset_index(drop=True)
        after = len(df)
        if before != after:
            print(f"Dropped {before - after} rows missing critical columns: {critical}")

    # Fill numeric columns with median
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if df[col].isna().any():
            med = df[col].median()
            df[col] = df[col].fillna(med)
            print(f"Filled NaNs in numeric column `{col}` with median = {med}")

    # Fill object (categorical) columns with mode or 'Unknown'
    obj_cols = df.select_dtypes(include=['object']).columns
    for col in obj_cols:
        if df[col].isna().any():
            mode = df[col].mode()
            fill_val = mode[0] if not mode.empty else 'Unknown'
            df[col] = df[col].fillna(fill_val)
            print(f"Filled NaNs in categorical column `{col}` with `{fill_val}`")
    return df

def inspect_data(df):
    print("Dataframe Info:")
    print(df.info())
    print("\nDataframe Head:")
    print(df.head())
    print("\nDataframe Description:")
    print(df.describe(include='all'))
    print("\nUnit and Sales Mode :")
    print(df[['Unit','Sales']].mode())

    # Ensure string columns are stripped of whitespace
    str_cols = df.select_dtypes(include=['object']).columns

    for col in str_cols:
        df[col] = df[col].str.strip()

    # Ensure Date is datetime; coerce invalid entries to NaT
    df['Date'] = pd.to_datetime(df.get('Date', None), errors='coerce')
    num_invalid_dates = df['Date'].isna().sum()
    if num_invalid_dates:
        print(f"\nFound {num_invalid_dates} invalid/missing Date values. Dropping those rows.")
        df = df.dropna(subset=['Date']).reset_index(drop=True)

    # Add time-related columns if Date available
    if 'Date' in df.columns and not df['Date'].isna().all():
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Week'] = df['Date'].dt.isocalendar().week
        df['Quarter'] = df['Date'].dt.quarter
        print(df['Year'].value_counts())
        print(df['Month'].value_counts())
        print(df['Week'].value_counts())
        print(df['Quarter'].value_counts())

    return df

def visualize_data(df):
    # Ensure Sales is numeric
    if 'Sales' in df.columns:
        df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce').fillna(0)
    else:
        raise ValueError("`Sales` column not found in dataframe. Available columns: " + ", ".join(df.columns))

    # Canonicalize demographic column name (allow variations like 'Demographic Group', 'Group', etc.)
    normalized = {col.lower().replace(" ", "").replace("_", ""): col for col in df.columns}
    preferred_keys = ['demographicgroup', 'demographicgroup', 'demographic', 'group', 'segment']
    dem_col = None
    for key in preferred_keys:
        if key in normalized:
            dem_col = normalized[key]
            break
    if dem_col is None:
        # try any column name containing 'demograph' or 'group'
        for k, v in normalized.items():
            if 'demograph' in k or 'group' in k:
                dem_col = v
                break

    if dem_col is None:
        print("Could not find a demographic/group column. Available columns:")
        print(list(df.columns))
        raise ValueError("Missing demographic/group column for plotting.")

    # Create a standard column name for plotting
    if dem_col != 'DemographicGroup':
        df['DemographicGroup'] = df[dem_col]

    # State-wise sales analysis
    if 'State' in df.columns:
        plt.figure(figsize=(12, 6))
        sns.barplot(x='State', y='Sales', data=df, estimator=np.sum)
        plt.title('State-wise Sales Analysis')
        plt.xticks(rotation=45)
        plt.show()
    else:
        print("`State` column not found; skipping state-wise plot.")

    # Group-wise sales analysis
    plt.figure(figsize=(12, 6))
    sns.barplot(x='DemographicGroup', y='Sales', data=df, estimator=np.sum)
    plt.title('Group-wise Sales Analysis')
    plt.xticks(rotation=45)
    plt.show()

    # Time-of-the-day analysis (only if Time column exists)
    if 'Time' in df.columns:
        # Safely parse times; ignore invalid entries
        df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
        if df['Hour'].notna().any():
            plt.figure(figsize=(12, 6))
            sns.lineplot(x='Hour', y='Sales', data=df, estimator=np.sum)
            plt.title('Time-of-the-day Sales Analysis')
            plt.xticks(range(0, 24))
            plt.show()
        else:
            print("No valid Time values for hourly plot; skipping time-of-day analysis.")
    else:
        print("`Time` column not found; skipping time-of-day analysis.")

def main():
    df = load_data()
    df = check_missing_values(df)
    df = inspect_data(df)
    visualize_data(df)

if __name__ == "__main__":
    main()