import turtle
import math

def check_point_position(cx, cy, r, px, py):
    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    if math.isclose(distance, r, abs_tol=1e-5):
        return "Точка лежит НА окружности", "orange"
    elif distance < r:
        return "Точка находится ВНУТРИ окружности", "green"
    else:
        return "Точка располагается ЗА ПРЕДЕЛАМИ окружности", "red"

cx = float(input("Введите X центра окружности: "))
cy = float(input("Введите Y центра окружности: "))
r = float(input("Введите радиус окружности: "))

px = float(input("Введите X точки: "))
py = float(input("Введите Y точки: "))

message, point_color = check_point_position(cx, cy, r, px, py)
print(message)

screen = turtle.Screen()
screen.title("Положение точки относительно окружности")
screen.setup(width=600, height=600)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(cx, cy - r)
t.color("blue")
t.pensize(2)
t.pendown()
t.circle(r)

t.penup()
t.goto(px, py)
t.dot(10, point_color)
screen.exitonclick()
