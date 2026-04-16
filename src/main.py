from utils import load_network


def main():
    file_path = "data/network.txt"

    try:
        graph, package_heap, depot_map, trie = load_network(file_path)
    except FileNotFoundError:
        print("Error: data/network.txt not found.")
        return

    while True:
        print("\n===== Smart Network Logistics Engine =====")
        print("1. Display Network Summary")
        print("2. Find Shortest Path")
        print("3. Detect Cycles")
        print("4. Dispatch Highest-Priority Package")
        print("5. Search Depot by Name")
        print("6. Autocomplete Depot Name")
        print("7. Exit")
        print("==========================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            graph.display_summary()

        elif choice == "2":
            source = input("Enter source node: ").strip()
            destination = input("Enter destination node: ").strip()
            path, cost = graph.dijkstra(source, destination)

            if path is None:
                print("No path found.")
            else:
                print("Shortest path:", " -> ".join(path))
                print("Total cost:", cost)

        elif choice == "3":
            cycles = graph.detect_cycles()
            if cycles:
                print("Cycle detected.")
                print("Nodes involved:", ", ".join(cycles))
            else:
                print("No cycles found.")

        elif choice == "4":
            package = package_heap.dequeue()
            if package is None:
                print("No packages to dispatch.")
            else:
                print("Dispatching package:")
                print(
                    f"ID: {package['package_id']}, "
                    f"Priority: {package['priority']}, "
                    f"Destination: {package['destination']}, "
                    f"Weight: {package['weight_kg']} kg"
                )

        elif choice == "5":
            name = input("Enter depot name: ").strip()
            result = depot_map.search(name)
            if result is None:
                print("Depot not found.")
            else:
                print("Depot found:")
                print(result)

        elif choice == "6":
            prefix = input("Enter prefix: ").strip()
            matches = trie.autocomplete(prefix)
            if matches:
                print("Matches:", ", ".join(matches))
            else:
                print("No matching depots found.")

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
