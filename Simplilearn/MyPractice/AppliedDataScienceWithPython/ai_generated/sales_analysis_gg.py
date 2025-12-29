import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_and_wrangle_data(file_path):
    """
    Loads the CSV data and performs cleaning and wrangling steps.
    """
    print("--- Loading and Wrangling Data ---")
    try:
        df = pd.read_csv(file_path)

        # 1. Clean Column Names: Remove any leading/trailing whitespace
        df.columns = df.columns.str.strip()

        # 2. Clean String Data: Remove whitespace from object columns (State, Group, Time)
        #    Example: ' WA' -> 'WA'
        str_cols = df.select_dtypes(include=['object']).columns
        for col in str_cols:
            df[col] = df[col].str.strip()

        # 3. Date Conversion: Convert 'Date' column to datetime objects
        #    Format appears to be '1-Oct-20' -> '%d-%b-%y'
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

        # 4. Missing Value Check
        missing_values = df.isnull().sum().sum()
        if missing_values > 0:
            print(f"Warning: Found {missing_values} missing values. Handling them...")
            # For this specific dataset, we drop them, but imputation could be used
            df = df.dropna()
        else:
            print("Data is clean: No missing values found.")

        # 5. Normalization and Standardization (as per problem statement)
        #    Normalization (Min-Max Scaling): Squashes values between 0 and 1
        min_sales = df['Sales'].min()
        max_sales = df['Sales'].max()
        df['Sales_Normalized'] = (df['Sales'] - min_sales) / (max_sales - min_sales)
        print(f"Sales Normalized: Min={df['Sales_Normalized'].min()}, Max={df['Sales_Normalized'].max()}")

        #    Standardization (Z-Score): Centers around 0 with unit variance
        mean_sales = df['Sales'].mean()
        std_sales = df['Sales'].std()
        df['Sales_Standardized'] = (df['Sales'] - mean_sales) / std_sales
        print(f"Sales Standardized: Mean={df['Sales_Standardized'].mean():.2f}, StdDev={df['Sales_Standardized'].std():.2f}")

        print("Data wrangling complete.\n")
        return df

    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def analyze_data(df):
    """
    Performs data analysis to identify high/low revenue states and other trends.
    """
    print("--- Data Analysis Report ---")

    # 1. State-wise Analysis
    state_group = df.groupby('State')['Sales'].sum().sort_values(ascending=False)
    highest_state = state_group.idxmax()
    lowest_state = state_group.idxmin()

    print(f"Total Sales by State:\n{state_group}")
    print(f"\nState with Highest Revenue: {highest_state} (${state_group.max():,.2f})")
    print(f"State with Lowest Revenue:  {lowest_state} (${state_group.min():,.2f})")

    # 2. Group-wise Analysis
    group_sales = df.groupby('Group')['Sales'].sum().sort_values(ascending=False)
    print(f"\nSales by Demographic Group:\n{group_sales}")

    # 3. Time-of-Day Analysis
    time_sales = df.groupby('Time')['Sales'].sum().sort_values(ascending=False)
    print(f"\nSales by Time of Day:\n{time_sales}")

    #4. Date wise Sales Trend
    date_sales = df.groupby('Date')['Sales'].sum().sort_index()
    print(f"\nSales Trend Over Dates:\n{date_sales}")

    # Recommendations
    print("\n--- Recommendations ---")
    print(f"1. Focus expansion and inventory optimization in {highest_state} as it drives the most revenue.")
    print(
        f"2. Develop specific sales programs and marketing campaigns for {lowest_state}, WA, and NT to boost performance.")
    print("3. Sales are relatively balanced across demographic groups, suggesting a broad market appeal.")

    return state_group, group_sales, time_sales , date_sales


def visualize_data(df, state_sales, group_sales, time_sales):
    """
    Generates and displays visualizations for the analysis.
    """
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig = plt.figure(figsize=(18, 12))
    fig.suptitle('Australian Apparel Sales Analysis (4th Qtr 2020)', fontsize=16)

    # Plot 1: Sales by State
    ax1 = fig.add_subplot(2, 2, 1)
    sns.barplot(x=state_sales.index, y=state_sales.values, ax=ax1, palette="viridis")
    ax1.set_title('Total Sales by State')
    ax1.set_ylabel('Sales (AUD)')
    ax1.set_xlabel('State')

    # Plot 2: Sales by Group
    ax2 = fig.add_subplot(2, 2, 2)
    sns.barplot(x=group_sales.index, y=group_sales.values, ax=ax2, palette="magma")
    ax2.set_title('Total Sales by Demographic Group')
    ax2.set_ylabel('Sales (AUD)')

    # Plot 3: Sales by Time of Day
    ax3 = fig.add_subplot(2, 2, 3)
    # Pie chart for time of day
    ax3.pie(time_sales, labels=time_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    ax3.set_title('Sales Distribution by Time of Day')

    # Plot 4: Weekly/Daily Sales Trend
    ax4 = fig.add_subplot(2, 2, 4)
    # Resample to weekly sales sum to see trend clearly
    daily_sales = df.groupby('Date')['Sales'].sum()
    sns.lineplot(data=daily_sales, ax=ax4, color='blue', marker='o')
    ax4.set_title('Daily Sales Trend (Oct - Dec)')
    ax4.set_ylabel('Total Daily Sales')
    plt.xticks(rotation=45)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for suptitle

    print("\nGenerating visualizations...")
    plt.show()


def main():
    file_path = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\AusApparalSales4thQrt2020.csv'

    # Step 1: Data Wrangling
    df = load_and_wrangle_data(file_path)

    if df is not None:
        # Step 2: Data Analysis & Reporting
        state_sales, group_sales, time_sales ,date_sales = analyze_data(df)

        # Step 3: Visualization
        visualize_data(df, state_sales, group_sales, time_sales)


if __name__ == "__main__":
    main()