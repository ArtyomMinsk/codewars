def zeros(n):
    mlt = 1
    for i in range(1, n + 1):
        mlt *= i

    return len(str(mlt))-len(str(mlt).rstrip('0'))

# print(zeros(12)) # 2
# print(zeros(4)) # 0
# print(zeros(10)) # 2
# print(zeros(15)) # 3
# print(zeros(5)) # 1
