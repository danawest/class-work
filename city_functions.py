"""A collection of functions for working with cities."""

def city_country(city, country, population=''):
    """Returns a city and country neatly formatted."""
    if population:
    	city_full = city + ', ' + country + " - population " + str(population)
    else:
    	city_full = city + ', ' + country
    return city_full.title()