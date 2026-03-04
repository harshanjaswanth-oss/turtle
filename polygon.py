import turtle

turtle.Screen().bgcolor("teal")
turtle.Screen().setup(400,400)

polygon=turtle.Turtle()
for i in range(6):
  polygon.forward(20)
  polygon.right(60)
turtle.done()