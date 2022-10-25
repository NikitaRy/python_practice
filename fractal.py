import turtle

turtle.speed(0) 
turtle.tracer(0, 0)  # вырубаем анимацию
screen = turtle.Screen()  # это чтобы поставить заголовок ))
screen.title('Random fractal') 
turtle.hideturtle()
turtle.color('purple')


def squares(x, y, length, n):
    if n == 0:
        return 0
    turtle.up()
    turtle.goto(x - length / 2, y - length / 2)
    turtle.down()
    turtle.seth(0)
    for i in range(4):  # рисуем в цикле четырехугольник
        turtle.fd(length)
        turtle.left(90)

    squares(x, y + 3 * length / 4, length / 2, n - 1)  # четырехугольники поменьше и из центра граней предыдущего
    squares(x, y - 3 * length / 4, length / 2, n - 1)
    squares(x + 3 * length / 4, y, length / 2, n - 1)
    squares(x - 3 * length / 4, y, length / 2, n - 1)


squares(0, 0, 200, 5)
screen.update()
turtle.done()
