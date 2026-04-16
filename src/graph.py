from heap import MinHeap


class Graph:
    def __init__(self):
        self.adj = {}
        self.edge_count = 0

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, src, dest, weight):
        self.add_node(src)
        self.add_node(dest)
        self.adj[src].append((dest, weight))
        self.edge_count += 1

    def get_nodes(self):
        return list(self.adj.keys())

    def display_summary(self):
        print("\n--- Network Summary ---")
        print(f"Number of nodes: {len(self.adj)}")
        print(f"Number of edges: {self.edge_count}")
        print(f"Connected components: {self.connected_components_count()}")

    def connected_components_count(self):
        visited = set()
        count = 0

        undirected = {node: [] for node in self.adj}
        for node in self.adj:
            for neighbor, _ in self.adj[node]:
                undirected[node].append(neighbor)
                undirected[neighbor].append(node)

        for node in undirected:
            if node not in visited:
                count += 1
                self._dfs_undirected(node, visited, undirected)

        return count

    def _dfs_undirected(self, node, visited, undirected):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                for neighbor in undirected[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    def dijkstra(self, start, end):
        if start not in self.adj or end not in self.adj:
            return None, float("inf")

        distances = {node: float("inf") for node in self.adj}
        previous = {node: None for node in self.adj}
        distances[start] = 0

        heap = MinHeap()
        heap.push((0, start))

        while not heap.is_empty():
            current_distance, current_node = heap.pop()

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adj[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heap.push((distance, neighbor))

        if distances[end] == float("inf"):
            return None, float("inf")

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()

        return path, distances[end]

    def detect_cycles(self):
        WHITE = 0
        GRAY = 1
        BLACK = 2

        color = {node: WHITE for node in self.adj}
        cycle_nodes = set()

        def dfs(node, path_stack):
            color[node] = GRAY
            path_stack.append(node)

            for neighbor, _ in self.adj[node]:
                if color[neighbor] == WHITE:
                    dfs(neighbor, path_stack)
                elif color[neighbor] == GRAY:
                    cycle_start = path_stack.index(neighbor)
                    for n in path_stack[cycle_start:]:
                        cycle_nodes.add(n)

            path_stack.pop()
            color[node] = BLACK

        for node in self.adj:
            if color[node] == WHITE:
                dfs(node, [])

        return list(cycle_nodes)
