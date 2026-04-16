# Smart Network Logistics Engine (SNLE)

**Name:** Pranik Goley  
**Student ID:** 300215208
## Project Overview
This project is a command-line Smart Network Logistics Engine (SNLE). It models a delivery network as a weighted directed graph. The program can load nodes, edges, and packages from a file, then perform route finding, cycle detection, package dispatching, depot lookup, and autocomplete search.

## How to Run
Make sure you are inside the project folder, then run:

```bash
python src/main.py
```

## Repository Structure
```bash
snle/
├── src/
│   ├── main.py
│   ├── graph.py
│   ├── heap.py
│   ├── hashmap.py
│   ├── trie.py
│   └── utils.py
├── data/
│   └── network.txt
├── README.md
└── requirements.txt
```

## Module Description

### main.py
Handles the CLI menu and connects all modules together.

### graph.py
Implements the graph using an adjacency list.
Functions:
- add_node
- add_edge
- display_summary
- connected_components_count
- dijkstra
- detect_cycles

### heap.py
Implements:
- MinHeap for Dijkstra’s algorithm
- MaxHeap for priority package dispatch

### hashmap.py
Implements a custom hash map using chaining.
Functions:
- insert
- search
- delete
- resize when load factor > 0.7

### trie.py
Implements a Trie for prefix-based depot autocomplete.

### utils.py
Loads the network data from `data/network.txt` and builds:
- graph
- package heap
- hash map
- trie

## Time and Space Complexity

### Graph Construction
- Time: O(V + E)
- Space: O(V + E)

### Dijkstra’s Algorithm
- Time: O((V + E) log V)
- Space: O(V)

### Cycle Detection using DFS Coloring
- Time: O(V + E)
- Space: O(V)

### Connected Components
- Time: O(V + E)
- Space: O(V)

### MinHeap / MaxHeap Insert and Remove
- Time: O(log n)
- Space: O(n)

### Hash Map
- Insert/Search/Delete average case: O(1)
- Worst case: O(n)
- Space: O(n)

### Trie Autocomplete
- Insert: O(L)
- Prefix search: O(P + k)
Where:
- L = length of word
- P = length of prefix
- k = number of characters visited in matching subtree

## Sample Run

```txt
===== Smart Network Logistics Engine =====
1. Display Network Summary
2. Find Shortest Path
3. Detect Cycles
4. Dispatch Highest-Priority Package
5. Search Depot by Name
6. Autocomplete Depot Name
7. Exit
==========================================
Enter your choice: 1

--- Network Summary ---
Number of nodes: 6
Number of edges: 6
Connected components: 1
```

## Bonus Features
None implemented.

## Notes
This project uses custom data structures instead of Python built-in priority queue libraries for the main heap requirement.
