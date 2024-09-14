import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')


print("Basic Information:\n")
print(df.info())
print("\nFirst few rows of the dataset:\n")
print(df.head())

print("\nSummary Statistics:\n")
print(df.describe())


print("\nMissing Values:\n")
print(df.isnull().sum())


print("\nUnivariate Analysis - Histograms:\n")
df.hist(figsize=(10, 8), bins=20)
plt.suptitle("Histograms of Iris Features")
plt.show()


print("\nPairplot for feature relationships:\n")
sns.pairplot(df, hue='species')
plt.show()


print("\nCorrelation Heatmap:\n")
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()


print("\nBoxplot for Feature Distribution across Species:\n")
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Sepal Length Distribution across Species')
plt.show()
