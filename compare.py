import config

#Porovnanie prichádzauceho názvu pravidla s tým ktoré sa nachádza v konfiguračnom súbore.
def compareRule(type):
    if type in config.DIR_NAMES:
        return type.upper()
    else:
        return config.DEFAULT_DIR.upper()