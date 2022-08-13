from copy import deepcopy
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    nodes = []

    def __init__(self, value: Any):
        self.value = value
        Node.nodes.append(self)
        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root
        self.crutch = deepcopy(Node.nodes)

    def dfs(self) -> list[Node]:
        def recursion(node: Node, stack: list[Node]):
            if not node.outbound:
                return stack
            for i in range(len(node.outbound)):
                if node.outbound[i] not in stack:
                    stack.append(node.outbound[i])
                    recursion(node=stack[-1], stack=stack)
            return stack
        answer = recursion(node=self._root, stack=[self._root, ])
        Node.nodes.clear()
        return answer

    def bfs(self) -> list[Node]:
        if Node.nodes:
            answer = [self._root, ]
            for node in self.crutch:
                answer.extend([out for out in node.outbound if out.value not in list(map(lambda n: n.value, answer))])
            Node.nodes.clear()
            return answer
        else:
            answer = [self._root, ]
            for node in self.crutch:
                answer.extend([out for out in node.outbound if out.value not in list(map(lambda n: n.value, answer))])
            self.crutch.clear()
            return answer
