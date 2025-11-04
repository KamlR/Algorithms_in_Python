from mergesort import merge_sort
from quicksort import quick_sort
import time
from random import shuffle

"""Сравнивает время работы Merge Sort и Quick Sort на разных типах массивов"""

sizes = [1000, 2000, 4000, 8000]
for size in sizes:
    print(f"\n=== Размер: {size} элементов ===")

    sorted_arr = list(range(size))
    shuffled_arr = sorted_arr.copy()
    shuffle(shuffled_arr)
    reversed_arr = sorted_arr[::-1]
    duplicates_arr = [5] * size

    test_cases = {
        "Отсортированный": sorted_arr,
        "Перемешанный": shuffled_arr,
        "Обратно отсортированный": reversed_arr,
        "Повторяющиеся": duplicates_arr
    }

    for name, arr in test_cases.items():
        arr1 = arr.copy()
        arr2 = arr.copy()

        start = time.perf_counter()
        merge_sort(arr1)
        merge_time = time.perf_counter() - start

        start = time.perf_counter()
        quick_sort(arr2)
        quick_time = time.perf_counter() - start

        print(f"{name:<25} | Merge Sort: {merge_time:.6f}s | Quick Sort: {quick_time:.6f}s")