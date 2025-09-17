from palindrome import check_number_for_palidrome

# Отдельно выделим случаи, которые выдают положительный результат
# Тестируем числа разной длины
# Учитываем, что они могут быть полностью одинаковые и состоять полностью из разных цифр с одной стороны
def test_check_number_for_palidrome_true():
    assert check_number_for_palidrome(5) is True
    assert check_number_for_palidrome(11) is True
    assert check_number_for_palidrome(121) is True
    assert check_number_for_palidrome(111) is True
    assert check_number_for_palidrome(1221) is True
    assert check_number_for_palidrome(2222) is True
    assert check_number_for_palidrome(45354) is True
    assert check_number_for_palidrome(55555) is True
    assert check_number_for_palidrome(123321) is True
    assert check_number_for_palidrome(222222) is True
    assert check_number_for_palidrome(2348432) is True
    assert check_number_for_palidrome(3333333) is True

# Отдельно выделим случаи, которые выдают негативный результат
# Тестируем числа разной длины
# Включаем числа полностью из разных цифр
# Включаем числа, почти похожие на палиндром
def test_check_number_for_palidrome_false():
    assert check_number_for_palidrome(12) is False
    assert check_number_for_palidrome(123) is False
    assert check_number_for_palidrome(12345) is False
    assert check_number_for_palidrome(123456) is False
    assert check_number_for_palidrome(123457) is False
    assert check_number_for_palidrome(2232) is False
    assert check_number_for_palidrome(153321) is False
    assert check_number_for_palidrome(2398432) is False
