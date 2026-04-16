from graph import Graph
from heap import MaxHeap
from hashmap import HashMap
from trie import Trie


def load_network(file_path):
    graph = Graph()
    package_heap = MaxHeap()
    depot_map = HashMap()
    trie = Trie()

    section = None

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line == "NODES":
                section = "NODES"
                continue
            elif line == "EDGES":
                section = "EDGES"
                continue
            elif line == "PACKAGES":
                section = "PACKAGES"
                continue

            if section == "NODES":
                nodes = line.split()
                for node in nodes:
                    graph.add_node(node)
                    trie.insert(node)
                    depot_map.insert(node, {
                        "location": f"{node} Area",
                        "capacity": 100,
                        "active": True
                    })

            elif section == "EDGES":
                src, dest, weight = line.split()
                graph.add_edge(src, dest, int(weight))

            elif section == "PACKAGES":
                package_id, priority, destination, weight_kg = line.split()
                package_heap.enqueue({
                    "package_id": package_id,
                    "priority": int(priority),
                    "destination": destination,
                    "weight_kg": float(weight_kg)
                })

    return graph, package_heap, depot_map, trie
