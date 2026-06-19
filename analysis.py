import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/netflix_titles.csv")

# Clean country column
df["country"] = df["country"].fillna("Unknown")

# Top 10 countries
top_countries = df["country"].value_counts().head(10)

top_countries.plot(kind="bar")

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.show()
