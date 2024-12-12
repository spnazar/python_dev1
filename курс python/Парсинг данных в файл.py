import requests
from bs4 import BeautifulSoup

url = "https://tengrinews.kz/"

response = requests.get(url)

if response.status_code == 200:
    bs = BeautifulSoup(response.text, 'html.parser')
    
    all_cards = bs.findAll('div', 'main-news_super_item')
    
    all_news = []

    for card in all_cards:
        title = card.find('span').text if card.find('span') else "Без заголовка"

        all_news.append({
            'title': title.strip()
            })
    
    with open('news.txt', 'a+', encoding='utf-8') as my_file:
        for news in all_news:
            my_file.write(news['title'] + '\n')

    print("Данные успешно сохранены в 'news.txt'.")
else:
    print(f"Ошибка при запросе: {response.status_code}")

"""
# import requests
from bs4 import BeautifulSoup

# URL сайта
url = "https://tengrinews.kz/"

# Выполняем запрос к сайту
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Парсим содержимое страницы
    bs = BeautifulSoup(response.text, 'html.parser')

    # Ищем все карточки с новостями
    all_cards = bs.findAll('div', 'main-news_super_item')

    # Список для хранения новостей
    all_news = []

    for card in all_cards:
        # Находим заголовок новости
        title = card.find('span').text if card.find('span') else "Без заголовка"

        # Добавляем новость в список
        all_news.append({'title': title.strip()})

    # Вывод данных в терминал
    print("\nСобранные новости:")
    for index, news in enumerate(all_news, start=1):
        print(f"{index}. {news['title']}")
else:
    print(f"Ошибка при запросе: {response.status_code}")
"""