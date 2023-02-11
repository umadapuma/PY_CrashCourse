#11-1 City, Country:
def location(city,country,population=''):
    if population:
        combo = f"{city}, {country} " 
        wombo = f"population - {population}"
        return combo.title() + wombo
    else:
        combo = f"{city}, {country}"
        return combo.title()

    return 0