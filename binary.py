def getIntegerComplement(n):
    binary_list = []
    inverted_list = []
    while n != 0:
        remainder = n % 2
        binary_list.append(str(remainder))
        n = n // 2
    binary_list.reverse()
    for number in binary_list:
        if number == "1":
            inverted_list.append("0")
        else:
            inverted_list.append("1")
    decimal_number = 0
    num = len(inverted_list) - 1
    for item in inverted_list:
        decimal_number += int(item) * (2 ** num)
        num -= 1
    return decimal_number

print(getIntegerComplement(50))
