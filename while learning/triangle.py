# print a triangle of words

def triangle(letter , rows):
    for i in range(rows+1):
        if(i == 0):
            continue
        print(letter*i)


triangle("l" ,5)