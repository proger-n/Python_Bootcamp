from py2neo import Graph, Node, Relationship
import json

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

graph.delete_all()

with open("wiki.json", "r") as f:
    data = json.load(f)

for key, value in data.items():
    node1 = Node("Topic", name=key)
    graph.create(node1)
    for v in value:
        node2 = Node("Topic", name=v)
        graph.create(node2)
        rel = Relationship(node1, "related_to", node2)
        graph.create(rel)
