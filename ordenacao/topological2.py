from graphlib import TopologicalSorter



if __name__ == '__main__':
    try:
        # Cria um objeto TopologicalSorter
        g = TopologicalSorter()
        # g.add('A', 'B')
        # g.add('A', 'C')
        g.add('A', ['B', 'C'])
        g.add('B', 'D')
        g.add('C', 'D')
        g.add('D', 'E')

        result = list(g.static_order())
        print("Ordenação topológica:")
        for vertex in result:
            print(vertex, end=' ')

    except Exception as e:
        print(e)
    finally:
        print("Done!")
