import turtle
turtle.setup(650,350,400,400)#width height startX startY
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.colormode(255)
turtle.pencolor(199,237,204)
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
