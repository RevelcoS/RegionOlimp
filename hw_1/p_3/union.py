def sorted_set(m):
    return sorted(set(m))

def union(a, b):
    a, b = sorted_set(a), sorted_set(b)
    p1, p2 = 0, 0
    while p1 < len(a) and p2 < len(b):
        a_num, b_num = a[p1], b[p2]
        if a_num < b_num:
            p1 += 1
        elif a_num > b_num:
            p2 += 1
        elif a_num == b_num:
            yield a_num
            p1 += 1