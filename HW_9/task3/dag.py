class Graph:
  def __init__(self, graph):
    self.graph = graph
    self.cycle = False
    self.visited = {}
    self.path = []
    self.first_cycle = []
    self.order = []

  def _dfs_help(self, vertex):
      self.visited[vertex] = 0
      self.path.append(vertex)

      for neighbor in self.graph[vertex]:
        if neighbor not in self.visited:
          self._dfs_help(neighbor)
        # есть цикл  
        elif self.visited[neighbor] == 0 and not self.cycle:
          self.first_cycle = self.path + [neighbor]
          self.path = []
          self.cycle = True
      self.visited[vertex] = 1
      self.order.append(vertex)  


  def find_cycle(self):
    for vertex in self.graph.keys():
      if vertex not in self.visited:
        self._dfs_help(vertex)
    if not self.cycle:
      return "Цикла нет. Можно сделать топологическую сортировку."
    else:
      print("Цикл:")
      elem = self.first_cycle[-1]
      for k in range(len(self.first_cycle)):
        if self.first_cycle[k] == elem:
          return self.first_cycle[k::]
  
  def topological_sorting(self):
    if self.cycle:
        return "Нельзя построить топологическую сортировку — есть цикл"
    return self.order[::-1] 





graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": []
}

graph1 = Graph(graph)
print(graph1.find_cycle())
print(graph1.topological_sorting())