
def has_e(text):
    for letter in text:
        if(letter == 'e' or letter == 'E'):
            return True
    return False

def exiting(n):
    for i in range(n):
        if(i == 2):
            return 9
        
    return 5
