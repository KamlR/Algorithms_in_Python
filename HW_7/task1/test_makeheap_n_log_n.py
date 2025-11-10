from makeheap_n_log_n import makeheap_n_log_n
def test_makeheap_n_log_n():
  assert makeheap_n_log_n([]) == [] 
  assert makeheap_n_log_n([1]) == [1] 
  assert makeheap_n_log_n([1, 2]) == [1, 2] 
  assert makeheap_n_log_n([1, 2, 3]) == [1, 2, 3] 
  assert makeheap_n_log_n([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5] 
  assert makeheap_n_log_n([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6] 
  assert makeheap_n_log_n([6, 5, 7, 1, 12, 0, 3, 2]) == [0, 2, 1, 5, 12, 7, 3, 6]
  assert makeheap_n_log_n([6, 5, 4, 3, 2, 1, 0]) == [0, 3, 1, 6, 4, 5, 2] 
  assert makeheap_n_log_n([8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 3, 2, 6, 7, 4, 8, 5] 
  assert makeheap_n_log_n([5, 4, 6, 8, 3, 7, 2, 1, 0]) == [0, 1, 3, 2, 5, 7, 6, 8, 4] 


