def toJadenCase(string):
    caps_list = []
    words_list = string.split(' ')
    for word in words_list:
        caps_list.append(word[0].upper() + word[1:])
    result = ' '.join(caps_list)
    return result


toJadenCase("Hello people how are you doing")
