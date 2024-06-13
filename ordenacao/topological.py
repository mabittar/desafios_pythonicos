from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.entries = set()
        self.n: int = 0

    def add_edge(self, u, v):
        self.entries.add(u)
        self.entries.add(v)
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                try:
                    self.topological_sort_util(neighbor, visited, stack)
                except KeyError:
                    continue
        stack.append(v)

    def topological_sort(self):
        self.n = len(self.entries)
        visited = {v: False for v in self.entries}

        stack = []
        for vertex in self.entries:
            if not visited[vertex]:
                self.topological_sort_util(vertex, visited, stack)

        # Inverte a ordem do stack para obter a ordenação topológica
        return stack


if __name__ == '__main__':
    try:
        g = Graph()
        g.add_edge('A', 'B')
        g.add_edge('A', 'C')
        g.add_edge('B', 'D')
        g.add_edge('C', 'D')
        g.add_edge('D', 'E')

        result = g.topological_sort()
        print("Ordenação topológica:")
        for vertex in result:
            print(vertex, end=' ')

    except Exception as e:
        print(e)
    finally:
        print("Done!")
