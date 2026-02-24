# prints a simple rectangle 

def rectangle(letter , lenght , width):
    for i in range(lenght + 1):
        if(i == 0):
            continue
        else:
            print(letter*width)


rectangle("H" , 5 , 4)