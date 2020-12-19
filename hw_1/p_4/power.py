def square_root(x, max_depth=100):
    res = x
    cur_term = 0.5
    i = 0    
    while i < max_depth:
        compare_num = res * res
        if compare_num == x:
            break
        elif compare_num > x:
            res -= cur_term * x
        elif compare_num < x:
            res += cur_term * x

        cur_term *= 0.5
        i += 1

    return res

def irrational_power(x, n, max_depth=100):
    '''n is in the half-opened interval [0, 1)'''
    if n == 0: return 1
    cur_power = 1; temp_power = 1
    cur_term = x
    i = 0
    while i < max_depth:
        next_term = square_root(cur_term)
        temp_power *= 0.5
        if cur_power == n:
            break
        elif cur_power > n:
            x /= next_term
            cur_power -= temp_power
        elif cur_power < n:
            x *= next_term
            cur_power += temp_power

        cur_term = next_term
        i += 1

    return x

def int_power(x, n, res=1):
    '''n is an integer and n >= 0'''
    return int_power(x, n-1, res=res*x) if n > 0 else res

def power(x, n):
    # power(0, 0) gives the same result as python returns (0 ** 0 = 1)
    if n == 0: return 1
    if x == 1: return 1
    if x == 0 and n > 0: return 0
    if x == 0 and n < 0: raise ZeroDivisionError

    pos_pow = True
    if n < 0:
        pos_pow = False
        n = abs(n)

    int_part = int(n)
    partial_part = n - int_part
    res = int_power(x, int_part) * irrational_power(x, partial_part)
    return res if pos_pow else 1 / res