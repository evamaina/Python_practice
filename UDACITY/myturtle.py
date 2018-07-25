import turtle
import tkinter as TK

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)

	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	eva = turtle.Turtle()
	eva.shape("arrow")
	eva.color("blue")
	eva.circle(100)


	window.exitonclick()

draw_square()	