# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import os
print("Current directory is:", os.getcwd())
print("Files in this folder:", os.listdir())


# Step 2: Load the Dataset
df = pd.read_csv("netflix_titles.csv")

# Step 3: Clean the Data
df.dropna(subset=["date_added"], inplace=True)
df["date_added"] = pd.to_datetime(df["date_added"])
df["year_added"] = df["date_added"].dt.year

# Step 4: Movies vs TV Shows
plt.figure(figsize=(6,4))
sns.countplot(x="type", data=df, palette="Set2")
plt.title("Movies vs TV Shows")
plt.show()

# Step 5: Content Added Each Year
plt.figure(figsize=(10,5))
df["year_added"].value_counts().sort_index().plot(kind="bar", color="skyblue")
plt.title("Content Added by Year")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# Step 6: Top Countries by Content
plt.figure(figsize=(8,5))
df["country"].value_counts().head(10).plot(kind="bar", color="green")
plt.title("Top 10 Countries with Netflix Content")
plt.xticks(rotation=45)
plt.show()

# Step 7: Top 10 Genres
genres = ", ".join(df["listed_in"].dropna()).split(", ")
genre_counts = Counter(genres)
top_genres = dict(genre_counts.most_common(10))

plt.figure(figsize=(10,5))
plt.bar(top_genres.keys(), top_genres.values(), color="orange")
plt.title("Top 10 Genres on Netflix")
plt.xticks(rotation=45)
plt.show()

# Step 8: Ratings Distribution
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index[:10], palette="pastel")
plt.title("Ratings Distribution")
plt.xticks(rotation=45)
plt.show()
