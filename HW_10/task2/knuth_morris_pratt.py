def build_lps(pattern: str) -> list[int]:
    n = len(pattern)
    lps = [0] * n

    i = 1      # идём по строке
    j = 0      # длина текущего совпадения префикса

    while i < n:
      if pattern[i] == pattern[j]:
        j += 1
        lps[i] = j
        i += 1
      else:
        if j != 0:
            j = lps[j - 1]
        else:
            lps[i] = 0
            i += 1

    return lps

def kmp_search(text: str, pattern: str) -> list[int]:
    """
    Возвращает список индексов начала всех вхождений pattern в text
    """
    if len(pattern) == 0 or len(pattern) > len(text):
        return [-1]

    lps = build_lps(pattern)
    result = []

    i = 0  # индекс в text
    j = 0  # индекс в pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]  # ищем следующее вхождение

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result
