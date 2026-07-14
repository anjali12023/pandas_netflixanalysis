import pandas as pd 

# Longest movies?
# Movies vs TV shows?
# Countries with the most content?

df = pd.read_csv("data.csv")
# print(df)
# print(df["release_year"].to_string())

#Which year had the most releases?
# group = df.groupby("release_year")
# group_count = group["release_year"].count()
# most_releases_year = group_count.idxmax()
# most_releases = group_count.max()
# print(f"Most releases were in {most_releases_year}, with {most_releases} releases!")


# Most common genres?
# print(df["listed_in"].to_string())
group = df.groupby("listed_in")
group_count = group["listed_in"].count()
most_category_text = group_count.idxmax()
most_category = group_count.max()
# print(most_category)
# print(f"Most common genres were {most_category_text}, with {most_category} counts!")



# Longest movies?
#filer all movies
# max movies

# group = df.groupby["type"]
print(group)

group = df[df["type"] == "Movie"]
group_count = group["duration"].max()
# most_category = group_count.max()
print(f"Longest movie ran for {group_count}!")
