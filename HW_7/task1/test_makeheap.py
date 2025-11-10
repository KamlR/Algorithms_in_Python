# makeheap и makeheap_n_log_n выдаёт разный порядок ответов 

from makeheap import makeheap
def test_makeheap():
  assert makeheap([]) == [] 
  assert makeheap([1]) == [1] 
  assert makeheap([1, 2]) == [1, 2] 
  assert makeheap([1, 2, 3]) == [1, 2, 3] 
  assert makeheap([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5] 
  assert makeheap([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6] 
  assert makeheap([6, 5, 7, 1, 12, 0, 3, 2]) == [0, 1, 3, 2, 12, 7, 6, 5]
  assert makeheap([6, 5, 4, 3, 2, 1, 0]) == [0, 2, 1, 3, 5, 6, 4] 
  assert makeheap([8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 5, 4, 3, 6, 7, 8] 
  assert makeheap([5, 4, 6, 8, 3, 7, 2, 1, 0]) == [0, 1, 2, 4, 3, 7, 6, 5, 8] 


