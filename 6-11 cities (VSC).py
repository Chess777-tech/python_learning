"""
make a dictionary called cities 
use the names of three cities as keys in dictionary 
create a dictionary of info 
about each city & country city is in 
its approximate population & and one fact about the country 


The keys for each city's dictionary should be 
country
population
fact


then print the name of each city & all of the information
"""


cities = {
    'London': {
    'country':     'england',
    'population': '8.982 million',
    'fact':       'Over 300 languages are spoken in london '
    },

    'Ontario': {
    'country':     'canada',
    'population': '14.57 million',
    'fact':       'Ontario is larger than France and Spain combined'
    },

    'new york': {
    'country':    'united states',
    'population': '8.468 million',
    'fact':       'Lady Liberty was not made in the USA',
    }
}



for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"It has a population of about {population}.")
    print(f"A fun Fact: {fact} .")