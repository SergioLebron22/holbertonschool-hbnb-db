""" Populate the database with some data at the start of the application"""
from src.persistence.repository import Repository


def populate_db(repo: Repository) -> None:

    from src.models.country import Country
    import pycountry
    
    countries = []
    
    for c in pycountry.countries:
        c = Country(c.name, c.alpha_2)
        if c not in countries:
            countries.append(c)

    for country in countries:
        existing_countries = repo.get_by_code(Country, country.code)
        if existing_countries is None:
            repo.save(country)
    print("Memory DB populated")
 

    
