# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.express as px

# Sample COVID-19 data (replace with actual data)
data = {
    "Date": ["2020-01-01", "2020-01-02", "2020-01-03", "2020-01-04", "2020-01-05"],
    "Cases": [10, 15, 20, 25, 30],
    "Deaths": [1, 2, 3, 4, 5],
    "Recoveries": [5, 10, 15, 20, 25]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculate daily change in cases, deaths and recoveries
df['New Cases'] = df['Cases'].diff()
df['New Deaths'] = df['Deaths'].diff()
df['New Recoveries'] = df['Recoveries'].diff()

# Calculate cumulative totals and rates
df['Cumulative Cases'] = df['Cases'].cumsum()
df['Cumulative Deaths'] = df['Deaths'].cumsum()
df['Cumulative Recoveries'] = df['Recoveries'].cumsum()
df['Case Fatality Rate'] = (df['Cumulative Deaths'] / df['Cumulative Cases']) * 100
df['Recovery Rate'] = (df['Cumulative Recoveries'] / df['Cumulative Cases']) * 100

# Plotly interactive plots
fig_cases = px.line(df, x='Date', y='Cases', title='Total COVID-19 Cases')
fig_new_cases = px.line(df, x='Date', y='New Cases', title='New COVID-19 Cases')
fig_deaths = px.line(df, x='Date', y='Deaths', title='Total COVID-19 Deaths')
fig_new_deaths = px.line(df, x='Date', y='New Deaths', title='New COVID-19 Deaths')
fig_recoveries = px.line(df, x='Date', y='Recoveries', title='Total COVID-19 Recoveries')
fig_new_recoveries = px.line(df, x='Date', y='New Recoveries', title='New COVID-19 Recoveries')

fig_cases.show()
fig_new_cases.show()
fig_deaths.show()
fig_new_deaths.show()
fig_recoveries.show()
fig_new_recoveries.show()

# Matplotlib static plots
plt.figure(figsize=(12, 8))

plt.subplot(3, 2, 1)
sns.lineplot(x='Date', y='Cases', data=df)
plt.title('Total COVID-19 Cases')

plt.subplot(3, 2, 2)
sns.lineplot(x='Date', y='New Cases', data=df)
plt.title('New COVID-19 Cases')

plt.subplot(3, 2, 3)
sns.lineplot(x='Date', y='Deaths', data=df)
plt.title('Total COVID-19 Deaths')

plt.subplot(3, 2, 4)
sns.lineplot(x='Date', y='New Deaths', data=df)
plt.title('New COVID-19 Deaths')

plt.subplot(3, 2, 5)
sns.lineplot(x='Date', y='Recoveries', data=df)
plt.title('Total COVID-19 Recoveries')

plt.subplot(3, 2, 6)
sns.lineplot(x='Date', y='New Recoveries', data=df)
plt.title('New COVID-19 Recoveries')

plt.tight_layout()
plt.show()

# Seaborn heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Cases', 'Deaths', 'Recoveries']].corr(), annot=True, cmap='coolwarm')
plt.title('COVID-19 Data Correlation')
plt.show()

# Case fatality rate and recovery rate plots
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.lineplot(x='Date', y='Case Fatality Rate', data=df)
plt.title('COVID-19 Case Fatality Rate')

plt.subplot(1, 2, 2)
sns.lineplot(x='Date', y='Recovery Rate', data=df)
plt.title('COVID-19 Recovery Rate')
plt.tight_layout()
plt.show()

# Additional enhancements
df['Active Cases'] = df['Cumulative Cases'] - df['Cumulative Deaths'] - df['Cumulative Recoveries']
df['Mortality Rate'] = (df['Cumulative Deaths'] / df['Cumulative Cases']) 

# Active cases plot
plt.figure(figsize=(8, 6))
sns.lineplot(x='Date', y='Active Cases', data=df)
plt.title('COVID-19 Active Cases')
plt.show()

# Mortality rate plot
plt.figure(figsize=(8, 6))
sns.lineplot(x='Date', y='Mortality Rate', data=df)
plt.title('COVID-19 Mortality Rate')
plt.show()