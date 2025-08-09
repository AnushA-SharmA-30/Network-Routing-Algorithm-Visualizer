import networkx as nx
import matplotlib.pyplot as plt
import heapq

class RoutingVisualizer:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_edge(self, u, v, weight):
        """Adds an edge to the graph."""
        self.graph.add_edge(u, v, weight=weight)

    def display_graph(self):
        """Displays the graph with weights."""
        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=15)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.title("Network Graph")
        plt.show()

    def dijkstra(self, source):
        """Visualizes Dijkstra's Algorithm."""
        print(f"\nRunning Dijkstra's Algorithm from source: {source}")
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[source] = 0
        pq = [(0, source)]

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.graph.neighbors(current_node):
                weight = self.graph[current_node][neighbor]['weight']
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        print("Shortest distances:", distances)
        self._highlight_shortest_path(distances, source)

    def bellman_ford(self, source):
        """Visualizes Bellman-Ford Algorithm."""
        print(f"\nRunning Bellman-Ford Algorithm from source: {source}")
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[source] = 0

        for _ in range(len(self.graph.nodes) - 1):
            for u, v, data in self.graph.edges(data=True):
                if distances[u] + data['weight'] < distances[v]:
                    distances[v] = distances[u] + data['weight']

        print("Shortest distances:", distances)
        self._highlight_shortest_path(distances, source)

    def _highlight_shortest_path(self, distances, source):
        """Highlights the shortest path on the graph."""
        shortest_paths = []
        for target in distances:
            if distances[target] < float('inf') and target != source:
                shortest_paths.append((source, target))

        pos = nx.spring_layout(self.graph)
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=15)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        nx.draw_networkx_edges(
            self.graph, pos,
            edgelist=shortest_paths,
            edge_color='red',
            width=2.5
        )
        plt.title("Shortest Path Highlighted")
        plt.show()

    def distance_vector_demo(self):
        """Simple demonstration of the Distance Vector Routing."""
        print("\nDistance Vector Routing:")
        for node in self.graph.nodes:
            print(f"Node {node}: {self._get_distance_vector(node)}")

    def _get_distance_vector(self, node):
        """Calculates the distance vector for a node."""
        distances = {n: float('inf') for n in self.graph.nodes}
        distances[node] = 0

        for neighbor in self.graph.neighbors(node):
            distances[neighbor] = self.graph[node][neighbor]['weight']

        return distances

    def link_state_demo(self):
        """Simple demonstration of Link-State Routing."""
        print("\nLink-State Routing:")
        for node in self.graph.nodes:
            print(f"Node {node} sends link state: {list(self.graph[node].items())}")


# Example Usage
if __name__ == "__main__":
    visualizer = RoutingVisualizer()

    # Create the graph
    visualizer.add_edge("A", "B", 1)
    visualizer.add_edge("A", "C", 4)
    visualizer.add_edge("B", "C", 2)
    visualizer.add_edge("B", "D", 6)
    visualizer.add_edge("C", "D", 3)

    visualizer.display_graph()

    # Visualize Dijkstra's Algorithm
    visualizer.dijkstra("A")

    # Visualize Bellman-Ford Algorithm
    visualizer.bellman_ford("A")

    # Demonstrate Distance Vector Routing
    visualizer.distance_vector_demo()

    # Demonstrate Link-State Routing
    visualizer.link_state_demo()
