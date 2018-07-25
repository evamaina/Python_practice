import turtle
import tkinter as TK

def draw_square(some_turtle):
	for i in range (1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	# create a turtle brad- draws a square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	for i in range(1,37):
		draw_square(brad)
		brad.right(10)

	# create a turtle eva - draws a circle
	# eva = turtle.Turtle()
	# eva.shape("arrow")
	# eva.color("blue")
	# eva.circle(100)

	window.exitonclick()

draw_art()

