def scramble(s1, s2):
    a = list(s1)
    b = list(s2)
    temp_list = set(a) & set(b)
    if temp_list == set(b):
        return True
    else:
        return False


scramble('rkqodlw','world')
scramble('cedewaraaossoqqyt','codewars')
scramble('katas','steak')
scramble('scriptjava','javascript')
scramble('scriptingjava','javascript')
scramble('scripting java','java script')
