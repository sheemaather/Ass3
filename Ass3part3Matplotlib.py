import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)

data = pd.DataFrame({
    "Day": np.arange(1, 31),
    "Sales": np.random.randint(50, 200, 30),
    "Profit": np.random.randint(10, 100, 30),
    "Category": np.random.choice(["A", "B", "C"], 30)
})
plt.figure(figsize=(8,4))
plt.plot(data["Day"], data["Sales"], marker='v')
plt.title("Sales Trend Over Time")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

category_counts = data["Category"].value_counts()

plt.figure(figsize=(6,4))
plt.bar(category_counts.index, category_counts.values, color='blue')
plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.legend(["Sales Distribution"],loc="upper right")
plt.show()

plt.figure(figsize=(6,4))
plt.scatter(data["Sales"], data["Profit"], alpha=0.7, color='red', marker='s')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

plt.figure(figsize=(6,4))
sns.boxplot(x="Category", y="Sales", data=data, color='pink')
plt.title("Sales by Category")
plt.show()

plt.figure(figsize=(6,4))
plt.hist(data["Sales"], bins=10, edgecolor='black', color='green')
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
