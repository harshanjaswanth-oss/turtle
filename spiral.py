import turtle


turtle.Screen().bgcolor("teal")
turtle.Screen().setup(400, 400)


t = turtle.Turtle()


for i in range(100):
    t.forward(i * 2)
    t.right(30)

turtle.done()

