# Считаем кол-во цифр в числе
def count_digits_in_num(n):
  digits = 0
  while n!=0:
    digits+=1
    n//=10
  return digits


# Вычисляем палиндром
def check_number_for_palidrome(n): 
  digits = count_digits_in_num(n)
  helper = 10 ** (digits - 1) 
  digits//=2
  n1, n2 = n, n
  while digits!=0:
    if (n1 // helper) % 10 != n2 % 10:
      return False
    helper//=10
    n2//=10
    digits-=1
  return True



if __name__ == "__main__":
    n = int(input())
    print(check_number_for_palidrome(n))

