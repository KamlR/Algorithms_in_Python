from prime import get_result

# Идея тестирования:
# Выпишем список простых чисел до 103, далее запустим цикл от 0 до 103 включительно.
# Функция get_expected_result смотрит, где тестируемое значение стоит относительно элементов списка prime_numbers.
# Зная эту позицию, мы знаем, сколько до тест. знач. простых чисел. Полученное значение сверяем с тем, что выдаёт наша функция в prime.py

def get_expected_result(tested_num, prime_numbers):
    if tested_num == 0 or tested_num == 1:
        return 0
    for i in range(len(prime_numbers)):
        if tested_num  == prime_numbers[i]:
            return i
        elif tested_num > prime_numbers[i] and tested_num < prime_numbers[i + 1]:
            return i + 1
        
def test_get_result():
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 
       37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
       79, 83, 89, 97, 101, 103]
    for i in range(0, prime_numbers[-1] + 1):
        assert get_result(i) == get_expected_result(i, prime_numbers)
        
        