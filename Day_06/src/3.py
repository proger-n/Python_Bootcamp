import requests
import json
from bs4 import BeautifulSoup


def save_wiki_graph(start_url, max_depth, graph):

    if max_depth < 0:
        return

    # Get page content
    response = requests.get(start_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get page title
    title = soup.find('h1', {'id': 'firstHeading'}).text

    # Find all paragraphs containing links
    paragraphs = soup.find_all('p')
    links = []
    for paragraph in paragraphs:
        # Find all links in the current paragraph
        paragraph_links = paragraph.find_all('a')
        for link in paragraph_links:
            href = link.get('href')
            # Include only internal links to other Wikipedia pages
            if href and href.startswith('/wiki/'):
                # Remove "/wiki/" prefix from the link
                target = href[6:]
                links.append(target)

    # Find 'See also' section
    see_also_section = soup.find('span', {'id': 'See_also'})
    if see_also_section:
        # Find all links in the 'See also' section
        see_also_links = see_also_section.find_next('ul').find_all('a')
        for link in see_also_links:
            href = link.get('href')
            # Include only internal links to other Wikipedia pages
            if href and href.startswith('/wiki/'):
                # Remove "/wiki/" prefix from the link
                target = href[6:]
                links.append(target)

    # Add page and its links to the graph
    graph[title] = links

    # Recursively save the graph for linked pages
    global count
    for link in links:
        if count > 1000:
            break
        count += 1
        new_url = f"https://en.wikipedia.org/wiki/{link}"
        print(count, " ", new_url)
        save_wiki_graph(new_url, max_depth - 1, graph)


start_url = 'https://en.wikipedia.org/wiki/Six_degrees_of_separation'
max_depth = 3  # Maximum depth to explore
graph = {}  # The graph representation
count = 0

save_wiki_graph(start_url, max_depth, graph)

# Save the graph as a JSON file
with open('wiki.json', 'w') as file:
    json.dump(graph, file, indent=4)

print("Graph saved successfully as wiki.json.")
