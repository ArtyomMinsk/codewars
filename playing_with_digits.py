def dig_pow(n, p):
    string_num = list(str(n))
    s = 0
    for i in string_num:
        s += int(i) ** p
        p += 1
    k = s//n

    if s == n * k:
        return k
    else:
        return -1
