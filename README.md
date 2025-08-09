# Network-Routing-Algorithm-Visualizer
Its main purpose is to demonstrate and visualize how fundamental routing algorithms determine the shortest path for data in a network.
🌐 Network Routing Algorithm Visualizer
This project is a Python-based tool for visualizing fundamental network routing algorithms and concepts. It uses networkx to create network topologies and matplotlib to display them, providing a clear visual aid for understanding how data packets find the most efficient path from a source to a destination.

This tool is perfect for students and enthusiasts of computer networking who want to see theoretical algorithms in action.

📜 Core Concepts Demonstrated
The script implements and demonstrates the following core networking concepts:

1. Dijkstra's Algorithm 🗺️
A cornerstone algorithm used in Link-State routing protocols (like OSPF). It calculates the shortest path from a single source node to all other nodes in a graph with non-negative edge weights. The visualizer calculates these paths and prints the final distance table.

2. Bellman-Ford Algorithm 🧮
The fundamental algorithm behind Distance-Vector routing protocols (like RIP). It also computes the shortest paths from a single source, with the key advantage of being able to handle graphs with negative edge weights (though none are used in this demo).

3. Link-State vs. Distance-Vector
The project provides a simple demonstration of the information at the heart of the two major intra-domain routing strategies:

Link-State Demo: It shows the information that a router would broadcast in a Link-State protocol—a list of its directly connected neighbors and the cost of the link to each (Node A sends link state: [('B', {'weight': 1}), ('C', {'weight': 4})]). Every router gets a complete map of the network.

Distance-Vector Demo: It shows a router's initial routing table in a Distance-Vector protocol, containing only the cost to its immediate neighbors (Node A: {'A': 0, 'B': 1, 'C': 4, 'D': inf}). Routers learn about the rest of the network through "routing by rumor" from their neighbors.

⚙️ How It Works
Graph Creation: The script initializes a directed graph using networkx. Edges are added with a weight attribute, representing the cost of traversing that link.

Initial Visualization: The complete network graph is displayed, showing all nodes, links, and their respective costs.

Algorithm Execution:

The dijkstra() and bellman_ford() methods are called for a specified source node.

Each algorithm calculates the shortest distance to all other nodes.

The final distance dictionary (e.g., {'A': 0, 'B': 1, 'C': 3, 'D': 6}) is printed to the console.

Results Visualization: After each algorithm runs, a new plot is shown. Note: The current visualization highlights the direct connection from the source to the final destinations, rather than tracing the full multi-hop path.
