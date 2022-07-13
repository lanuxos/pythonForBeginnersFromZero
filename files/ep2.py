# ep1
# Python Turtle
import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Rectangle():
	for i in range(4):
		tao.forward(100)
		tao.left(90)

def Triangle():
	for i in range(3):
		tao.forward(100)
		tao.left(120)

def Go(x, y):
	tao.penup()
	tao.goto(x, y)
	tao.pendown()

Go(200, 200)
Rectangle()
Go(100, 100)
Triangle()