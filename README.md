# Habr UI Tests

UI-автотесты для сайта [habr.com](https://habr.com/ru/articles/) на Python + Selenium + pytest

## Стек

- Python 3.9+
- [Selenium](https://pypi.org/project/selenium/) 4.36.0
- [pytest](https://pypi.org/project/pytest/) 8.4.2
- Google Chrome + ChromeDriver

  # Установить зависимости
pip install -r requirements.txt

## Структура проекта

```
test_habr/
├── tests/
│   ├── conftest.py        # Фикстуры: browser, base_url, wait
│   ├── test_articles.py   # Тесты навигационных вкладок
├── requirements.txt
└── README.md
```
## Тест-кейсы

### `test_articles.py`
| Тест | Описание |
|------|----------|
| `test_all_tabs_clickable` | Кликает по каждой вкладке и проверяет, что активна ровно одна вкладка и URL совпадает |

**Проверяемые вкладки:** Статьи, Посты, Новости, Хабы, Пользователи, Компании.
