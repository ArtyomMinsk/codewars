def gcd(numerator, denominator):
    while denominator:
        numerator, denominator = denominator, numerator % denominator
    return numerator


def mixed_fraction(s):
    div_sign_index = s.index('/')
    chislitel = int(s[0:div_sign_index])
    znamenatel = int(s[div_sign_index + 1:])

    try:
        if chislitel % znamenatel == 0:
            print(str(int(chislitel / znamenatel)))
            return str(int(chislitel / znamenatel))
    except ZeroDivisionError as e:
        raise e

    if chislitel < 0 and znamenatel < 0:
        chislitel = abs(chislitel)
        znamenatel = abs(znamenatel)

    integer_part = abs(chislitel) // abs(znamenatel)
    if chislitel < 0 and znamenatel > 0 or chislitel > 0 and znamenatel < 0:
        integer_part = integer_part * (-1)
    ostatok = abs(chislitel) - abs(znamenatel) * abs(integer_part)

    common_factor = gcd(ostatok, abs(znamenatel))

    reduced_ostatok = ostatok / common_factor
    reduced_znamenatel = abs(znamenatel) / common_factor

    if chislitel < 0 and abs(chislitel) < abs(znamenatel) or znamenatel < 0 and abs(chislitel) < abs(znamenatel):
        reduced_ostatok = reduced_ostatok * (-1)

    if integer_part == 0:
        return str(int(reduced_ostatok)) + '/' + str(int(reduced_znamenatel))
    else:
        return str(integer_part) + ' ' + str(int(reduced_ostatok)) + '/' + str(int(reduced_znamenatel))



mixed_fraction('42/9')
mixed_fraction('6/3')
mixed_fraction('4/6')
mixed_fraction('0/18891')
mixed_fraction('-10/7')
mixed_fraction('-22/-7')
mixed_fraction('0/0')
mixed_fraction('-70244/8762526')
