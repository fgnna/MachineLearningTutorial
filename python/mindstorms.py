
import turtle
window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
brad.shape("turtle")
brad.color("blue")
brad.speed(10)

def draw_circle(n):
    count = 360/n
    for i in range(n):
        brad.circle(50)
        brad.right(count)


draw_circle(20)
window.exitonclick()