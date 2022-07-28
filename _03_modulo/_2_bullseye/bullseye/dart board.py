import turtle
if __name__ == '__main__':
    sam = turtle.Turtle()
    sam.speed(0)

    for i in range(100):
        if i % 2:
            sam.up()
            sam.pencolor('black')
            sam.right(90)
            sam.forward(10*i)
            sam.left(90)
            sam.down()
            sam.circle(10*i, steps=100)
            sam.up()
            sam.goto(0, 0)
            sam.down()
        else:
            sam.up()
            sam.pencolor('orange')
            sam.right(90)
            sam.forward(10 * i)
            sam.left(90)
            sam.down()
            sam.circle(10*i, steps=100)
            sam.up()
            sam.goto(0, 0)
            sam.down()







turtle.done()