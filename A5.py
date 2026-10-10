try:
    import seaborn as sns  # type: ignore
    import matplotlib.pyplot as plt
except ImportError as exc:
    raise SystemExit("This script requires the 'seaborn' and 'matplotlib' packages. Install them with: pip install seaborn matplotlib") from exc

df = sns.load_dataset('penguins')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()
print("df.info():")
print(df.info())
print()
print("descrbe():")
print(df.describe())
print()
print("Species:", df['species'].unique())
print("Island:", df['island'].unique())
sns.histplot(data=df, x='body_mass_g', bins = 20, color='skyblue')
plt.title("Distribution of penguin body mass")
plt.xlabel("Body Mass (g)")
plt.ylabel("Count")
plt.show()

sns.kdeplot(data=df, x="flipper_length_mm", hue="species", fill=True)
plt.title("KDE of Flipper Length by Species (KDE)")
plt.xlabel("Flipper Length (mm)")
plt.show()

sns.histplot(data=df, x="flipper_length_mm", kde="True", color = "coral")
plt.title("Flipper length - histogram with KDE Curve")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Count")
plt.show()

sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Flipper Length vs Body Mass by Species ")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (grams)")
plt.show()

corr = df.corr(numeric_only=True)
print("Correlation matrix:")
print(corr)
print()

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap - Penguins Measurements")
plt.show()