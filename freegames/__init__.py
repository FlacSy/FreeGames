from .steam import get_steam_discounts
from .epic import get_epic_discounts
from .gog import get_gog_discounts

def get_all_discounts():
    steam_discounts = get_steam_discounts()
    epic_discounts = get_epic_discounts()
    gog_discounts = get_gog_discounts()
    
    return {
        'steam': steam_discounts,
        'epic': epic_discounts,
        'gog': gog_discounts,
    }
