import requests
from bs4 import BeautifulSoup

def get_gog_discounts():
    url = "https://www.gog.com/games?price=discounted"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    games = []
    for item in soup.find_all('a', class_='product-tile'):
        title_tag = item.find('div', class_='product-tile__title ng-star-inserted')

        title = title_tag.text.strip() if title_tag else "No title"

        discount_tag = item.find('price-discount')
        discount = discount_tag.text.strip() if discount_tag else "No discount"
        
        original_price_tag = item.find('span', class_='base-value')
        original_price = original_price_tag.text.strip() if original_price_tag else "No original price"
        
        discounted_price_tag = item.find('span', class_='final-value')
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else "No discounted price"
        
        games.append({
            'title': title,
            'discount': discount,
            'original_price': original_price,
            'discounted_price': discounted_price,
        })
    
    return games