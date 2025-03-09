import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Step 1: Read the CSV file into a DataFrame without setting any column as the index
df = pd.read_csv("data.csv", index_col=False)

# Step 2: Display the DataFrame in a table format
print("Original DataFrame:")
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# CLEANING THE MESSY DATA
# Step 1: Drop rows with any missing values
df.dropna(inplace=True)

# Step 2: Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Step 3: Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

# Data Visualization using matplotlib

# 1: Plot the 'Confirmed' cases over time with bold labels and catchy colors
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Confirmed'], label='Confirmed Cases', color='blue', marker='o', markersize=8)
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Confirmed Cases', fontsize=14, fontweight='bold')
plt.title('Confirmed COVID-19 Cases Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.legend()
plt.show()

# Deaths over time in a bar graph with bold labels and catchy colors
plt.figure(figsize=(10, 6))
plt.bar(df['Date'], df['Deaths'], label='Deaths', color='red', alpha=0.7)
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Deaths', fontsize=14, fontweight='bold')
plt.title('COVID-19 Deaths Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.legend()
plt.show()

# Recovered over time with bold labels and catchy colors
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Recovered"], color="blue", marker="o", markersize=8)
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Recovered', fontsize=14, fontweight='bold')
plt.title('COVID-19 Recovered Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.legend()
plt.show()

# Confirmed, Death, and Recovered ratio in a Pie chart with bold labels, catchy colors, and explode effect
explode = (0.1, 0, 0)  # This will "explode" the 'Confirmed' slice
plt.figure(figsize=(10, 6))
plt.pie(df[['Confirmed', 'Deaths', 'Recovered']].sum(axis=0), labels=['Confirmed', 'Deaths', 'Recovered'], autopct='%1.1f%%', startangle=140, colors=["red","blue","green"], textprops={'fontsize': 14, 'fontweight': 'bold'}, explode=explode)
plt.title('COVID-19 Cases, Deaths, and Recovered Ratio', fontsize=16, fontweight='bold')
plt.legend()
plt.show()