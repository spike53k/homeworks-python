def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

def reverse(word):
    return word[::-1]


def anagram(w1, w2):
    w1_c = w1.lower().replace(" ", "")
    w2_c = w2.lower().replace(" ", "")

    w1_s = sorted(w1_c)
    w2_s = sorted(w2_c)

    return w1_s == w2_s