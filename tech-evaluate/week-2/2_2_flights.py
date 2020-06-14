import sys
import functools
from dataclasses import dataclass, field


@dataclass
class Graph:
    edges: dict = field(default_factory=dict)

    def add_edge(self, src: str, dst: str, weight: int):
        if src not in self.edges:
            self.edges[src] = dict()
        self.edges[src][dst] = int(weight)


def path_comparator(a: list, b: list) -> int:
    result = a[-1] - b[-1]

    if result == 0:
        result = len(a) - len(b)
        if result == 0:
            a_str = " ".join(a[:-1])
            b_str = " ".join(b[:-1])
            if a_str < b_str:
                return -1
            elif a_str > b_str:
                return 1
            else:
                return 0

    return result


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
            for current_neighbour in network.edges[node] if node in network.edges else {}:
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
            visited.add(node)
    return all_paths


def find_connections(src: str, dst: str, limit: int, network: Graph) -> list:
    paths = bfs(src, dst, network)
    if paths:
        for path in paths:
            cost = 0
            i = 0
            for i in range(len(path) - 1):
                cost += network.edges[path[i]][path[i+1]]
            path.append(cost)
        paths.sort(key=functools.cmp_to_key(path_comparator))
        return paths[:limit]
    else:
        return [["<no solution>"]]


def main():
    network = Graph()
    number_of_flights = int(sys.stdin.readline())

    for _ in range(number_of_flights):
        network.add_edge(*sys.stdin.readline().strip().split(" "))

    # print(network)
    limit = int(sys.stdin.readline())
    src, dst = sys.stdin.readline().strip().split(" ")
    connections = find_connections(src, dst, limit, network)

    for connection in connections:
        print(*connection)


if __name__ == '__main__':
    main()
