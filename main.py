import pandas as pd
#Load the Netflix dataset
df = pd.read_csv("dataset/netflix_titles.csv")
#Display the first 5 rows
print(df.head())
#Display dataset information
print("\nDataset Shape:")
print(df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
#Check missing values in each column
print("\nMissing Values:")
print(df.isnull().sum().to_string())
#Verify missing and blanks values
print("\nMissing values detected:")
print(df.isna().sum())
print("\nBlank or whitespace-only cells:")
print(
    df.astype("string")
    .apply(lambda col:
        col.str.strip().eq("").sum())
)
print("TEST: LATEST CODE IS RUNNING")
print("\nActual missing values by colum:")
print(df.isna().sum().to_dict())
# Check placeholder values in the dataset
print("\nPlaceholder values:")
for col in df.select_dtypes(include="object").columns:
    count = df[col].astype(str).str.strip().str.lower().isin(
        ["not given", "unknown", "n/a", "na", "null"]
    ).sum()
    if count > 0:
        print(f"{col}: {count}")
# Replace placeholder text with proper missing values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("string").str.strip()

    df[col] = df[col].replace(
        r"(?i)^(not given|unknown|n/a|na|null|none)?$",
        pd.NA,
        regex=True
    )
print("\nMissing values after standardizing placeholders:")
print(df.isna().sum().to_string())
# Handle missing values
df["director"] = df["director"].fillna("Not Available")
df["country"] = df["country"].fillna("Not Available")

# Drop rows where title is missing
df = df.dropna(subset=["title"])

print("\nMissing values after handling:")
print(df.isnull().sum())
# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

#check data types of each column
print("\nDataset Description:")
print(df.describe(include="all"))

#content type distribution
print("\nContent Type Distribution:")
print(df["type"].value_counts())

#visualize content type
import matplotlib.pyplot as plt
df["type"].value_counts().plot(
    kind="bar",
    title="Netflix Content Type Distribution"
)
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#content released per year
print("\nContent Released Per Year:")
yearly_content = df["release_year"].value_counts().sort_index()
print(yearly_content.tail(15))

#visualization
yearly_content.tail(15).plot(
    kind="bar",
    figsize=(10,5),
    title="Netflix Content Released by Year"
)

plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

#Netflix content rating analysis
print("\nContent Rating Distribution:")
rating_counts = df["rating"].value_counts()
print(rating_counts)

#visulization
rating_counts.head(10).plot(
    kind="bar",
    figsize=(10,5),
    title="Netflix Content Rating Distribution"
)
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

#top 10 countries with most netflix content
print("\nTop 10 Countries:")
country_counts =df["country"].value_counts().head(10)
print(country_counts)

#visulization
country_counts.plot(
    kind="bar",
    figsize=(10,5),
    title="Top 10 countries with Most Netflix Content"
)
plt.xlabel("Country")
plt.ylabel("Number of Titiles")
plt.tight_layout()
plt.show()

# Content Rating Distribution

print("\nContent Rating Distribution:")

rating_counts = df["rating"].value_counts().head(10)

print(rating_counts)

# Visualization

rating_counts.plot(
    kind="bar",
    figsize=(10,5),
    title="Netflix Content Rating Distribution"
)

plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

#movies vs tv shows analysis
print("\nMovies vs TV Shows:")
duration_counts = df.groupby("type")["duration"].count()
print(duration_counts)

#visualization
duration_counts.plot(
    kind="bar",
    figsize=(8,5),
    title="Movies vs TV Shows Duration Analysis"
)
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# Top 10 directors on Netflix

print("\nTop 10 Directors on Netflix:")

director_counts = df["director"].dropna()

director_counts = director_counts[
    ~director_counts.isin(["Not Available", "Unknown", "Not Given"])
]

director_counts = director_counts.str.split(",").explode().str.strip()

top_directors = director_counts.value_counts().head(10)

print(top_directors)

# Visualization
top_directors.plot(
    kind="bar",
    figsize=(10,5),
    title="Top 10 Directors on Netflix"
)

plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()