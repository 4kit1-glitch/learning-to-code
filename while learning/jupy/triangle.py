from jupyturtle import make_turtle , forward , left , right

make_turtle(delay=0.1 , width=300 ,height=300)


def triangle(lenght):
    angle = 180 - 60
    for i in range(3):
        forward(lenght)
        left(angle)

def draw_pie(n , lenght):
    for i in range(n):
        triangle(50)