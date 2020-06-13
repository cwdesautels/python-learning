import sys
from dataclasses import dataclass, field


@dataclass
class Edge:
    src: str
    dest: str
    weight: int


@dataclass
class Graph:
    edges: dict = field(default_factory=dict)

    def add_edge(self, src: str, dst: str, weight: int):
        self.edges[src] = Edge(src, dst, int(weight))


def find_connections():
    # write your code here
    return []


def main():
    network = Graph()

    number_of_flights = int(sys.stdin.readline())
    for _ in range(number_of_flights):
        network.add_edge(*sys.stdin.readline().strip().split(" "))
    print(network)
    limit = int(sys.stdin.readline())
    source_airport, destination_airport = sys.stdin.readline().strip().split(' ')

    connections = find_connections()
    for connection in connections:
        # print connections
        print()


if __name__ == '__main__':
    main()
