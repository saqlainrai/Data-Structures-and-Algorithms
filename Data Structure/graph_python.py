
from collections import deque

class vertex:
    def __init__(self, data):
        self.data = data
        self.adjacent = []
        self.visited = False    

class edge:
    def __init__(self, source, destination, weight):
        self.weight = weight
        self.source = source
        self.destination = destination

class Graph:
    def __init__ (self):
        self._vertices = []
        self._edges = []
    
    def add_vertex(self, data):
        previous = self.find_vertex(data)
        if not previous:
            self._vertices.append(vertex(data))
    
    def add_edge(self, source, destination, weight):
        s = self.find_vertex(source)
        d = self.find_vertex(destination)
        if s and d:
            temp = edge(s, d, weight)
            self._edges.append(temp)
            s.adjacent.append(d)
            d.adjacent.append(s)
            print("Edge added.")
        else:
            print("Add valid vertices first.")
    
    def find_vertex(self, data):
        for vertex in self._vertices:
            if vertex.data == data:
                return vertex
        return None
    
    def dfs(self, start_vertex):                       # Depth First Search uses stack to implement
        for vertex in self._vertices:
            vertex.visited = False
        stack = [start_vertex]                # add the first vertex to the stack
        while stack:
            current_vertex = stack.pop()
            if not current_vertex.visited:  
                print(current_vertex.data, end=' ')
                current_vertex.visited = True

                # Add unvisited neighbors to the stack
                for n in reversed(current_vertex.adjacent):
                    if not n.visited:
                        stack.append(n)

    def bfs(self, start_vertex):                          # Breadth First Search uses queue to implement
        for vertex in self._vertices:
            vertex.visited = False
        queue = deque([start_vertex])

        while queue:
            current_vertex = queue.popleft()
            if not current_vertex.visited:
                print(current_vertex.data, end=' ')
                current_vertex.visited = True

                # Add unvisited neighbors to the queue
                for i in current_vertex.adjacent:
                    if not i.visited:
                        queue.append(i)
    
    def show(self):
        for vertex in self._vertices:
            print(vertex.data, end=": ")
            for i in vertex.adjacent:
                print(i.data, end=" ")
            print()

def main():
    g = Graph()
    print("Graph created.")
    g.add_vertex(9)
    g.add_vertex(1)
    g.add_vertex(11)
    g.add_vertex(7)
    # g.add_vertex(7)
    g.add_vertex(43)
    g.add_vertex(3)
    g.add_vertex(10)
    g.add_vertex(15)
    g.add_vertex(20)
    g.add_edge(11, 43, 10)
    g.add_edge(9, 7, 20)
    g.add_edge(9, 1, 20)
    g.add_edge(43, 7, 20)
    g.add_edge(20, 7, 20)
    g.add_edge(10, 3, 20)
    g.add_edge(1, 3, 20)
    g.add_edge(10, 1, 20)
    g.add_edge(10, 15, 20)
    # g.show()
    print("BFS: ")
    g.bfs(g.find_vertex(9))
    print() 
    print("DFS: ")
    g.dfs(g.find_vertex(9))

if __name__ == "__main__":
    main()