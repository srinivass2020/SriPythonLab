'''
Task: Data Processing and Statistical Analysis
• Import relevant Python libraries.
• Import the CSV file – NSMES1988new.csv into a dataframe.
• Perform memory analysis of the new dataframe and compare it with the memory of the
dataframe in the previous week and mark your comments.
• Perform the following operations on age and income columns. Multiply age by 10 and
income by 10000.
• Perform basic statistical analysis on the new dataframe and generate a brief report on
the outcome. Save the dataframe as NSMES1988updated.csv file in the local space for
possible future use.
• Invoke describe command on the dataframe and compare that with the basic statistical
analysis done in the previous step
Indicate which of the columns are not eligible for statistical analysis and indicate possible
datatype changes, and report.
• Make changes to the recommended file from previous step in the previous step, export it as
a new .csv file for possible future use (Optional).
'''
import pandas as pd
import numpy as np
DATA_PATH_NEW = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\NSMES1988new.csv'
DATA_PATH_UPDATED = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\NSMES1988updated.csv'
def load_data(path=DATA_PATH_NEW):
    return pd.read_csv(path)
def memory_analysis(df):
    mem_usage = df.memory_usage(deep=True).sum() / (1024 ** 2)  # in MB
    print(f"\nMemory usage of dataframe: {mem_usage:.2f} MB")
    return mem_usage
def process_columns(df):
    print("nProcessing 'age' and 'income' columns:")
    if 'age' in df.columns:
        df['age'] = df['age'] * 10
    if 'income' in df.columns:
        df['income'] = df['income'] * 10000
    print("Columns processed.\n",df['age'].head(3), df['income'].head(3))
def basic_statistical_analysis(df):
    stats = df.describe(include='all')
    print("\nBasic Statistical Analysis:")
    print(stats)
    return stats
def save_updated_data(df, path=DATA_PATH_UPDATED):
    df.to_csv(path, index=False)
    print(f"\nUpdated dataframe saved to {path}")
def identify_non_eligible_columns(df):
    non_eligible = []
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].nunique() < 2:
            non_eligible.append(col)
    print("\nNon-eligible columns for statistical analysis:")
    print(non_eligible)
    return non_eligible
def recommend_data_type_changes(df):
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
def main():
    df = load_data()
    memory_analysis(df)
    process_columns(df)
    basic_statistical_analysis(df)
    save_updated_data(df)
    identify_non_eligible_columns(df)
    recommend_data_type_changes(df)
if __name__ == "__main__":
    main()
#     memory_analysis(df)
#     process_columns(df)
#     basic_statistical_analysis(df)
#     save_updated_data(df)
#     identify_non_eligible_columns(df)
#     recommend_data_type_changes(df)
# if __name__ == "__main__":
#     main()


