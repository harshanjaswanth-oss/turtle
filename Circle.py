import turtle

turtle.Screen().bgcolor("teal")
turtle.Screen().setup(400,400)

T=turtle.Turtle()
T.circle(50)
T.color("red")
T.begin_fill()
T.circle(100)
T.end_fill()
turtle.done()