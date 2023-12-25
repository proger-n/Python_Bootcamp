import json
import networkx as nx
import matplotlib.pyplot as plt


def render_wiki_graph():
    with open('wiki.json', 'r') as file:
        graph = json.load(file)

    G = nx.DiGraph()

    for page, links in graph.items():
        G.add_node(page)
        for link in links:
            G.add_edge(link, page)

    node_sizes = [G.in_degree(node) * 100 for node in G.nodes()]

    plt.figure(figsize=(17, 10))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, alpha=0.7)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, font_size=8)
    plt.axis('off')

    plt.savefig('wiki_graph.png', format='png')
    plt.show()
    plt.close()

    print("Graph rendered successfully as wiki_graph.png.")


if __name__ == "__main__":
    render_wiki_graph()
