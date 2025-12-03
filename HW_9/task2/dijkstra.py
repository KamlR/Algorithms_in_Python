import heapq
def dijkstra(graph, start):
  distances = {vertex: float('inf') for vertex in graph}
  distances[start] = 0
  heap = [(0, start)]

  while heap:
    current_distance, current_vertex = heapq.heappop(heap)

    if current_distance > distances[current_vertex]:
      continue

    for neighbor, weight in graph[current_vertex]:
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(heap, (distance, neighbor))
  return distances


graph = {
    'A': [('B', 10), ('E', 100), ('D', 30)],
    'B': [('C', 50)],
    'C': [('E', 10)],
    'D': [('C', 20), ('E', 60)],
    'E': []
}

print(dijkstra(graph, 'A'))


