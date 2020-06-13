import sys
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Edge:
    src: str
    dest: str
    weight: int


@dataclass
class Graph:
    edges: dict = field(default_factory=dict)

    def add_edge(self, src: str, dst: str, weight: int):
        if src not in self.edges:
            self.edges[src] = dict()
        self.edges[src][dst] = Edge(src, dst, int(weight))

    def get_neighbours(self, node: str):
        return self.edges[node] if node in self.edges else {}


def bfs(src: str, dst: str, network: Graph):
    queue = [[src]]
    visited = set()
    all_paths = list()
    while queue:
        path = queue.pop()
        node = path[-1]
        if node == dst:
            all_paths.append(path)
        elif node not in visited:
            for current_neighbour in network.get_neighbours(node):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
            visited.add(node)
    return all_paths


def find_connections(src: str, dst: str, limit: int, network: Graph) -> list:
    return bfs(src, dst, network)


def main():
    network = Graph()
    number_of_flights = int(sys.stdin.readline())

    for _ in range(number_of_flights):
        network.add_edge(*sys.stdin.readline().strip().split(" "))

    print(network)
    limit = int(sys.stdin.readline())
    src, dst = sys.stdin.readline().strip().split(" ")
    connections = find_connections(src, dst, limit, network)

    for connection in connections:
        print(*connection)


if __name__ == '__main__':
    main()
