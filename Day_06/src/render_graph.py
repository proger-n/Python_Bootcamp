import json
import networkx as nx
import matplotlib.pyplot as plt


def render_wiki_graph():
    # Load the graph from the JSON file
    with open('wiki.json', 'r') as file:
        graph = json.load(file)

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges to the graph
    for page, links in graph.items():
        G.add_node(page)
        for link in links:
            G.add_edge(link, page)

    # Calculate node sizes based on the number of incoming connections
    node_sizes = [G.in_degree(node) * 100 for node in G.nodes()]

    # Render the graph
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, alpha=0.7)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw_networkx_labels(G, pos, font_size=8)
    plt.axis('off')

    # Save the graph as a PNG image
    plt.savefig('wiki_graph.png', format='png')
    plt.close()

    print("Graph rendered successfully as wiki_graph.png.")


if __name__ == "__main__":
    render_wiki_graph()
