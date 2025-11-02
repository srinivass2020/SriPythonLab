"""
Steps to Perform
    Create a Pandas Series for sales data
    Use a list of daily sales figures to create a Pandas Series
    Assign days of the week as the index
Access and manipulate sales data
    Access sales data for specific days using index labels
    Calculate total sales for the week
    Identify the day with the highest and lowest sales
Basic analysis of sales data
    Calculate the average sales for the week
    Determine the days with sales figures significantly different from the average
"""

#Step 1: Import the pandas library
#Use a list of daily sales figures to create a Pandas Series
import pandas as pd
sales_figures = [250, 300, 400, 150, 500]
sales_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#Assign days of the week as the index
sales_series = pd.Series(sales_figures)
print("Sales Series before assigning Index" ,sales_series.head())
#Assign days of the week as the index
sales_series.index = sales_days
print("Sales Series after assigning Index" ,sales_series.head())
#Display the Series
print("Daily Sales Figures:")
print(sales_series)

#Step 2: Access and manipulate sales data
#Access sales data for specific days using index labels
monday_sales = sales_series['Monday']
wednesday_sales = sales_series['Wednesday']
print(f"\nSales on Monday: {monday_sales}") 
print(f"Sales on Wednesday: {wednesday_sales}")
#Calculate total sales for the week
total_sales = sales_series.sum()
print(f"\nTotal Sales for the Week: {total_sales}")
#Identify the day with the highest and lowest sales
highest_sales_day = sales_series.idxmax()
lowest_sales_day = sales_series.idxmin()
print(f"Highest Sales Day: {highest_sales_day} with sales of {sales_series[highest_sales_day]}")
print(f"Lowest Sales Day: {lowest_sales_day} with sales of {sales_series[lowest_sales_day]}")
#Step 3: Basic analysis of sales data
print("\nBasic Analysis of Sales Data:",sales_series.describe())
#Calculate the average sales for the week
average_sales = sales_series.mean()
print(f"\nAverage Sales for the Week: {average_sales}")
#Determine the days with sales figures significantly different from the average
significantly_high_sales = sales_series[sales_series > average_sales * 1.2]
significantly_low_sales = sales_series[sales_series < average_sales * 0.8]
print("\nDays with Significantly High Sales:")  
print(significantly_high_sales)
print("\nDays with Significantly Low Sales:")
print(significantly_low_sales)



