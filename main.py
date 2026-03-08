"""
Mumbai Weather Data Analysis
Author: Ansari Mohd Zaki
Date: 3/9/2026
Description: Loads historical weather data, cleans it, and creates visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Load Data.
def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print("File not found. Please check the path.")
        exit()

# Clean Data.
def clean_data(df):
    print("\n*************** Cleaning ***************")

    # Convert Date column (DD-MM-YYYY)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')
    # Drop rows with invalid date
    df = df.dropna(subset=['Date'])
    print(f"Dates parsed.")

    # Convert temperature columns, coercing errors (like '-----') to NaN
    df['Temp Max'] = pd.to_numeric(df['Temp Max'], errors='coerce')
    df['Temp Min'] = pd.to_numeric(df['Temp Min'], errors='coerce')

    # Handle rainfall: separate amount and trace flag
    # First, create a numeric column; 'Tr' becomes NaN
    df['Rain_Amount'] = pd.to_numeric(df['Rain'], errors='coerce')
    # Create a boolean column for trace rainfall
    df['Rain_Trace'] = (df['Rain'] == 'Tr')
    # Define a rainy day as amount > 0 OR trace = True
    df['Rainy'] = (df['Rain_Amount'] > 0) | df['Rain_Trace']

    return df

# Prepare Data for Analysis.
def prepare_data(df):
    # Add year and month columns
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    # Daily mean temperature (only where both temps are available)
    df['Mean Temp'] = (df['Temp Max'] + df['Temp Min']) / 2
    return df

# Create Visualizations.
def create_charts(df):
    os.makedirs('visualizations', exist_ok=True)

    # Subset for temperature analysis (drop rows with missing temps)
    df_temp = df.dropna(subset=['Temp Max', 'Temp Min']).copy()

    # 1. Annual average temperature line chart
    annual_temp = df_temp.groupby('Year')['Mean Temp'].mean().reset_index()
    plt.figure(figsize=(12,6))
    plt.plot(annual_temp['Year'], annual_temp['Mean Temp'], marker='o', linestyle='-', color='red')
    plt.title('Annual Average Temperature in Mumbai (1951–2024)', fontsize=16)
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('visualizations/annual_temp_trend.png')
    plt.close()
    print("Line chart saved: annual_temp_trend.png")

    # 2. Monthly average temperature bar chart
    monthly_temp = df_temp.groupby('Month')['Mean Temp'].mean().reset_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_temp['MonthName'] = monthly_temp['Month'].map(lambda x: month_names[x-1])

    plt.figure(figsize=(10,6))
    plt.bar(monthly_temp['MonthName'], monthly_temp['Mean Temp'], color='skyblue')
    plt.title('Average Monthly Temperature in Mumbai (Overall)', fontsize=16)
    plt.xlabel('Month')
    plt.ylabel('Average Temperature (°C)')
    plt.tight_layout()
    plt.savefig('visualizations/monthly_avg_temp.png')
    plt.close()
    print("Bar chart saved: monthly_avg_temp.png")

    # 3. Annual total rainfall bar chart
    # Use only numeric rainfall (trace counts as 0)
    annual_rain = df.groupby('Year')['Rain_Amount'].sum().reset_index()
    # Remove years with no data
    annual_rain = annual_rain[annual_rain['Year'] >= 1951]

    plt.figure(figsize=(12,6))
    plt.bar(annual_rain['Year'], annual_rain['Rain_Amount'], color='blue')
    plt.title('Annual Total Rainfall in Mumbai (1951–2024)', fontsize=16)
    plt.xlabel('Year')
    plt.ylabel('Total Rainfall (mm)')
    plt.tight_layout()
    plt.savefig('visualizations/annual_rainfall.png')
    plt.close()
    print("Bar chart saved: annual_rainfall.png")

# Main.
def main():
    print("\n******************** MUMBAI WEATHER DATA ANALYSIS ********************\n")


    # Load
    df = load_data("Internship\Week 4\data\Weather dataset.csv")

    # Clean
    df = clean_data(df)

    # Prepare (add year, month, mean temp)
    df = prepare_data(df)

    # Create visualizations
    create_charts(df)

    print("\nAll tasks completed. Check the 'visualizations' folder.")

    print("\n**********************************************************************\n")


if __name__ == "__main__":
    main()