def find_missing(sequence):
    s = sequence[0]
    if (sequence[1] - sequence[0]) == (sequence[2] - sequence[1]):
        diff = sequence[1] - sequence[0]
    else:
        diff = sequence[3] - sequence[2]

    ap = [s + i * diff for i in range(len(sequence))]
    for j in ap:
        if j not in sequence:
            return j
