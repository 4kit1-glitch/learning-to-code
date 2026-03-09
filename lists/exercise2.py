def is_palindrome(word):
    if list(reversed(word)) == list(word):
        return True
    return False

def is_palindrome2(word):
    delimiter = ''
    if delimiter.join(reversed(word)) == word:
        return True
    return False

def is_palindrome3(word):
    if word[::-1] == word:
        return True
    return False