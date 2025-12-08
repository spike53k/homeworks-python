def upper(text):
    return text.upper()
def count(text):
    return len(text)
def palindrome(word):
    if word[::-1] == word:
        return True
    else:
        return False