countries = [{'name': 'Israel', 'population': 9.3, 'birth': 1948},
            {'name': 'United States', 'population': 331.9, 'birth': 1776},
            {'name': 'Japan', 'population': 125.8, 'birth': 660 },
            {'name': 'Australia', 'population': 25.7, 'birth': 1901},
            {'name': 'Canada', 'population': 38.0, 'birth': 1867}]

print(list(filter(lambda countries: countries["population"] > 30, countries)))
print(list(filter(lambda countries: countries["birth"] > 1800, countries)))
print(list(map(lambda countries: countries["name"], countries)))
print(list(map(lambda countries: countries["birth"], countries)))
print(sorted(countries, key=lambda countries: countries["birth"]))
print(sorted(countries, key=lambda countries: countries["population"]))