import turtle  # 从标准库里面引入turtle


def draw_art():

    window = turtle.Screen()  # 获得一个窗口句柄

    window.bgcolor("blue")  # 把背景设为蓝色

    brad = turtle.Turtle()

    brad.shape("turtle")  # 形状是一个海龟除了画海龟还可以画箭头，圆圈等等

    brad.color("orange")  # 颜色是橙色

    brad.speed('fast')  # 画的速度是快速
    window.exitonclick()  # 当点击一下窗口会自动关闭

# draw_art()  # 调用函数
x = 1
y = 2
print((x, y))
print('sd=%s=%s' % (x, y))
li = [1, 2, 3, 4, 5]
import random
print(random.randint(1, 23))
