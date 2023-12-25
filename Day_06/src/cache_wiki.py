import requests
import json
from bs4 import BeautifulSoup
import logging
import argparse
logging.basicConfig(level=logging.INFO)


def get_links(url):
    global counter
    response = requests.get("https://en.wikipedia.org/wiki/"+url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = []
    see_also = soup.find(id='See_also')
    if (see_also is not None):
        if see_also.find_next("ul").find(class_="portalbox-entry"):
            see_also = see_also.find_next("ul")
        for link in see_also.find_next("ul").find_all("li"):
            if counter > 200:
                break
            try:
                href = link.a.get('href').split("/")[-1]
                links.append(href)
                logging.info(counter)
                logging.info(href)
                counter += 1
            except AttributeError:
                break

    return links


def build_graph(url, depth, graph):
    global visited
    if depth == 0:
        return

    if url not in visited:
        visited.add(url)
        links = get_links(url)
        graph[url.split("/")[-1]] = links
        for link in links:
            build_graph(link, depth-1, graph)


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--text",
                    help="flag input article")
parser.add_argument("-d", "--dep",
                    help="flag input depth")
args = parser.parse_args()
start_url = 'Six_degrees_of_separation'
depth = 3
if args.text:
    start_url = args.text
if args.dep:
    depth = int(args.dep)
graph = {}
counter = 0
visited = set()
build_graph(start_url, depth, graph)

with open('wiki.json', 'w') as outfile:
    json.dump(graph, outfile, indent=4)
