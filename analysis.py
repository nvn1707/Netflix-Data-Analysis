import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/netflix_titles.csv")

print("========== NETFLIX DATA ANALYSIS ==========\n")

# Dataset overview
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Missing values before cleaning
print("\n========== BEFORE CLEANING ==========\n")
print(df.isnull().sum())

# Data cleaning
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = df["date_added"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

# Missing values after cleaning
print("\n========== AFTER CLEANING ==========\n")
print(df.isnull().sum())

# Content type analysis
print("\nContent Type Count:")
print(df["type"].value_counts())

# Top release years
print("\nTop 10 Release Years:")
print(df["release_year"].value_counts().head(10))

# Top 10 countries
top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_countries.plot(kind="bar")
plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
