from time_decorator import timeit
 
#-------------------------------------------------
# Сортировка слиянием
#-------------------------------------------------

def merge_list(a, b):
    c = []
    n = len(a)
    m = len(b)

    i = 0
    j = 0
    while i < n and j < m:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    c += a[i:] + b[j:]
    return c


def split_and_merge_list(a):
    n = len(a) // 2
    a1 = a[:n]    
    a2 = a[n:]

    if len(a1) > 1: 
        a1 = split_and_merge_list(a1)
    if len(a2) > 1: 
        a2 = split_and_merge_list(a2)

    return merge_list(a1, a2)  

@timeit
def merge_sort(a):
    return split_and_merge_list(a)


a = [4, 5, 1]
b = a.copy()
a.sort()
print(a)
print(b)