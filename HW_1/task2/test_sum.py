from sum import get_max_odd_sum

def test_get_max_odd_sum():
    # Все числа чётные
    assert get_max_odd_sum([2, 4, 6, 8]) == 20 
    
    # Все числа нечётные
    assert get_max_odd_sum([1, 3, 5, 7]) == 16 
    
    # Смешанные числа - сумма чётная
    assert get_max_odd_sum([1, 2, 3, 4]) == 10 
    
    # Смешанные числа - сумма нечётная
    assert get_max_odd_sum([1, 2, 3, 4, 5]) == 14  

    # Минимальное нечётное в середине, нет сортировки
    assert get_max_odd_sum([9, 1, 8, 5, 4]) == 26  

    # Один элемент - чётный
    assert get_max_odd_sum([4]) == 4
    
    # Один элемент - нечётный
    assert get_max_odd_sum([3]) == 0
    
    # Пустой массив
    assert get_max_odd_sum([]) == 0
    
    # Большие числа
    assert get_max_odd_sum([1000000, 999999, 888888]) == 1888888
    
    # Все числа одинаковые нечётные
    assert get_max_odd_sum([7, 7, 7, 7]) == 28 
    
    # Все числа одинаковые чётные
    assert get_max_odd_sum([2, 2, 2, 2]) == 8 
    


