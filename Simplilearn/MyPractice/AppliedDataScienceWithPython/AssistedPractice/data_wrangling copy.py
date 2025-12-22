"""
### Problem Statement:
The complexity of the housing market can be overwhelming.
For a data scientist at a real estate company, the responsibility lies in analyzing housing data to
uncover insights into house prices.
The goal is to comprehend the elements influencing house prices and the
impact of various house features on their price. This understanding aids the
company in navigating the housing market more effectively and making well-informed decisions
when purchasing and selling houses.

Steps to Perform:
Understand the structure of the dataset, the types of variables, and any obvious issues in the data
Check for duplicate entries in the dataset and decide how to handle them
Identify and handle missing values. Decide whether to fill them in or drop them based on the context
Apply the necessary transformations to the variables. This could include scaling numerical variables
or encoding categorical variables
find all the columns that are int and float in your dataset.  Those are the main ones to focus on to find skewness.
After doing that, go over the object columns to see if any of them contain numeric variables but have incorrectly
fallen into object datatype
For continuous variables, consider creating bins to turn them into categorical variables.
For example, you can bin the YearBuilt feature into decades
Identify outliers in the dataset and decide on a strategy to handle them. You can use a box plot to
visualize outliers in features like LotArea or SalePrice
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
DATA_PATH = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\housing_data_datawrangle.csv'
def load_data(path=DATA_PATH):
    return pd.read_csv(path)
def check_duplicates(df):   
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        df = df.drop_duplicates()
    else:
        print("No duplicate entries found.")
    return df, duplicate_count
def handle_missing_values(df):
    missing_info = df.isnull().sum()
    for column, missing_count in missing_info.items():
        if missing_count > 0:
            if df[column].dtype == 'object':
                df[column].fillna(df[column].mode()[0], inplace=True)
            else:
                df[column].fillna(df[column].median(), inplace=True)
    return df, missing_info[missing_info > 0]
def transform_variables(df):
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df
def bin_year_built(df):
    df['YearBuiltBin'] = pd.cut(df['YearBuilt'], bins=range(1800, 2025, 10), right=False)
    return df
def identify_outliers(df, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f'Box plot for {column}')
    plt.show()
# Example usage:
if __name__ == "__main__":
    df = load_data()
    print("Initial Data Shape:", df.shape)
    
    df, duplicate_count = check_duplicates(df)
    print(f"Duplicates Removed: {duplicate_count}")
    
    df, missing_info = handle_missing_values(df)
    print("Missing Values Handled:\n", missing_info)
    
    df = transform_variables(df)
    print("Data Shape after Transformation:", df.shape)
    
    df = bin_year_built(df)
    print("YearBuilt Binned.")
    
    identify_outliers(df, 'LotArea')
    identify_outliers(df, 'SalePrice')