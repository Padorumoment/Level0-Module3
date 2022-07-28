import turtle

if __name__ == '__main__':
    sam = turtle.Turtle()
    sam.shape('turtle')
    sam.color('blue', 'green')
    sam.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    sam.goto(-200, 0)
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.
    for i in range(10):
        for i in range(5):
            sam.forward(30)
            sam.left(144)
        sam.forward(50)

    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
