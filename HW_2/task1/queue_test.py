from queue import Queue
import pytest

def test_new_queue_is_empty():
  q = Queue()
  assert q.is_empty()

def test_push_and_peek():
  q = Queue()
  q.push(10)
  assert not q.is_empty()
  assert q.peek() == 10

  q.push(11)
  q.push(12)
  q.push(13)
  assert q.peek() == 10

def test_pop_and_peek():
  q = Queue() 
  q.push(10)
  q.push(11)
  q.push(12)
  q.push(13)
  
  assert q.pop() == 10
  assert q.peek() == 11

  assert q.pop() == 11
  assert q.peek() == 12

  assert q.pop() == 12
  assert q.peek() == 13

  assert q.pop() == 13
  with pytest.raises(IndexError):
        q.peek()

def test_get_size():
    q = Queue() 
    for i in range(10): 
        assert q.get_size() == i
        q.push(i) 
    for i in range(10): 
        assert q.get_size() == 10 - i
        q.pop()

def test_pop_empty_queue_raises():
    q = Queue() 
    with pytest.raises(IndexError):
        q.pop()


def test_peek_empty_queue_raises():
    q = Queue() 
    with pytest.raises(IndexError):
        q.peek()
