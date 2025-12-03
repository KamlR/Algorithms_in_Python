from dijkstra import dijkstra

def test_dijkstra():
  graph1 = {
    'A': [('B', 10), ('E', 100), ('D', 30)],
    'B': [('C', 50)],
    'C': [('E', 10)],
    'D': [('C', 20), ('E', 60)],
    'E': []
  }
  assert dijkstra(graph1, "A") == {"A" : 0, "B" : 10, "C" : 50, "D" : 30, "E" : 60 }

  graph2 = {
    'A': [('B', 10)],
    'B': [('C', 20)],
    'C': [('D', 30)],
    'D': []
  }
  assert dijkstra(graph2, "A") == {"A" : 0, "B" : 10, "C" : 30, "D" : 60}

  graph3 = {
    'A': [('B', 10)],
    'B': [('C', 20)],
    'C': [('D', 30)],
    'D': [('E', 40)],
    'E': []
  }
  assert dijkstra(graph3, "A") == {"A" : 0, "B" : 10, "C" : 30, "D" : 60, "E" : 100}

  graph4 = {
    'A': [('B', 10), ('B', 5), ('C', 5)],
    'B': [('C', 20)],
    'C': [('D', 30)],
    'D': [('E', 40)],
    'E': []
  }
  assert dijkstra(graph4, "A") == {"A" : 0, "B" : 5, "C" : 5, "D" : 35, "E" : 75}

  # 5 компонент связности = кол-ву вершин
  graph5 = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': []
  }
  assert dijkstra(graph5, "A") == {"A" : 0, "B" : float("inf"), "C" : float("inf"), "D" : float("inf"), "E" : float("inf")}

  # вершина E, до которой из A добраться невозможно
  graph6 = {
    'A': [('C', 40), ('D', 5), ('B', 100)],
    'B': [],
    'C': [],
    'D': [('B', 20), ('C', 10)],
    'E': [('D', 40)]
  }
  assert dijkstra(graph6, "A") == {"A" : 0, "B" : 25, "C" : 15, "D" : 5, "E" : float("inf")}
