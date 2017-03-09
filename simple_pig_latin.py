def pig_it(text):
    alpha = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789"
    str_list = text.split()
    new_list = []
    for item in str_list:
        if (item in alpha) and len(item) == 1:
            new_list.append(item + 'ay')
        elif len(item) >= 2:
            new_list.append(item[1:] + item[0] + 'ay')
        else:
            new_list.append(item)
    return ''.join(new_list)
print(pig_it('Pig latin is b cool ?'))
