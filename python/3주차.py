##a = int(input("첫번째 값 :"))
##b = int(input("두번째 값 :"))
##c = int(input("세번째 값 :"))


##print(a, "*", b, "=", a*b)
##print(a, "+", b, "=", a+b)
##print(a, "-", b, "=", a-b)
##print(a, "/", b, "=," a/b)

##data="안녕" + \
##"하세요?" + \
##"파이썬!"
##print(data)


##import turtle
##t = turtle.Turtle()

##t.speed(3)
##t.pensize(10)
##t.pencolor("red")


##t.shape("arrow")
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)
##t.right(144)
##t.forward(200)

##turtle.done()


import turtle
import random

##함수 선언 부분 ##
def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

def screenrightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def screenmiddleClick(x, y):
    global r, g, b
    tsize = random.randrange(1, 10)
    turtle.shapesize(tsize)
    r = random.random()
    g = random.random()
    b = random.random()

##변수 선언 부분##
psize =10
r,g,b =0.0,0.0,0.0

##메인 코드 부분##
turtle.title("거북이로 그림그리기")
turtle.shape("turtle")
turtle.pensize(psize)
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenmiddleClick, 2)
turtle.onscreenclick(screenrightClick, 3)

turtle.done()


            