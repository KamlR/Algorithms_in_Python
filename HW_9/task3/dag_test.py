from dag import Graph

def test_no_cycle():
  graph1 = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D"],
    "D": []
  }
  graph_object1 = Graph(graph1)
  assert graph_object1.find_cycle() == "Цикла нет. Можно сделать топологическую сортировку."
  assert graph_object1.topological_sorting() == ["A", "B", "C", "D"]

  graph2 = {
    "A": ["B", "D"],
    "B": ["C"],
    "C": ["E", "D"],
    "D": ["E"],
    "E": []
  }
  graph_object2 = Graph(graph2)
  assert graph_object2.find_cycle() == "Цикла нет. Можно сделать топологическую сортировку."
  assert graph_object2.topological_sorting() == ["A", "B", "C", "D", "E"]

  # две компоненты связности без циклов
  graph3 = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": [],
    "D": ["E"],
    "E": []
  }
  graph_object3 = Graph(graph3)
  assert graph_object3.find_cycle() == "Цикла нет. Можно сделать топологическую сортировку."
  assert graph_object3.topological_sorting() == ["D", "E", "A", "B", "C"]

  graph4 = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": []
  }
  graph_object4 = Graph(graph4)
  assert graph_object4.find_cycle() == "Цикла нет. Можно сделать топологическую сортировку."
  assert graph_object4.topological_sorting() == ["E", "D", "C", "B", "A"]

  graph5 = {
    "A": ["B", "D", "C", "E"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["E"],
    "E": []
  }
  graph_object5 = Graph(graph5)
  assert graph_object5.find_cycle() == "Цикла нет. Можно сделать топологическую сортировку."
  assert graph_object5.topological_sorting() == ["A", "C", "B", "D", "E"]


def test_cycle():
  graph1 = {
    "A": ["B"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["A"],
    "E": ["D"]
  }
  graph_object1 = Graph(graph1)
  assert graph_object1.find_cycle() == ["A", "B", "C", "E", "D", "A"]

  graph2 = {
    "A": ["B"],
    "B": ["D", "C"],
    "C": ["E"],
    "D": ["A"],
    "E": ["D"]
  }
  graph_object2 = Graph(graph2)
  assert graph_object2.find_cycle() == ["A", "B", "D", "A"]


  graph3 = {
    "A": ["B"],
    "B": ["A", "D", "C"],
    "C": ["E"],
    "D": ["A"],
    "E": ["D"]
  }
  graph_object3 = Graph(graph3)
  assert graph_object3.find_cycle() == ["A", "B", "A"]

  graph4 = {
    "A": ["B"],
    "B": ["E", "C"],
    "C": ["B"],
    "D": ["A"],
    "E": ["D", "C"]
  }
  graph_object4 = Graph(graph4)
  assert graph_object4.find_cycle() == ["A", "B", "E", "D", "A"]



