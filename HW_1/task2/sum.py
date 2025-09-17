def find_min_odd_number(arr):
  min = 0
  for element in arr:
    if element % 2 != 0:
      min = element
      break
  for element in arr:
    if element % 2 != 0 and element < min:
      min = element
  return min
def get_max_odd_sum(arr):
  if (len(arr) == 1 and arr[0] % 2 != 0) or len(arr) == 0:
    return 0
  suma = 0
  for element in arr:
    suma+=element
  if suma % 2 == 0:
    return suma
  else:
    mini_odd = find_min_odd_number(arr)
    return suma - mini_odd

if __name__ == "__main__":
  arr = list(map(int, input().split()))
  print(get_max_odd_sum(arr))