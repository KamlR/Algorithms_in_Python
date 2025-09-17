import math

def is_prime(num):
  for i in range(2, int(math.sqrt(num)) + 1):
     if num % i == 0:
       return False
  return True
  
def get_result(n):
  count = 0
  for i in range(2, n):
    if is_prime(i):
      count+=1
  return count

if __name__ == "__main__":
  n = int(input())
  print(get_result(n))