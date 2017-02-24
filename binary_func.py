def binary(number):
    binary_list = []
    while number != 0:
        remainder = number % 2
        binary_list.append(str(remainder))
        number = number // 2
    # print("binary_list: ", binary_list)
    binary_list.reverse()
    # print("reversed_list: ", binary_list)
    return binary_list


def invert(binary_list):
    inverted_list = []
    for digit in binary_list:
        if digit == "1":
            inverted_list.append("0")
        else:
            inverted_list.append("1")
    # print("inverted binary_list: ", inverted_list)
    return inverted_list


def get_decimal_number(inverted_list):
    decimal_number = 0
    n = len(inverted_list) - 1
    for item in inverted_list:
        decimal_number += int(item) * (2 ** n)
        n -= 1
    # print("final number: ", decimal_number)
    return decimal_number


def main():
    while True:
        try:
            user_input = int(input("Please enter a decimal number to convert: "))
            break
        except ValueError:
            print("Oops!  That was invalid input.  Try again...")
    binary_digits_list = binary(user_input)
    inverted_list = invert(binary_digits_list)
    print(get_decimal_number(inverted_list))

if __name__ == '__main__':
    main()
