import requests
from bs4 import BeautifulSoup
import networkx as nx
import json


def crawl_web(start_url, depth):
    visited = set()  # Словарь для отслеживания посещенных страниц
    graph = nx.DiGraph()  # Создание направленного графа

    def crawl(url, level):
        url_begin = 'https://en.wikipedia.org'
        url = url_begin + url
        # Проверка, посещали ли мы эту страницу и достигнут ли максимальный уровень
        if url not in visited and level <= depth:
            print(url)
            visited.add(url)  # Добавляем текущий URL в список посещенных

            # Отправка HTTP-запроса и получение содержимого веб-страницы
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            see_also = soup.find(id='See_also')
            if see_also is not None:
                see_also = see_also.find_next("ul").find_all("li")
                hrefs = []
                for item in see_also:
                    hrefs.append(item.a.get("href"))
                    graph.add_edge(url, url_begin + item.a.get("href"))
                    crawl(item.a.get("href"), level + 1)

            # Извлечение связанных URL из текущей страницы
            # links = soup.find_all('a')
            # for link in links:
            #     href = link.get('href')
            #     if href.startswith('http'):  # Проверка, что это внешний URL
            #         # Добавление связи между текущим URL и найденным URL
            #         graph.add_edge(url, href)
            #         # Рекурсивный вызов crawl для найденного URL
            #         crawl(href, level + 1)

    crawl(start_url, 0)  # Запуск процесса обхода веба

    return graph

# Пример использования


start_url = '/wiki/Six_degrees_of_separation'  # URL, с которого начинается обход
depth = 1  # Максимальный уровень обхода

graph = crawl_web(start_url, depth)  # Получение направленного графа

# Сохранение графа в файл JSON
data = nx.node_link_data(graph)
with open('graph.json', 'w') as f:
    json.dump(data, f)
