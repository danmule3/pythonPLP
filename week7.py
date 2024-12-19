import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
from sklearn.datasets import load_iris  

# Load the Iris dataset  
iris = load_iris()  
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)  
iris_df['species'] = iris.target  

# Display the first few rows  
print("First few rows of the dataset:")  
print(iris_df.head())  

# Explore the structure of the dataset  
print("\nData types and missing values:")  
print(iris_df.info())  

# Check for missing values  
print("\nMissing values:")  
print(iris_df.isnull().sum())  

# Clean the dataset (not needed here, but let's ensure)  
# If there were missing values, we could fill or drop them  
# Example: iris_df.fillna(iris_df.mean(), inplace=True)  
# or  
# iris_df.dropna(inplace=True)

# Compute basic statistics  
print("\nBasic statistics of numerical columns:")  
print(iris_df.describe())  

# Group by species and compute the mean of numerical columns  
grouped_means = iris_df.groupby('species').mean()  
print("\nMean of numerical columns grouped by species:")  
print(grouped_means)  

# Identify patterns  
# For example, we can see which species has the largest petal length  
max_petal_length_species = grouped_means['petal length (cm)'].idxmax()  
print(f"\nSpecies with the largest average petal length: {max_petal_length_species}")


# Set the style for seaborn  
sns.set(style="whitegrid")  

# 1. Line chart (not applicable for this dataset, but we can create a trend for petal length)  
plt.figure(figsize=(10, 6))  
iris_df.groupby('species')['petal length (cm)'].mean().plot(kind='line', marker='o')  
plt.title('Average Petal Length by Species')  
plt.xlabel('Species')  
plt.ylabel('Average Petal Length (cm)')  
plt.xticks(ticks=range(len(iris.target_names)), labels=iris.target_names)  
plt.grid()  
plt.show()  

# 2. Bar chart  
plt.figure(figsize=(10, 6))  
sns.barplot(x='species', y='petal length (cm)', data=iris_df, estimator=lambda x: sum(x) / len(x))  
plt.title('Average Petal Length per Species')  
plt.xlabel('Species')  
plt.ylabel('Average Petal Length (cm)')  
plt.show()  

# 3. Histogram  
plt.figure(figsize=(10, 6))  
sns.histplot(iris_df['petal length (cm)'], bins=20, kde=True)  
plt.title('Distribution of Petal Length')  
plt.xlabel('Petal Length (cm)')  
plt.ylabel('Frequency')  
plt.show()  

# 4. Scatter plot  
plt.figure(figsize=(10, 6))  
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=iris_df)  
plt.title('Sepal Length vs Petal Length')  
plt.xlabel('Sepal Length (cm)')  
plt.ylabel('Petal Length (cm)')  
plt.legend(title='Species')  
plt.show()