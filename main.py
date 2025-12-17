import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
colourlist=[(229, 233, 238), (225, 238, 233), (235, 113, 37), (143, 67, 26), (237, 37, 72), (220, 55, 164), (15, 88, 140), (174, 50, 162), (33, 186, 122), (52, 227, 189), (173, 94, 44), (242, 57, 219), (80, 74, 24), (127, 92, 190), (250, 0, 223), (23, 122, 169), (189, 41, 67), (207, 165, 133), (147, 25, 29), (35, 208, 181), (11, 56, 101), (239, 193, 163), (243, 157, 166)]
p=len(colourlist)
p-=1
r=0
l=0.0
timmy=Turtle()
timmy.pensize(15)
for i in range(1,100):
    n=random.randint(0,p)
    timmy.pencolor((colourlist[n]))
    timmy.dot(5)
    r+=50
    timmy.teleport(r,l)
    if i%10==0:
        timmy.teleport(0,i)
        l+=10.0
        r=0
    i+=1














screen=Screen()
screen.exitonclick()

