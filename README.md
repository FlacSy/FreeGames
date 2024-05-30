# FreeGames

## Введение

FreeGames - это библиотека на Python для получения информации о скидках на игры с различных платформ, включая Steam, Epic Games и GOG.com. Она предоставляет функции для получения скидок, первоначальных цен и цен со скидкой на игры, доступные на этих платформах.

## Установка

Чтобы установить библиотеку `FreeGames`, воспользуйтесь pip:

[PyPi](https://pypi.org/project/py-freegames)
```bash
pip install py-freegames
```
[GitHub](https://github.com/FlacSy/FreeGames)
```bash
pip install git+https://github.com/FlacSy/FreeGames
```

### Пример использования

Вот как вы можете использовать FreeGames для получения скидок с различных платформ и их вывода:

```python
from freegames import get_all_discounts

def print_discounts():
    discounts = get_all_discounts()
    
    print("Скидки на Steam:")
    for game in discounts['Steam']:
        print(f"Название: {game['title']}, Скидка: {game['discount']}, Оригинальная цена: {game['original_price']}, Цена со скидкой: {game['discounted_price']}")
    
    print("\nСкидки на Epic Games:")
    for game in discounts['Epic Games']:
        print(f"Название: {game['title']}, Скидка: {game['discount']}, Оригинальная цена: {game['original_price']}, Цена со скидкой: {game['discounted_price']}")
    
    print("\nСкидки на GOG:")
    for game in discounts['GOG']:
        print(f"Название: {game['title']}, Скидка: {game['discount']}, Оригинальная цена: {game['original_price']}, Цена со скидкой: {game['discounted_price']}")

print_discounts()
```

## Функции

### `get_all_discounts()`

Эта функция возвращает словарь, содержащий скидки с разных платформ.

- **Возвращает:** `dict`
- **Ключи:** 'Steam', 'Epic Games', 'GOG'
- **Значения:** Списки словарей, содержащих информацию о играх, включая название, скидку, оригинальную цену и цену со скидкой.

### `get_steam_discounts()`

Эта функция возвращает список словарей, содержащих скидки от Steam.

- **Возвращает:** `list`
- **Элементы:** Словари, содержащие информацию о играх, включая название, скидку, оригинальную цену и цену со скидкой.

### `get_epic_games_discounts()`

Эта функция возвращает список словарей, содержащих скидки от Epic Games.

- **Возвращает:** `list`
- **Элементы:** Словари, содержащие информацию о играх, включая название, скидку, оригинальную цену и цену со скидкой.

### `get_gog_discounts()`

Эта функция возвращает список словарей, содержащих скидки от GOG.com.

- **Возвращает:** `list`
- **Элементы:** Словари, содержащие информацию о играх, включая название, скидку, оригинальную цену и цену со скидкой.

## Лицензия

FreeGames выпущен под лицензией MIT. См. файл [LICENSE](https://github.com/FlacSy/FreeGames/LICENSE) для получения подробной информации.