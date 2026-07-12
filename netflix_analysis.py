import pandas as pd 

#Which year had the most releases?
# Most common genres?
# Longest movies?
# Movies vs TV shows?
# Countries with the most content?

df = pd.read_csv("data.csv")
# print(df["release_year"].to_string())

group = df.groupby("release_year")
group_count = group["release_year"].count()
print(group_count.max())