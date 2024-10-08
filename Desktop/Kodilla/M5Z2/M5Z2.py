class Film:
    def __init__ (self, title, year, type, plays_number):
        self.title = title
        self.year = year
        self.type = type
        self.plays_number = plays_number

class Series(Film):
    def __init__(self, series_number, sezon_number, *args, **kwargs)
        super().__init__(*args, **kwargs)
        self.series_number = series_number
        self.sezon_number = sezon_number

