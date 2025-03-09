import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Set Seaborn style for the plots
sns.set(style="darkgrid")

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

# 1: Plot the 'Confirmed' cases over time with customized styling
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Confirmed'], label='Confirmed Cases', color='blue', marker='o', markersize=8, linestyle='-', linewidth=2)
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Confirmed Cases', fontsize=14, fontweight='bold')
plt.title('Confirmed COVID-19 Cases Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()

# Deaths over time in a bar graph with color and data labels
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Date'], df['Deaths'], label='Deaths', color='red', alpha=0.7)
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Deaths', fontsize=14, fontweight='bold')
plt.title('COVID-19 Deaths Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()

# Adding data labels to the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()

# Recovered over time with improved styling
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Recovered"], color="green", marker="o", markersize=8, linestyle='-', linewidth=2)
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('Recovered', fontsize=14, fontweight='bold')
plt.title('COVID-19 Recovered Over Time', fontsize=16, fontweight='bold')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.show()

# Confirmed, Death and Recovered ratio in a Pie chart with explosion and style
plt.figure(figsize=(10, 6))
sizes = df[['Confirmed', 'Deaths', 'Recovered']].sum(axis=0)
labels = ['Confirmed', 'Deaths', 'Recovered']
explode = (0.1, 0.1, 0.1)  # explode the slices a bit

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=explode, 
        colors=['#66b3ff', '#ff6666', '#99ff99'], shadow=True, 
        textprops={'fontsize': 14, 'fontweight': 'bold'})
plt.title('COVID-19 Cases, Deaths, and Recovered Ratio', fontsize=16, fontweight='bold')
plt.legend()
plt.show()
