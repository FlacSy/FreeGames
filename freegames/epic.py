import requests
from bs4 import BeautifulSoup

def get_epic_discounts():
    url = "https://www.epicgames.com/store/en-US/browse?sortBy=discount&pageSize=20"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    games = []
    for item in soup.find_all('a', class_='css-g3jcms'):
        title_tag = item.find('div', class_='css-rgqwpc')
        title = title_tag.text.strip() if title_tag else "No title"
        
        discount_tag = item.find('div', class_='css-1q7f74q')
        discount = discount_tag.text.strip() if discount_tag else "No discount"
        
        original_price_tag = item.find('div', class_='css-d3i3lr')
        original_price = original_price_tag.text.strip() if original_price_tag else "No original price"
        
        discounted_price_tag = item.find('span', class_='css-119zqif')
        discounted_price = discounted_price_tag.text.strip() if discounted_price_tag else "No discounted price"
        
        games.append({
            'title': title,
            'discount': discount,
            'original_price': original_price,
            'discounted_price': discounted_price,
        })
    
    return games