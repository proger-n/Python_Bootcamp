import json


with open('wiki.json', 'r') as file:
    graph = json.load(file)

path_len = []
dep = 0
start = 'Erdős_number'
end = 'Graph_theory'
saw = set()
# print(graph.keys())


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
