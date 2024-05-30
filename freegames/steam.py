import requests
from bs4 import BeautifulSoup

def get_steam_discounts():
    url = "https://store.steampowered.com/search/?specials=1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    games = []
    for item in soup.find_all('a', class_='search_result_row'):
        title = item.find('span', class_='title').text if item.find('span', class_='title') else "No title"
        
        discount_block = item.find('div', class_='discount_block')
        if discount_block:
            discount = discount_block.find('div', class_='discount_pct').text if discount_block.find('div', class_='discount_pct') else "No discount"
            original_price = discount_block.find('div', class_='discount_original_price').text if discount_block.find('div', class_='discount_original_price') else "No original price"
            discounted_price = discount_block.find('div', class_='discount_final_price').text if discount_block.find('div', class_='discount_final_price') else "No discounted price"
        else:
            discount = "No discount"
            original_price = "No original price"
            discounted_price = "No discounted price"
        
        games.append({
            'title': title,
            'discount': discount,
            'original_price': original_price,
            'discounted_price': discounted_price,
        })
    
    return games