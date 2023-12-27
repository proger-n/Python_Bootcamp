import json
from collections import deque
from collections import defaultdict
import argparse

WIKI_FILE = 'wiki.json'

parser = argparse.ArgumentParser()
parser.add_argument("--from", dest='accumulate',
                    help="flag input start article")
parser.add_argument("--to", help="flag input end depth")
parser.add_argument("-v", action="store_true")
parser.add_argument("--non-directed", dest='non_dir', action="store_true")
args = parser.parse_args()

if args.accumulate:
    start_node = args.accumulate.replace(" ", "_").lower()
if args.to:
    end_node = args.to.replace(" ", "_").lower()


def find_shortest_path(graph, start_node, end_node):
    neighbors = defaultdict(list)
    for node, neighbors_list in graph.items():
        for neighbor in neighbors_list:
            neighbors[node].append(neighbor)

    visited = set()

    queue = [(start_node, [start_node])]

    shortest_path = None

    while queue:
        current_node, path = queue.pop(0)

        if current_node == end_node:
            if shortest_path is None or len(path) < len(shortest_path):
                shortest_path = path
            continue

        visited.add(current_node)

        for neighbor in neighbors[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return shortest_path


with open(WIKI_FILE) as file:
    graph = json.load(file)


shortest_path = find_shortest_path(graph, start_node, end_node)

if shortest_path:
    if args.v:
        print(*shortest_path, sep=" -> ")
        print(len(shortest_path)-1)
    else:
        print(len(shortest_path)-1)
else:
    if args.non_dir:
        shortest_path = find_shortest_path(graph, end_node, start_node)
        if args.v:
            print(*shortest_path, sep=" -> ")
            print(len(shortest_path)-1)
        else:
            print(len(shortest_path)-1)
    else:
        print("Path not found")
