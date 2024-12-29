import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import scipy.stats as stats

# Sample data
data = {
    "Fruits": ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
    "Quantity": [25, 40, 30, 20, 35],
    "Price": [10, 5, 8, 12, 9]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)

# Customizable bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Fruits", y="Quantity", data=df, palette="Blues", capsize=0.2)
plt.title("Fruit Quantity", fontsize=18)
plt.xlabel("Fruit Name", fontsize=14)
plt.ylabel("Quantity", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

# Interactive 3D scatter plot
fig = px.scatter_3d(df, x="Quantity", y="Price", z="Quantity", color="Fruits")
fig.update_layout(title="Fruit Quantity-Price Relationship")
fig.show()

# Dual-axis line chart with regression line
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df["Fruits"], df["Quantity"], color="blue", label="Quantity", marker="o")
ax1.set_xlabel("Fruit Name", fontsize=14)
ax1.set_ylabel("Quantity", color="blue", fontsize=14)
ax1.tick_params(axis="y", labelcolor="blue")

ax2 = ax1.twinx()
ax2.plot(df["Fruits"], df["Price"], color="red", label="Price", marker="s")
ax2.set_ylabel("Price", color="red", fontsize=14)
ax2.tick_params(axis="y", labelcolor="red")

z = stats.linregress(df["Quantity"], df["Price"])[0] * df["Quantity"] + stats.linregress(df["Quantity"], df["Price"])[1]
ax1.plot(df["Fruits"], z, color="green", label="Regression Line")

plt.title("Fruit Quantity-Price Trend", fontsize=18)
plt.legend(loc="upper left")
plt.show()

# Heatmap with clustering
df_pivot = pd.pivot_table(df, values="Quantity", index="Fruits", columns="Price")
plt.figure(figsize=(10, 6))
sns.clustermap(df_pivot, annot=True, cmap="Blues", standard_scale=1)
plt.title("Fruit Quantity Heatmap", fontsize=18)
plt.show()

# Boxplot for quantity distribution
plt.figure(figsize=(10, 6))
sns.boxplot(df["Quantity"])
plt.title("Fruit Quantity Distribution", fontsize=18)
plt.show()

# Violin plot for price distribution
plt.figure(figsize=(10, 6))
sns.violinplot(df["Price"])
plt.title("Fruit Price Distribution", fontsize=18)
plt.show()

# Pairplot for relationships
plt.figure(figsize=(10, 6))
sns.pairplot(df)
plt.title("Fruit Quantity-Price Relationship", fontsize=18)
plt.show()