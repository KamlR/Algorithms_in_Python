def dfs(start_vertex, graph, visited):
  stack = [start_vertex]
  component = []
  while stack:
    v = stack.pop()
    if v not in visited:
      component.append(v)
      visited.add(v)
      stack.extend(graph[v])  
  return component

  
def find_connected_components(graph):
  visited = set()
  components = []
  for vertex in graph:
    if vertex not in visited:
      # начало новой компоненты связности
      component = dfs(vertex, graph, visited)
      components.append(component)
  return components


graph = {
    3: [4, 6],
    4: [3, 5, 6],
    3: [6, 4],
    5: [4],
    6: [3, 4],
    7: [8],
    8: [7]
}


for vertex_amount in range(1, 4 + 1):
    graph = {}
    for j in range(1, vertex_amount + 1):
      graph[j] = [x for x in range(1, vertex_amount + 1) if x != j]
    result = find_connected_components(graph)
    res = sorted([sorted(c) for c in result])
    print(graph)
