"""
sales_analysis.py

Project: AAL Australia Apparel Sales Analysis – Q4 2020
Author: Data Science Team
Description:
This module performs data wrangling, statistical analysis, visualization,
and reporting support for AAL's fourth-quarter sales data in Australia.
"""

# =========================
# Import Required Libraries
# =========================
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Set visualization style
sns.set(style="whitegrid")


# =========================
# Data Loading
# =========================
def load_data(file_path: str) -> pd.DataFrame:
    """
    Load the sales CSV file into a Pandas DataFrame.

    Parameters:
        file_path (str): Path to the CSV file

    Returns:
        pd.DataFrame: Loaded sales data
    """
    return pd.read_csv(file_path)


# =========================
# Data Wrangling
# =========================
def inspect_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Inspect missing and non-missing values in the dataset.

    Parameters:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Summary of missing values per column
    """
    summary = pd.DataFrame({
        "Missing Values": df.isna().sum(),
        "Non-Missing Values": df.notna().sum()
    })
    return summary


def treat_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Treat missing or incorrect values in the dataset.

    Strategy:
    - Numerical columns: filled with median (robust to outliers)
    - Categorical columns: filled with mode

    Parameters:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Cleaned DataFrame
    """
    for col in df.columns:
        if df[col].dtype in ["int64", "float64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])
    return df


def normalize_sales_units(df: pd.DataFrame,
                           columns=("Sales", "Units")) -> pd.DataFrame:
    """
    Normalize Sales and Units columns using Min-Max Normalization.

    Rationale:
    Normalization ensures all numerical features are scaled between 0 and 1,
    improving comparability across states and demographic groups.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (tuple): Columns to normalize

    Returns:
        pd.DataFrame: DataFrame with normalized columns appended
    """
    scaler = MinMaxScaler()
    df[[f"{col}_Normalized" for col in columns]] = scaler.fit_transform(df[list(columns)])
    return df


def groupby_insights():
    """
    Provide insights on GroupBy usage.

    GroupBy is recommended for:
    - Aggregating sales at state, demographic, and time levels
    - Identifying high and low-performing regions
    - Creating weekly, monthly, and quarterly summaries
    """
    insight = (
        "GroupBy() is essential for chunking data by State, Group, and Time.\n"
        "It enables efficient aggregation (sum, mean) and supports\n"
        "state-wise, group-wise, and temporal performance comparisons."
    )
    print(insight)


# =========================
# Data Analysis
# =========================
def descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform descriptive statistical analysis on Sales and Units.

    Metrics:
    - Mean
    - Median
    - Mode
    - Standard Deviation

    Parameters:
        df (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Descriptive statistics
    """
    stats_dict = {
        "Mean": df[["Sales", "Units"]].mean(),
        "Median": df[["Sales", "Units"]].median(),
        "Mode": df[["Sales", "Units"]].mode().iloc[0],
        "Standard Deviation": df[["Sales", "Units"]].std()
    }
    return pd.DataFrame(stats_dict)


def highest_lowest_sales_by_group(df: pd.DataFrame,
                                  group_col: str) -> pd.DataFrame:
    """
    Identify highest and lowest sales by a grouping column.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        group_col (str): Column name to group by (e.g., 'State', 'Group')

    Returns:
        pd.DataFrame: Aggregated sales sorted by Sales
    """
    result = (
        df.groupby(group_col)["Sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return result


def generate_time_reports(df: pd.DataFrame,
                          date_col: str = "Date") -> dict:
    """
    Generate weekly, monthly, and quarterly sales reports.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        date_col (str): Date column name

    Returns:
        dict: Dictionary containing weekly, monthly, and quarterly reports
    """
    df[date_col] = pd.to_datetime(df[date_col])

    reports = {
        "Weekly": df.groupby(pd.Grouper(key=date_col, freq="W"))["Sales"].sum(),
        "Monthly": df.groupby(pd.Grouper(key=date_col, freq="M"))["Sales"].sum(),
        "Quarterly": df.groupby(pd.Grouper(key=date_col, freq="Q"))["Sales"].sum()
    }
    return reports


# =========================
# Data Visualization
# =========================
def plot_boxplot_sales_units(df: pd.DataFrame):
    """
    Create box plots for Sales and Units for descriptive statistics.
    """
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df[["Sales", "Units"]])
    plt.title("Box Plot – Sales and Units")
    plt.show()


def plot_state_group_sales(df: pd.DataFrame):
    """
    Visualize state-wise sales across demographic groups.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(x="State", y="Sales", hue="Group", data=df, estimator=np.sum)
    plt.title("State-wise Sales by Demographic Group")
    plt.xticks(rotation=45)
    plt.show()


def plot_time_of_day_sales(df: pd.DataFrame):
    """
    Analyze peak and off-peak sales by time of day.

    Assumes a column 'TimeOfDay' exists (Morning, Afternoon, Evening, Night).
    """
    plt.figure(figsize=(8, 5))
    sns.barplot(x="TimeOfDay", y="Sales", data=df, estimator=np.sum)
    plt.title("Time-of-Day Sales Analysis")
    plt.show()


def visualization_recommendation():
    """
    Provide visualization library recommendation.
    """
    recommendation = (
        "Seaborn is recommended due to its statistical plotting capabilities,\n"
        "built-in themes, and seamless integration with Pandas DataFrames.\n"
        "It is ideal for dashboards, distribution plots, and comparative analysis."
    )
    print(recommendation)


# =========================
# Main Execution
# =========================
def main():
    """
    Main execution pipeline for sales analysis.
    """
    file_path = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\AusApparalSales4thQrt2020.csv'

    # Load data
    df = load_data(file_path)

    # Data wrangling
    print(inspect_missing_data(df))
    df = treat_missing_data(df)
    df = normalize_sales_units(df)
    groupby_insights()

    # Data analysis
    print(descriptive_statistics(df))
    print(highest_lowest_sales_by_group(df, "State"))
    print(highest_lowest_sales_by_group(df, "Group"))

    # Visualization
    plot_boxplot_sales_units(df)
    plot_state_group_sales(df)
    visualization_recommendation()


if __name__ == "__main__":
    main()
