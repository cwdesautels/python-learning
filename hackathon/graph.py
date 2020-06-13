class Node:
    value: str = None

    def __init__(self, value: str):
        self.value = value

    def __repr__(self) -> str:
        return self.value


class Graph:
    edges: dict = dict()

    def addChild(self, parent: Node, child: Node, weight=1) -> None:
        self.edges[(parent, child)] = weight

    def addParent(self, parent: Node, child: Node, weight=1) -> None:
        self.edges[(child, parent)] = weight

    def getChildren(self, node: Node) -> set:
        children = set()
        for edge in self.edges:
            if node is edge[0]:
                children.add(edge[1])
        return children

    def getParents(self, node: Node) -> set:
        parents = set()
        for edge in self.edges:
            if node is edge[1]:
                parents.add(edge[0])
        return parents

    def getDescendants(self, node: Node) -> set:
        descendants = set()
        for child in self.getChildren(node):
            descendants.add(child)
            descendants |= self.getDescendants(child)
        return descendants

    def getAncestors(self, node: Node) -> set:
        ancestors = set()
        for parent in self.getParents(node):
            ancestors.add(parent)
            ancestors |= self.getAncestors(parent)
        return ancestors


relationships = Graph()
football = Node("Football")
player = Node("Player")
competition = Node("Competition")
champtionsLeague = Node("Champtions League")
premierLeague = Node("Premier League")
manUtd = Node("Manchester United")
manCity = Node("Manchester City")

relationships.addChild(football, player)
relationships.addChild(football, competition)
relationships.addChild(competition, champtionsLeague)
relationships.addChild(competition, premierLeague)
relationships.addChild(champtionsLeague, manUtd)
relationships.addChild(premierLeague, manUtd)
relationships.addChild(premierLeague, manCity)

print("Children of %s: %s" % (football, relationships.getChildren(football)))
print("Children of %s: %s" % (player, relationships.getChildren(player)))
print("Children of %s: %s" %
      (premierLeague, relationships.getChildren(premierLeague)))
print("Parents of %s: %s" % (football, relationships.getParents(football)))
print("Parents of %s: %s" % (player, relationships.getParents(player)))
print("Parents of %s: %s" % (manUtd, relationships.getParents(manUtd)))
print("Descendants of %s: %s" %
      (football, relationships.getDescendants(football)))
print("Descendants of %s: %s" % (player, relationships.getDescendants(player)))
print("Descendants of %s: %s" %
      (premierLeague, relationships.getDescendants(premierLeague)))
print("Ancestors of %s: %s" %
      (football, relationships.getAncestors(football)))
print("Ancestors of %s: %s" % (player, relationships.getAncestors(player)))
print("Ancestors of %s: %s" %
      (manUtd, relationships.getAncestors(manUtd)))
