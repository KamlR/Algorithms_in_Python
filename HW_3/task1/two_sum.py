# Важно!
# В условии сказано, что "Гарантируется, что такая пара будет ровно одна".
# Не может быть случая отсутствия ответа вообще.
# Рассматриваем массивы длины 1+. Предполагается, что другие на вход не подаются.
# Ответ должен состоять из разных индексов.
def two_sum(arr, k):
  work_list = []
  for i in range(len(arr)):
    work_list.append([arr[i], i])
  work_list.sort(key=lambda x: x[0])
  left = 0
  right = len(arr) - 1
  while left < right: 
    if work_list[left][0] + work_list[right][0] < k:
      left+=1
    elif work_list[left][0] + work_list[right][0] > k:
      right-=1
    else:
      result = sorted([work_list[left][1],  work_list[right][1]])
      return str(result[0]) + " " + str(result[1])
print(two_sum([3, 4, 2, 10], 13))