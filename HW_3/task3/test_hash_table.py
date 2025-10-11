from hash_table import HashTable
import pytest

def test_insert_and_get_size():
  table = HashTable()
  assert table.get_size() == 0

  table.insert(10, 12)
  assert table.get_size() == 1

  table.insert(11, 13)
  assert table.get_size() == 2

  table.insert(12, 14)
  assert table.get_size() == 3

  table.insert(12, 15)
  assert table.get_size() == 3

def test_setitem_and_get_size():
  table = HashTable()

  table[10] = 12
  assert table.get_size() == 1

  table[11] = 13
  assert table.get_size() == 2

  table[12] = 14
  assert table.get_size() == 3

  table[12] = 15
  assert table.get_size() == 3


def test_insert_and_get():
  table = HashTable()

  table.insert(10, 12)
  assert table.get(10) == 12

  table.insert(11, 13)
  assert table.get(11) == 13

  table.insert(12, 14)
  assert table.get(12) == 14

  table.insert(12, 15)
  assert table.get(12) == 15

  assert table.get(20) == None


def test_setitem_and_get():
  table = HashTable()

  table[10] = 12
  assert table.get(10) == 12

  table[11] = 13
  assert table.get(11) == 13

  table[12] = 14
  assert table.get(12) == 14

  table[12] = 15
  assert table.get(12) == 15

  assert table.get(20) == None


def test_insert_and_getitem():
  table = HashTable()

  table.insert(10, 12)
  assert table[10] == 12

  table.insert(11, 13)
  assert table[11] == 13

  table.insert(12, 14)
  assert table[12] == 14

  table.insert(12, 15)
  assert table[12] == 15

  with pytest.raises(KeyError):
     print(table[20])


def test_setitem_and_getitem():
  table = HashTable()

  table[10] = 12
  assert table[10] == 12

  table[11] = 13
  assert table[11] == 13

  table[12] = 14
  assert table[12] == 14

  table[12] = 15
  assert table[12] == 15

  with pytest.raises(KeyError):
     print(table[20])

def test_delete():
  table = HashTable()
  with pytest.raises(KeyError):
     table.delete(10)
  
  table.insert(10, 11)
  table.insert(12, 13)
  table[13] = 14
  assert table.get_size() == 3

  assert table.delete(10) == 11
  assert table.get(10) == None
  with pytest.raises(KeyError):
    assert table[10] == None
  assert table.get_size() == 2

  assert table.delete(12) == 13
  assert table.get(12) == None
  with pytest.raises(KeyError):
    assert table[12] == None
  assert table.get_size() == 1

  assert table.delete(13) == 14
  assert table.get(13) == None
  with pytest.raises(KeyError):
    assert table[13] == None
  assert table.get_size() == 0

  with pytest.raises(KeyError):
    table.delete(10)
  
def test_print_all_items(capsys):
    table = HashTable()
    table.insert("apple", 10)
    table.insert("banana", 20)
    table["pineapple"] =  30

    table.print_all_items()

    # Перехватываем stdout
    captured = capsys.readouterr()

    assert "apple 10" in captured.out
    assert "banana 20" in captured.out
    assert "pineapple 30" in captured.out

