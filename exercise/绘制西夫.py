#绘制西夫
import turtle as t

def turtuleMoveWithoutDraw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    return

#设置基本参数
t.setup(1000,800)
t.speed(10)
t.pensize(10)
t.pencolor("purple")

#西字上面一横
turtuleMoveWithoutDraw(-300,200)
t.fd(150)

#画西的口
turtuleMoveWithoutDraw(-350,100)
for i in range(4):
    t.fd(250)
    t.right(90)

#画西的两撇
turtuleMoveWithoutDraw(-250,200)
t.right(90)
t.fd(125)
t.circle(-100,70)


turtuleMoveWithoutDraw(-200,200)
t.setheading(-90)
t.fd(200)
t.circle(20,90)
t.fd(60)


#画夫字的两横
t.setheading(0)
turtuleMoveWithoutDraw(150,150)
t.fd(150)
turtuleMoveWithoutDraw(100,50)
t.fd(250)

#画夫的两撇
t.setheading(-90)
turtuleMoveWithoutDraw(225,200)
t.fd(150)

t.setheading(-100)
t.circle(-250,50)
turtuleMoveWithoutDraw(225,50)
t.setheading(-80)
t.circle(250,50)



t.exitonclick()