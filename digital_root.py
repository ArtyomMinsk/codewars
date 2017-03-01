def digital_root(n):
    s = 0
    string = list(str(n))
    for i in string:
        s += int(i)

    if len(str(s)) == 1:
        return s
    else:
        return digital_root(s)
