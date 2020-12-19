from functools import reduce

def sort_extend(lst1, lst2):
    new_lst = []
    p1, p2 = 0, 0
    while p1 < len(lst1) and p2 < len(lst2):
        num1, num2 = lst1[p1], lst2[p2]
        if num1 <= num2:
            new_lst.append(num1)
            p1 += 1
        elif num1 > num2:
            new_lst.append(num2)
            p2 += 1
    
    if p1 == len(lst1):
        new_lst.extend(lst2[p2:])
    else:
        new_lst.extend(lst1[p1:])
    return new_lst

def cons_diffs(lst):
    cons_lst = []
    for i in range(len(lst) - 1):
        cons_lst.append(lst[i+1] - lst[i])
    return cons_lst

def cons_sums(lst):
    cons_lst = []
    for i in range(len(lst) - 1):
        cons_lst.append(lst[i] + lst[i+1])
    return cons_lst

def min_diff(lst, n):
    lst.sort()
    all_diffs = []
    base_diffs = cons_diffs(lst)
    temp_diffs = cons_sums(base_diffs)
    for lst in (base_diffs, temp_diffs):
        all_diffs.append(lst)
    
    while len(temp_diffs) > 1:
        new_diffs = []
        for i in range(1, len(temp_diffs)):
            new_diffs.append(temp_diffs[i] + base_diffs[i-1])
        all_diffs.append(new_diffs)
        temp_diffs = new_diffs

    return reduce(sort_extend, all_diffs)[n-1]

# [0, 2, 2, 4, 3, 5, 5, 6, 6, 7, 8, 9, 9, 10, 12, 13, 14, 14, 17, 19, 19]
#print(min_diff([1, 3, 1, 10, 15, 7, 20], 10))