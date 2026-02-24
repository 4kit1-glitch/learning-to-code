from jupyturtle import make_turtle , forward , left

make_turtle()

def square(lenght):   ### encapsulating
    for i in range(4):
        forward(lenght)
        left(90)

square(50)
square(30)