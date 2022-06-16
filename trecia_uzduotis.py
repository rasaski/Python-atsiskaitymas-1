# Turimas "audi" dict.

# Parašykite funkciją "show_object_values", kuri kaip argumentą priims objektą
# ir grąžins visus jo "values" list'e.

audi = {
    "make": 'audi',
    "model": 'A6',
    "year": 2005,
    "color": 'white',
}


def show_object_values():
    listas = []
    values = audi.get('make'), audi.get('model'), audi.get('year'), audi.get('color')
    listas += values

    print(listas)


show_object_values()
