import random
from datetime import datetime

class Content:
    def __init__ (self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        self.views = 0

    def play(self):
        self.views += 1
    
class Movie(Content):
    def __str__(self):
        return f"{self.title} ({self.year})"

class Series(Content):
    def __init__(self, title, year, genre, season, episode):
        super(). __init__(title, year, genre)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"

#filtruje filmy z biblioteki  
def get_movies(library):
    return sorted([content for content in library if isinstance(content, Movie)], key=lambda x: x.title)
#filtruje seriale z biblioteki
def get_series(library):
    return sorted([content for content in library if isinstance(content, Series)], key=lambda x: x.title)
#szuka po tytule
def search(library, title):
    return next((content for content in library if content.title == title), None)
#losowo zwieksza liczbe odtworzeń
def generate_views(library):
    item = random.choice(library)
    item.views += random.randint(1, 100)
#wielokrotnie uruchamia generate views
def generate_multiple_views(library, times=100):
    for _ in range(times):
        generate_views(library)
#zwraca najpopularniejze tresci
def top_titles(library, top_n=3, content_type=None):
    if content_type == "movie":
        filtered = get_movies(library)
    elif content_type == "series":
        filtered = get_series(library)
    else:
        filtered = library
    return sorted(filtered, key=lambda x: x.views, reverse=True)[:top_n]
#dodawanie pełne sezony seriali
def add_season(library, title, year, genre, season, episodes):
    for episode in range(1, episodes +1):
        library.append(Series(title, year, genre, season, episode))

def main():
    print("Biblioteka filmów")
    
    library = [
        Movie("Przerwane objęcia", 2001, "Moral"),
        Movie("Skóra w której żyję", 2011, "Moral"),
        Series("Ozark", 2020, "Crime", 1, 1),
        Series("The Dark", 2021, "Sci-Fi", 1, 5)
    ]
    add_season(library, "Ku Jezioru", 2023, "Crime", 3, 5)
    generate_multiple_views(library, times=10)

    today = datetime.now().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {today}")
    for top_title in top_titles(library, top_n=3):
        print(f"{top_title} - {top_title.views} odtworzeń")

if __name__ == "__main__":
    main()





