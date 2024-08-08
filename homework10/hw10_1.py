israel_info: dict = {"name": "Israel", "birth": 1948, "population_millions": 9.3, "capital": "Jerusalem",\
                     "language": "Hebrew", "cities": ["Jerusalem" "Tel Aviv" "Rishon Lezion" "Petah Tikva" "Ashdod"],\
                     "currency": "ILS", "area_km": 22145, "gdp_billion": 450}
print(israel_info.get("capital"))
print(israel_info.keys())
comp = [key.upper() for key in israel_info.keys()]
print(comp)
print(israel_info.values())
comp2 = [len(str(key)) for key in israel_info.values()]
print(comp2)
print(israel_info.items())
israel_info2 = (israel_info.copy())
print(israel_info2)
print(israel_info2.clear())
new_dict = dict.fromkeys(israel_info)
del israel_info['currency']
print('after delete', israel_info2)
try:
    del israel_info['currency']
except:
    print('could not delete. does it exist?')
print(israel_info.get("currency"))

print(israel_info.pop("area_km"))

israel_info.update({"population_millions": 9.4})
print('after update', israel_info)
israel_info.update({"national sport": "soccer"})
print('after update', israel_info)
