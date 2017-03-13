def anagrams(word, words):
    l1 = list(word)
    anagram_list = []
    for wrd in words:
        if len(wrd) == len(word):
            l2 = list(wrd)
            l1.sort()
            l2.sort()
            if l1 == l2:
                anagram_list.append(wrd)
    return anagram_list

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
