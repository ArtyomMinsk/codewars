def unique_in_order(iterable):
    iterable_list = list(iterable)
    unique_list = []
    if len(iterable_list) == 0:
        return []
    else:
        unique_list.append(iterable_list[0])
    for i in range(0, len(iterable_list)):
        if i != 0 and iterable_list[i] != unique_list[-1]:
            unique_list.append(iterable_list[i])
    return unique_list

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcADAA'))
print(unique_in_order([1,2,2,3,3]))
print(unique_in_order('A'))
print(unique_in_order('AAA'))
