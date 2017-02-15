def divisors(integer):
    generated_list = []
    divisors_list = []

    for i in range(1, integer):
        generated_list.append(i)
        i += 1

    for num in generated_list:
        if integer % num == 0 and num != 1:
            divisors_list.append(num)

    if len(divisors_list) == 0:
        return "{} is prime".format(integer)
    else:
        return divisors_list

divisors(15)
