import requests
from bs4 import BeautifulSoup
import networkx as nx
import json
import matplotlib.pyplot as plt
import logging
from time import sleep
from random import random


def crawl_web(start_url, depth):
    visited = set()  # Словарь для отслеживания посещенных страниц
    graph = nx.DiGraph()  # Создание направленного графа

    def crawl(name, url, level):
        global counter
        url_begin = 'https://en.wikipedia.org'
        url = url_begin + url
        # Проверка, посещали ли мы эту страницу и достигнут ли максимальный уровень
        if url not in visited and level <= depth:
            counter += 1
            logging.info(counter)
            logging.info(url)
            visited.add(url)  # Добавляем текущий URL в список посещенных

            # Отправка HTTP-запроса и получение содержимого веб-страницы
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            see_also = soup.find(id='See_also')
            if (see_also is not None):
                see_also = see_also.find_next("ul").find_all("li")
                # hrefs = []
                for item in see_also:
                    if counter > 100:
                        break
                    # hrefs.append(item.a.get("href"))
                    try:
                        graph.add_edge(
                            name, item.a.get("href"))
                        crawl(item.a.get("href"), item.a.get("href"), level + 1)
                        # sleep(random())
                    except AttributeError:
                        break

    # Запуск процесса обхода веба
    crawl(start_url.split('/')[-1], start_url, 0)

    return graph


# Пример использования
logging.basicConfig(level=logging.INFO)
counter = 0
start_url = '/wiki/Six_degrees_of_separation'  # URL, с которого начинается обход
depth = 3  # Максимальный уровень обхода

graph = crawl_web(start_url, depth)  # Получение направленного графа

# Сохранение графа в файл JSON
data = nx.node_link_data(graph)
with open('wiki.json', 'w') as f:
    json.dump(data, f)

# Строим граф с помощью matplotlib
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
nx.draw_networkx_edges(graph, pos, edge_color='gray')

# Отображаем граф
plt.show()

# Сохраняем граф в формате PNG
# plt.savefig('graph.png')

# nx.draw(graph, with_labels=True)
plt.savefig('plotgraph.png', dpi=500, bbox_inches='tight')
# plt.show()
