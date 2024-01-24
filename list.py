travel_log = [
    {
        "country": "France",
        "visits": 12
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "Visits": 5,
        "Cities": ["Berlin", "Hamburg", "STuttgart"]
    }
]

# TODO-1: Write a function  that will allow new caountries to be added to the travell_log

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    travel_log.append(new_country)
    

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
