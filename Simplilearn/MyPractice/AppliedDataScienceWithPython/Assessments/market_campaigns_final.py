"""
Marketing Campaigns

Problem scenario:
Marketing mix stands as a widely utilized concept in the execution of marketing strategies. It encompasses various facets within a comprehensive marketing plan, with a central focus on the four Ps of marketing: product, price, place, and promotion.

Problem objective:
As a data scientist, you must conduct exploratory data analysis and hypothesis testing to enhance your comprehension of the diverse factors influencing customer acquisition.

Data description:
The dataset aligns with the Four Ps of Marketing, categorizing variables to analyze consumer behavior. Product-related variables track spending across categories, while Price factors like income and deal-based purchases indicate affordability. Place covers shopping channels and web visits, reflecting purchase preferences. Promotion measures campaign engagement, complaints, and recency. Additionally, demographics support segmentation for personalized marketing. This structured approach helps businesses optimize products, pricing, distribution, and promotions for better customer engagement and market performance.

Steps to perform:

1.	After importing the data, examine variables such as Dt_Customer and Income to verify their accurate importation.

2.	There are missing income values for some customers. Conduct missing value imputation, considering that customers with similar education and marital status tend to have comparable yearly incomes, on average. It may be necessary to cleanse the data before proceeding. Specifically, scrutinize the categories of education and marital status for data cleaning.

3.	Create variables to represent the total number of children, age, and total spending.

a.	Derive the total purchases from the number of transactions across the three channels.

4.	Generate box plots and histograms to gain insights into the distributions and identify outliers. Implement outlier treatment as needed.

5.	Apply ordinal and one-hot encoding based on the various types of categorical variables.

6.	Generate a heatmap to illustrate the correlation between different pairs of variables.

7.	Test the following hypotheses:
a.	Older individuals may not possess the same level of technological proficiency and may, therefore, lean toward traditional in-store shopping preferences.
b.	Customers with children likely experience time constraints, making online shopping a more convenient option.
c.	Sales at physical stores may face the risk of cannibalization by alternative distribution channels.
d.	Does the United States significantly outperform the rest of the world in total purchase volumes?


8.	Use appropriate visualization to help analyze the following:
a.	Identify the top-performing products and those with the lowest revenue.
b.	Examine if there is a correlation between customers' age and the acceptance rate of the last campaign.
c.	Determine the country with the highest number of customers who accepted the last campaign.
d.	Investigate if there is a discernible pattern in the number of children at home and the total expenditure.
e.	Analyze the educational background of customers who lodged complaints in the last two years.

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def load_and_clean_data(filepath):
    """
    Loads data, cleans column names, converts types, and handles missing values.
    """
    print("--- Loading and Cleaning Data ---")
    df = pd.read_csv(filepath)

    # 1. Clean Column Names (remove whitespace)
    df.columns = df.columns.str.strip()

    # 2. Clean 'Income' column (remove '$', ',', and convert to float)
    #    Handle potential non-string types by forcing string first, then clean
    df['Income'] = df['Income'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    #    Replace 'nan' string with actual np.nan
    df['Income'] = df['Income'].replace('nan', np.nan).astype(float)

    # 3. Convert 'Dt_Customer' to datetime
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])

    # 4. Impute Missing Income Values

    #    Using median income based on Education and Marital_Status as requested
    print(f"Missing Income values before imputation: {df['Income'].isnull().sum()}")
    # Print rows that have Income Null before imputation
    print("Before Filling",df[df['Income'].isnull()][['Education', 'Marital_Status', 'Income']].head())
    # Collect and Print rwos of those Id's of Income Null rows before imputation
    df_ids_before = df[df['Income'].isnull()].index.tolist()
    #Print the rows of these Id's
    print(df.loc[df_ids_before][['Education', 'Marital_Status', 'Income']])
     # Impute using group median
    df['Income'] = df.groupby(['Education', 'Marital_Status'])['Income'].transform(lambda x: x.fillna(x.median()))
    print(f"Missing Income values after imputation: {df['Income'].isnull().sum()}")
    # Print rows that have Income Null after imputation
    print(df.loc[df_ids_before][['Education', 'Marital_Status', 'Income']])

    return df

def feature_engineering(df):
    """
    Creates new variables as per the problem statement.
    """
    print("\n--- Feature Engineering ---")

    # 1. Age (Assuming analysis year is 2014 based on data context)
    #    Using 2014 ensures ages are relevant to the campaign period.
    df['Age'] = 2014 - df['Year_Birth']

    # 2. Total Children
    df['Total_Children'] = df['Kidhome'] + df['Teenhome']

    # 3. Total Spending (Sum of all 'Mnt' columns)
    spending_cols = [col for col in df.columns if 'Mnt' in col]
    df['Total_Spending'] = df[spending_cols].sum(axis=1) # axis=1 for row-wise sum

    # 4. Total Purchases (Sum of all 'Num...Purchases' columns)
    purchase_cols = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumDealsPurchases']
    df['Total_Purchases'] = df[purchase_cols].sum(axis=1) # axis=1 for row-wise sum

    print("After Feature Engineering ",df.head())
    return df


def outlier_treatment(df):
    """
    Visualizes and treats outliers.
    # remove rows with Income considered outliers by the 1.5*IQR rule
    q1 = df['Income'].quantile(0.25)
    q3 = df['Income'].quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df = df[(df['Income'] >= lower) & (df['Income'] <= upper)]
    """
    print("\n--- Outlier Analysis ---")

    # Visualizing Age and Income
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    sns.boxplot(y=df['Age'])
    plt.title('Age Distribution')

    plt.subplot(1, 2, 2)
    sns.boxplot(y=df['Income'])
    plt.title('Income Distribution')
    
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reports\outliers_before.png')
    plt.close()  # Close to prevent display overlap

    # Treatment: Removing extreme outliers
    # Age > 100 is likely a data entry error
    # Income > 600,000 is likely an outlier based on typical distribution
    initial_count = len(df)
    df = df[df['Age'] < 100]
    df = df[df['Income'] < 600000]
    print(f"Removed {initial_count - len(df)} outliers.")

    return df


def encode_categorical(df):
    """
    Applies Ordinal and One-Hot Encoding.
    """
    print("\n--- Encoding Categorical Variables ---")

    # Ordinal Encoding for Education
    # Defining hierarchy: Basic < 2n Cycle < Graduation < Master < PhD
    education_map = {'Basic': 0, '2n Cycle': 1, 'Graduation': 2, 'Master': 3, 'PhD': 4}
    df['Education_Ordinal'] = df['Education'].map(education_map)

    # One-Hot Encoding for Marital_Status
    df = pd.get_dummies(df, columns=['Marital_Status'], prefix='Marital', drop_first=True)

    print ("Encoding Categorical \n" , df.head())

    return df


def analyze_hypotheses(df):
    """
    Tests the specific hypotheses mentioned in the problem statement.
    """
    print("\n--- Hypothesis Testing ---")

    # Hypothesis 1: Older individuals lean toward in-store shopping
    # Check correlation between Age and Store Purchases vs Web Purchases
    corr_age_store = df['Age'].corr(df['NumStorePurchases'])
    corr_age_web = df['Age'].corr(df['NumWebPurchases'])
    print(f"1. Age vs Store Purchases Correlation: {corr_age_store:.2f}")
    print(f"   Age vs Web Purchases Correlation:   {corr_age_web:.2f}")
    if corr_age_store > corr_age_web:
        print("   -> Support found: Older people correlate more with store purchases.")
    else:
        print("   -> No strong support found.")

    # Hypothesis 2: Customers with children lean toward online shopping
    # Check correlation between Total_Children and NumWebPurchases
    corr_kids_web = df['Total_Children'].corr(df['NumWebPurchases'])
    print(f"2. Children vs Web Purchases Correlation: {corr_kids_web:.2f}")
    if corr_kids_web > 0:
        print("   -> Support found: Positive correlation between kids and web purchases.")

    # Hypothesis 3: Cannibalization (Store vs Other Channels)
    # Check correlation between Store Purchases and (Web + Catalog)
    other_channels = df['NumWebPurchases'] + df['NumCatalogPurchases']
    corr_cannibal = df['NumStorePurchases'].corr(other_channels)
    print(f"3. Store vs Non-Store Purchases Correlation: {corr_cannibal:.2f}")
    if corr_cannibal < 0:
        print("   -> Support found: Negative correlation suggests cannibalization.")
    else:
        print("   -> No support: Channels appear complementary.")

    # Hypothesis 4: US outperforms rest of world in total purchase volumes
    us_purchases = df[df['Country'] == 'US']['Total_Purchases']
    rest_purchases = df[df['Country'] != 'US']['Total_Purchases']
    t_stat, p_val = stats.ttest_ind(us_purchases, rest_purchases, equal_var=False)
    print(f"4. US vs Rest of World Purchases (T-Test): p-value = {p_val:.4f}")
    if p_val < 0.05 and us_purchases.mean() > rest_purchases.mean():
        print("   -> Significant: US has higher purchase volumes.")
    else:
        print(
            f"   -> Not Significant or US is lower (US Mean: {us_purchases.mean():.1f}, Rest Mean: {rest_purchases.mean():.1f})")


def generate_visualizations(df):
    """
    Generates required visualizations.
    """
    print("\n--- Generating Visualizations ---")

    # 1. Heatmap of Correlations
    plt.figure(figsize=(12, 10))
    # Select numeric columns for correlation
    numeric_df = df.select_dtypes(include=[np.number])
    sns.heatmap(numeric_df.corr(), cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reports\correlation_heatmap.png')

    # 2. Top Performing Products
    product_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    product_totals = df[product_cols].sum().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=product_totals.index, y=product_totals.values)
    plt.title('Total Revenue by Product Category')
    plt.xticks(rotation=45)
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reports\product_performance.png')

    # 3. Age vs Last Campaign Acceptance
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Response', y='Age', data=df)
    plt.title('Age Distribution by Last Campaign Acceptance (Response)')
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reports\age_vs_response.png')

    # 4. Country with Highest Campaign Acceptance
    country_acceptance = df[df['Response'] == 1]['Country'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=country_acceptance.index, y=country_acceptance.values)
    plt.title('Number of Accepted Offers by Country')
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reports\country_acceptance.png')

    # 5. Pattern: Children at Home vs Total Expenditure
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Total_Children', y='Total_Spending', data=df)
    plt.title('Total Expenditure by Number of Children')
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reportschildren_vs_spending.png')

    # 6. Education of Complainers
    complainers = df[df['Complain'] == 1]
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Education', data=complainers)
    plt.title('Education Level of Customers who Complained')
    plt.savefig(r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\reports\complainers_education.png')

    print("Visualizations saved as PNG files.")


def main():
    file_path = r'D:\Workspace\Python\SriPythonWorkshop\Simplilearn\resources\marketing_data.csv'

    # Step 1: Load and Clean
    df = load_and_clean_data(file_path)

    # Step 2: Feature Engineering
    df = feature_engineering(df)

    # Step 3: Outlier Treatment
    df = outlier_treatment(df)

    # Step 4: Encoding
    df = encode_categorical(df)

    # Step 5: Hypothesis Testing
    analyze_hypotheses(df)

    # Step 6: Visualizations
    generate_visualizations(df)


if __name__ == "__main__":
    main()