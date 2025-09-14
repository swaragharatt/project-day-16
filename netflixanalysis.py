import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("dark_background")
NETFLIX_RED = "#E50914"
NETFLIX_BLACK = "#141414"
NETFLIX_WHITE = "#FFFFFF"
NETFLIX_GRAY = "#999999"
plt.rcParams["font.family"] = "Impact"   
plt.rcParams["font.weight"] = "bold"

df = pd.read_csv(r"C:\Users\USER\OneDrive\New folder\New folder\netflx\netflix_titles.csv.zip")  
df.drop_duplicates(inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['genre_list'] = df['listed_in'].str.split(', ')
all_genres = []
for sublist in df['genre_list'].dropna():
    all_genres.extend(sublist)

genre_counts = pd.Series(all_genres).value_counts().head(10)

plt.figure(figsize=(10, 5), facecolor=NETFLIX_BLACK)
plt.barh(genre_counts.index, genre_counts.values, color=NETFLIX_RED)
plt.title("TOP 10 NETFLIX GENRES", fontsize=20, color=NETFLIX_WHITE, pad=15)
plt.xlabel("NUMBER OF TITLES", color=NETFLIX_GRAY, fontsize=12)
plt.ylabel("GENRE", color=NETFLIX_GRAY, fontsize=12)
plt.xticks(color=NETFLIX_WHITE, fontsize=10)
plt.yticks(color=NETFLIX_WHITE, fontsize=10)
plt.gca().invert_yaxis()
plt.show()

ratings_count = df['rating'].value_counts()

plt.figure(figsize=(8, 4), facecolor=NETFLIX_BLACK)
plt.bar(ratings_count.index, ratings_count.values, color=NETFLIX_RED, edgecolor=NETFLIX_WHITE)
plt.title("CONTENT RATINGS DISTRIBUTION", fontsize=20, color=NETFLIX_WHITE, pad=15)
plt.xlabel("RATING", color=NETFLIX_GRAY, fontsize=12)
plt.ylabel("NUMBER OF TITLES", color=NETFLIX_GRAY, fontsize=12)
plt.xticks(rotation=45, color=NETFLIX_WHITE, fontsize=10)
plt.yticks(color=NETFLIX_WHITE, fontsize=10)
plt.show()

df = df.dropna(subset=['date_added'])
df['year_added'] = df['date_added'].dt.year
yearly_trend = df['year_added'].value_counts().sort_index()

plt.figure(figsize=(12, 4), facecolor=NETFLIX_BLACK)
plt.plot(yearly_trend.index, yearly_trend.values, marker="o", color=NETFLIX_RED, linewidth=2)
plt.title("NETFLIX CONTENT ADDITIONS OVER TIME", fontsize=20, color=NETFLIX_WHITE, pad=15)
plt.xlabel("YEAR ADDED", color=NETFLIX_GRAY, fontsize=12)
plt.ylabel("NUMBER OF TITLES ADDED", color=NETFLIX_GRAY, fontsize=12)
plt.xticks(color=NETFLIX_WHITE, fontsize=10)
plt.yticks(color=NETFLIX_WHITE, fontsize=10)
plt.grid(True, linestyle="--", alpha=0.3, color=NETFLIX_GRAY)
plt.show()

type_trend = df.groupby(['year_added', 'type']).size().unstack().fillna(0)

ax = type_trend.plot(kind='bar', stacked=True, figsize=(12, 5),
                     color=[NETFLIX_RED, NETFLIX_GRAY], edgecolor=NETFLIX_WHITE)

plt.title("TREND: MOVIES VS TV SHOWS EACH YEAR", fontsize=20, color=NETFLIX_WHITE, pad=15)
plt.xlabel("YEAR", color=NETFLIX_GRAY, fontsize=12)
plt.ylabel("COUNT", color=NETFLIX_GRAY, fontsize=12)
plt.xticks(rotation=45, color=NETFLIX_WHITE, fontsize=10)
plt.yticks(color=NETFLIX_WHITE, fontsize=10)
plt.legend(title="TYPE", facecolor=NETFLIX_BLACK, edgecolor=NETFLIX_WHITE,
           labelcolor=NETFLIX_WHITE, title_fontsize=10, fontsize=9)
plt.tight_layout()
plt.show()
