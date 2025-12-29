"""
sales_analysis.py
-----------------
Sales Analysis for AAL (Australian Apparel Limited)

This module performs:
1. Data wrangling (cleaning, inspection, normalization)
2. Data analysis (descriptive statistics, aggregation)
3. Data visualization (state-wise, group-wise, time-based insights)

Dataset:
AusApparalSales4thQrt2020.csv

Author: Data Science Team
"""

# ==========================
# Imports
# ==========================
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


# ==========================
# Configuration
# ==========================
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


# ==========================
# Data Loading
# ==========================
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the sales dataset from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded sales data.
    """
    return pd.read_csv(file_path)


# ==========================
# Data Wrangling
# ==========================
def inspect_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Inspect missing values in the dataset.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Summary of missing values per column.
    """
    return df.isna().sum()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset by handling missing or incorrect values.

    Strategy:
    - Drop rows with missing Sales or Units (critical fields)
    - Fill other missing categorical values with mode

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Cleaned dataset.
    """
    df = df.dropna(subset=["Sales", "Units"])

    for col in df.select_dtypes(include="object").columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    return df


def normalize_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Apply Min-Max normalization to selected numeric columns.

    Normalization is preferred because it scales values
    between 0 and 1, making comparison easier across states.

    Formula:
    (x - min) / (max - min)

    Parameters
    ----------
    df : pd.DataFrame
    columns : list

    Returns
    -------
    pd.DataFrame
        DataFrame with normalized columns added.
    """
    for col in columns:
        df[col + "_Normalized"] = (df[col] - df[col].min()) / (
            df[col].max() - df[col].min()
        )
    return df


# ==========================
# GroupBy Insights
# ==========================
def state_wise_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total sales by state.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        State-wise total sales.
    """
    return df.groupby("State")["Sales"].sum().sort_values(ascending=False)


def group_wise_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate total sales by demographic group.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Group-wise total sales.
    """
    return df.groupby("Group")["Sales"].sum().sort_values(ascending=False)


# ==========================
# Descriptive Statistics
# ==========================
def descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform descriptive statistical analysis on Sales and Units.

    Statistics included:
    - Mean
    - Median
    - Mode
    - Standard Deviation

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    pd.DataFrame
        Statistical summary.
    """
    stats_df = pd.DataFrame({
        "Mean": df[["Sales", "Units"]].mean(),
        "Median": df[["Sales", "Units"]].median(),
        "Mode": df[["Sales", "Units"]].mode().iloc[0],
        "Std_Dev": df[["Sales", "Units"]].std()
    })
    return stats_df


# ==========================
# Time-Based Analysis
# ==========================
def time_based_reports(df: pd.DataFrame) -> dict:
    """
    Generate daily, weekly, monthly, and quarterly sales reports.

    Parameters
    ----------
    df : pd.DataFrame

    Returns
    -------
    dict
        Dictionary containing aggregated reports.
    """
    df["Date"] = pd.to_datetime(df["Date"])

    reports = {
        "Daily": df.groupby(df["Date"].dt.date)["Sales"].sum(),
        "Weekly": df.groupby(df["Date"].dt.to_period("W"))["Sales"].sum(),
        "Monthly": df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum(),
        "Quarterly": df.groupby(df["Date"].dt.to_period("Q"))["Sales"].sum()
    }

    return reports


# ==========================
# Visualization
# ==========================
def plot_state_group_sales(df: pd.DataFrame):
    """
    Plot state-wise sales across demographic groups.

    Parameters
    ----------
    df : pd.DataFrame
    """
    sns.barplot(data=df, x="State", y="Sales", hue="Group")
    plt.title("State-wise Sales by Demographic Group")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_group_sales(df: pd.DataFrame):
    """
    Plot group-wise sales distribution.

    Parameters
    ----------
    df : pd.DataFrame
    """
    sns.boxplot(data=df, x="Group", y="Sales")
    plt.title("Sales Distribution by Group")
    plt.show()


def plot_time_of_day_sales(df: pd.DataFrame):
    """
    Analyze peak and off-peak sales based on time of day.

    Parameters
    ----------
    df : pd.DataFrame
    """
    df["Hour"] = pd.to_datetime(df["Time"]).dt.hour
    sns.lineplot(data=df, x="Hour", y="Sales", estimator="sum")
    plt.title("Time-of-Day Sales Analysis")
    plt.xlabel("Hour of Day")
    plt.ylabel("Total Sales")
    plt.show()


# ==========================
# Main Execution
# ==========================
def main():
    """
    Main execution pipeline for sales analysis.
    """
    file_path = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\AusApparalSales4thQrt2020.csv'

    df = load_data(file_path)

    print("Missing Data Summary:")
    print(inspect_missing_data(df))

    df = clean_data(df)

    df = normalize_columns(df, ["Sales", "Units"])

    print("\nDescriptive Statistics:")
    print(descriptive_statistics(df))

    print("\nState-wise Sales:")
    print(state_wise_sales(df))

    print("\nGroup-wise Sales:")
    print(group_wise_sales(df))

    reports = time_based_reports(df)

    # Visualizations
    plot_state_group_sales(df)
    plot_group_sales(df)
    plot_time_of_day_sales(df)


if __name__ == "__main__":
    main()
