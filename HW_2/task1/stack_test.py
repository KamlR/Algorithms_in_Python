from stack import Stack
import pytest


def test_stack_is_empty():
    s = Stack()
    assert s.is_empty()

    s.push(10)
    assert not s.is_empty()

def test_push_and_peek():
    s = Stack()
    s.push(10)
    assert not s.is_empty()
    assert s.peek() == 10

    s.push(20)
    assert s.peek() == 20

def test_pop():
    s = Stack() 
    s.push(1)
    s.push(2)
    s.push(3)

    assert s.pop() == 3
    assert s.peek() == 2

    assert s.pop() == 2
    assert s.peek() == 1

    assert s.pop() == 1
    assert s.is_empty()
    
def test_get_size():
    s = Stack() 
    for i in range(10): 
        assert s.get_size() == i
        s.push(i) 
    for i in range(10): 
        assert s.get_size() == 10 - i
        s.pop()

def test_pop_empty_stack_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_peek_empty_stack_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.peek()
