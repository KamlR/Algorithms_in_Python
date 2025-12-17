def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return [-1]

    # параметры хэша
    p = 31                  # основание
    mod = 10**9 + 7         # модуль

    # p^(m-1) % mod — для вычитания старшего символа
    power = pow(p, m - 1, mod)

    # начальные хэши
    hash_pattern = 0
    hash_window = 0

    # считаем хэш шаблона и первого окна
    for i in range(m):
        hash_pattern = (hash_pattern * p + ord(pattern[i])) % mod
        hash_window = (hash_window * p + ord(text[i])) % mod

    result = []

    # основной цикл
    for i in range(n - m + 1):
        # если хэши совпали — проверяем посимвольно
        if hash_window == hash_pattern:
            if text[i:i + m] == pattern:
                result.append(i)

        # rolling hash: сдвиг окна
        if i < n - m:
            # убираем левый символ
            hash_window = (hash_window - ord(text[i]) * power) % mod
            # сдвигаем степени
            hash_window = (hash_window * p) % mod
            # добавляем новый символ
            hash_window = (hash_window + ord(text[i + m])) % mod

    return result
