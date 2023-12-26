import json
import argparse

path_len = []
dep = 0
start = 'Dog_training'.lower()
end = 'Man_bites_dog'.lower()
saw = set()
# print(graph.keys())

parser = argparse.ArgumentParser()
parser.add_argument("--from", dest='accumulate',
                    help="flag input start article")
parser.add_argument("--to", help="flag input end depth")

args = parser.parse_args()

if args.accumulate:
    start = args.accumulate.replace(" ", "_").lower()
if args.to:
    end = args.to.replace(" ", "_").lower()

with open('wiki.json', 'r') as file:
    graph = json.load(file)


def search(graph, start, end, dep):
    global path_len
    global saw
    if start not in graph:
        return
    dep += 1
    values = graph[start]
    # print(values)
    if end in values:
        path_len.append(dep)
    print(path_len)
    for v in values:
        if v not in saw:
            saw.add(v)
            search(graph, v, end, dep)


search(graph, start, end, dep)
