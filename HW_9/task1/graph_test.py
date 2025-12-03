from graph import find_connected_components

"""
Одна компонента связности.
"""
def test_one_connected_component():
  graph1 = {
    3: [4, 6],
    4: [3, 5, 6],
    3: [6, 4],
    5: [4],
    6: [3, 4]
  }
  result1 = find_connected_components(graph1)
  res1 = sorted([sorted(c) for c in result1])
  assert res1 == [[3, 4, 5, 6]]

  graph2 = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3]
  }
  result2 = find_connected_components(graph2)
  res2 = sorted([sorted(c) for c in result2])
  assert res2 == [[1, 2, 3, 4]]

  graph3 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4],
    4: [3]
  }
  result3 = find_connected_components(graph3)
  res3 = sorted([sorted(c) for c in result3])
  assert res3 == [[1, 2, 3, 4]]

  # каждая вершина связана с каждой
  for vertex_amount in range(1, 10 + 1):
    graph = {}
    for j in range(1, vertex_amount + 1):
      graph[j] = [x for x in range(1, vertex_amount + 1) if x != j]
    result = find_connected_components(graph)
    res = sorted([sorted(c) for c in result])
    assert res == [list(range(1, vertex_amount + 1))]


"""
Две компоненты связности.
"""
def test_two_connected_component():
  graph1 = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4]
  }
  result1 = find_connected_components(graph1)
  res1 = sorted([sorted(c) for c in result1])
  assert res1 == [[1, 2, 3], [4, 5]]

  graph2 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 6, 7],
    6: [3],
    7: [3],
    4: [5],
    5: [4, 9],
    9: [5]
  }
  result2 = find_connected_components(graph2)
  res2 = sorted([sorted(c) for c in result2])
  assert res2 == [[1, 2, 3, 6, 7], [4, 5, 9]]

  graph3 = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 6, 7],
    6: [3, 8],
    7: [3, 10],
    4: [5],
    5: [4, 9, 12],
    9: [5, 11],
    8: [6],
    10: [7],
    11: [9],
    12: [11, 5]
  }
  result3 = find_connected_components(graph3)
  res3 = sorted([sorted(c) for c in result3])
  assert res3 == [[1, 2, 3, 6, 7, 8, 10], [4, 5, 9, 11, 12]]

  # первая компонента связности из 4 вершин, вторая из одной.
  graph4 = {
    3: [4, 6],
    4: [3, 5, 6],
    3: [6, 4],
    5: [4],
    6: [3, 4],
    7: []
  }
  result4 = find_connected_components(graph4)
  res4 = sorted([sorted(c) for c in result4])
  assert res4 == [[3, 4, 5, 6], [7]]


"""
n компонент связностей, где n - число вершин.
"""
def test_many_connected_component():
  for vertex_amount in range(1, 10 + 1):
    graph = {}
    for j in range(1, vertex_amount + 1):
      graph[j] = {}
    result = find_connected_components(graph)
    res = sorted([sorted(c) for c in  result])
    assert res == [[i] for i in range(1, vertex_amount + 1)]

  
