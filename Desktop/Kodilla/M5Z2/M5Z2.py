#TO JEST TRUDNE ROZWIĄZANIE, Z POMOCĄ INTERNETU

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
def generate_multiple_views(library, times=10):
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
#dodawanie pełnych sezonów seriali
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


#TO JEST INNE ROZWIĄZANIE NIE WIEM CZY DLA MNIE ŁATWIEJSZE, TEŻ Z POMOCĄ INTERNETU - ale tutaj jest na konkretnym przykładzie, program nie uruchamia się tak jak jest w zadaniu ale chciałam robić krok po kroku każdy punkt i patrzeć co się dzieje (bez opcji dla chętnych).
class Movie:
    def __init__ (self, film_title, film_year, film_type, film_plays_number):
        self.film_title = film_title
        self.film_year = film_year
        self.film_type = film_type
        self.film_plays_number = film_plays_number
#metoda play na zwiększanie odtworzeń o 1 
    def play(self):
        self.film_plays_number += 1
#wyświetlanie filmu jako string z tytułem i rokiem + odtworzenia
    def __str__(self):
        return f"{self.film_title} ({self.film_year}) - {self.film_plays_number} odtworzeń"

class Series:
    def __init__(self, series_title, series_year, series_type, series_plays_number, series_number, sezon_number):
        self.series_title = series_title
        self.series_year = series_year
        self.series_type = series_type
        self.series_plays_number = series_plays_number
        self.series_number = series_number
        self.sezon_number = sezon_number
#metoda play na zwiększanie odtworzeń o 1   
    def play(self):
        self.series_plays_number += 1
#wyświetlanie serialu jako string z formą E episode i S season + odtworzenia
    def __str__(self):
        return f"{self.series_title} S{self.sezon_number}E{self.series_number} - {self.series_plays_number} odtworzeń"

film_no_1 = Movie(film_title = "Przerwane objęcia", film_year = 2001, film_type = "Moral", film_plays_number = 11987)
film_no_2 = Movie(film_title = "Skóra w której żyję", film_year = 2011, film_type = "Moral", film_plays_number = 33567)
series_no_1 = Series(series_title = "Ozark", series_year = 2020, series_type = "Crime", series_plays_number = 12897, series_number = "01", sezon_number = "01")
series_no_2 = Series(series_title = "Ku Jezioru", series_year = 2023, series_type = "Crime", series_plays_number = 10897, series_number = "02", sezon_number = "03")

print("Zwiększanie liczby odtworzeń o 1")
film_no_1.play()
print(film_no_1)
film_no_2.play()
print(film_no_2)
series_no_1.play()
print(series_no_1)
series_no_2.play()
print(series_no_2)

print("Alfabetyczne filtrowanie po filmach z listy")
#filmy i seriale jako lista
library = [film_no_1, film_no_2, series_no_1, series_no_2]
def get_movies(library):
        movies = [item for item in library if isinstance(item, Movie)]
        return sorted(movies, key=lambda movie: movie.film_title)

sorted_movies = get_movies(library)
for movie in sorted_movies:
    print(movie)

print("Alfabetyczne filtrowanie po serialach z listy")
def get_series(library):
        series = [item for item in library if isinstance(item, Series)]
        return sorted(series, key=lambda serie: serie.series_title)

sorted_series = get_series(library)
for serie in sorted_series:
    print(serie)

print("Funkcja search wyszukująca film lub serial po tytule")
def search(library, title):
    for item in library:
        if isinstance(item, Movie) and item.film_title.lower() == title.lower():
            return item
        elif isinstance(item, Series) and item.series_title.lower() == title.lower():
            return item
    return None
result = search(library, "Przerwane Objęcia")
if result:
    print(f"Znaleziono: {result}")
else:
    print("Nie znaleziono tytułu")

print("Funkcja generate views dodająca losowo odtworzenia od 1 do 100")
import random
def generate_views(library):
    item = random.choice(library)
    random_views = random.randint(1, 100)
    if isinstance(item, Movie):
        item.film_plays_number += random_views
    elif isinstance(item, Series):
        item.series_plays_number += random_views

    print(f"Losowo wybrano: {item}. Dodano {random_views} odtworzeń.")
generate_views(library)

print("Uruchomienie generate views 10 razy")
def generate_multiple_views(library):
    for _ in range(10):
        generate_views(library)
generate_multiple_views(library)

print("Funkcja top titles zwraca wybraną ilość najpopularniejszych tytułów")
def top_titles(library, n):
    sorted_library = sorted(library, key=lambda x: x.film_plays_number if hasattr(x, 'film_plays_number') else x.series_plays_number, reverse=True)
    return sorted_library[:n]
top_3_titles = top_titles(library, 3)
for title in top_3_titles:
    print(title)





