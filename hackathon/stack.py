# Stack with O(1) depth check
class Node:
    value: str = None
    next = None
    pos: int = 1

    def __init__(self, value: str):
        self.value = value


class Stack:
    root: Node = None

    def depth(self) -> int:
        if self.root:
            return self.root.pos
        else:
            return 0

    def pop(self) -> str:
        node = self.root

        if node:
            self.root = node.next
            return node.value
        else:
            return None

    def push(self, data: str) -> str:
        if data is not None:
            node = Node(data)
            node.next = self.root

            if self.root:
                node.pos = self.root.pos + 1
            self.root = node

        return data


s = Stack()
print("depth: %s" % s.depth())
print("pushing: %s" % s.push("a"))
print("depth: %s" % s.depth())
print("pushing: %s" % s.push("b"))
print("depth: %s" % s.depth())
print("pushing: %s" % s.push("c"))
print("depth: %s" % s.depth())
print("popping: %s" % s.pop())
print("depth: %s" % s.depth())
print("popping: %s" % s.pop())
print("depth: %s" % s.depth())
print("popping: %s" % s.pop())
print("depth: %s" % s.depth())
