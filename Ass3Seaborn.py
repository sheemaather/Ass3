import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = sns.load_dataset("tips")
#Heat Map
plt.figure(figsize=(7,5))

corr = df.corr(numeric_only=True)

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)

plt.title("Correlation Heatmap of Tips Dataset", fontsize=10)
plt.show()

#Pair plot
sns.pairplot(
    df,
    hue="sex",
    palette="Set2",
    diag_kind="kde",
    height=2
)

plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()

#Violinplot
plt.figure(figsize=(7,5))

sns.violinplot(
    x="day",
    y="total_bill",
    hue="sex",
    data=df,
    palette=["#FF9999", "#66B2FF", "#99FF99", "#FFCC99"],
    split=True
)

plt.title("Total Bill Distribution by Day and Gender", fontsize=14)
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.legend(title="Gender",loc="upper left")
plt.show()
