import turtle

turtle.shape("turtle")

def move_f():
    turtle.forward(50)
    turtle.stamp()
def move_b():
    turtle.backward(50)
    turtle.stamp()
def move_l():
    turtle.left(90)
def move_r():
    turtle.right(90)
def restart():
    turtle.reset()


turtle.onkey(move_f, 'w')
turtle.onkey(move_b, 's')
turtle.onkey(move_l, 'a')
turtle.onkey(move_r, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()

