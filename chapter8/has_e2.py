#better algorithm

# def has_e(word):
#     return 'e' in word or 'E' in word 

def has_e(word):
    return 'e' in word.lower()  # very efficient algorithm

print(has_e("hello"))
print(has_e("nappy"))