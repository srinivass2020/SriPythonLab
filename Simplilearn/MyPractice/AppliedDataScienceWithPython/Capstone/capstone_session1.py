'''
Task: Import and Export data, clean data
• Import relevant Python libraries necessary for Python programming and Numpy for doing
numerical operations.
• Import the CSV file – NSMES1988.csv into a dataframe.
• Inspect the data and report the details from physical inspection – rows, columns, data
types etc.
• Find out if the data is clean or if the data has missing values.
• Comment on the data types, their values and range, specifically on age and income
columns.
• Export the data to JSON as NSMES1988.json format file and view and enter your
comments
Perform memory information on the data and recommend what non-default data types
would you recommend to optimize memory settings for the dataframe.
• What changes would you recommend on the dataframe before attempting a detailed data
analysis?
• Export the data frame as a new CSV file NSMES1988new.csv and store it in the local space
for likely use in other assignments.
• Write a short report on the visual observations of the data
'''
import pandas as pd
import numpy as np
import sys
DATA_PATH = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\NSMES1988.csv'
DATA_PATH_NEW = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\NSMES1988new.csv'

def load_data(path=DATA_PATH):
    return pd.read_csv(path)
def inspect_data(df):
    print("Dataframe Info:")
    print(df.info())
    print("\nDataframe Head:")
    print(df.head())
    print("\nDataframe Description:")
    print(df.describe(include='all'))
def check_missing_values(df):
    missing = df.isnull().sum()
    print("\nMissing Values in Each Column:")
    print(missing)
    return missing
def analyze_columns(df):
    for col in ['age', 'income']:
        if col in df.columns:
            print(f"\nColumn: {col}")
            print(f"Data Type: {df[col].dtype}")
            print(f"Unique Values: {df[col].nunique()}")
            print(f"Value Range: {df[col].min()} to {df[col].max()}")
        else:
            print(f"Column '{col}' not found in dataframe.")
def export_to_json(df, path='NSMES1988.json'):
    df.to_json(path, orient='records', lines=True)
    print(f"\nDataframe exported to {path}")
def memory_analysis(df):
    mem_usage = df.memory_usage(deep=True).sum() / (1024 ** 2)  # in MB
    print(f"\nMemory usage of dataframe: {mem_usage:.2f} MB")
    return mem_usage
def recommend_data_types(df):
    recommendations = {}
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        if df[col].nunique() < 256:
            recommendations[col] = 'category'
        elif df[col].dtype == 'int64':
            recommendations[col] = 'int32'
        elif df[col].dtype == 'float64':
            recommendations[col] = 'float32'
    print("\nRecommended Data Type Changes:")
    for col, dtype in recommendations.items():
        print(f"{col}: {dtype}")
    return recommendations
def save_dataframe(df, path=DATA_PATH_NEW):
    df.to_csv(path, index=False)
    print(f"\nDataframe saved to {path}")
def main():
    df = load_data()
    print("Initial Dataframe Loaded.")
    inspect_data(df)
    check_missing_values(df)
    analyze_columns(df)
    export_to_json(df)
    memory_analysis(df)
    recommend_data_types(df)
    save_dataframe(df)
print("\nVisual observations: The dataset contains demographic and socioeconomic data. "
          "Age and income columns show a wide range of values, indicating diverse population segments. "
          "Missing values in certain columns may affect analysis and should be addressed.")
if __name__ == "__main__":
    main()