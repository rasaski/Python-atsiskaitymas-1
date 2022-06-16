# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu.
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas:
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title: str, director: str, budget: float):
        self.title = title
        self.director = director
        self.budget = budget


filmas1 = Movie("Vienas namuose", "Chris Columbus", 150000000)
filmas2 = Movie("Valentinas vienas", "Donatas Ulvydas", 1000000)


def was_expensive(self):
    if self.budget > 10000000:
        print(True)
    else:
        print(False)


was_expensive(filmas1)
was_expensive(filmas2)