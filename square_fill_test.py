# draw square in Python Turtle
from turtle import *

color('#FF0000')
fillcolor('yellow')
begin_fill()

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)


while True:
    if abs(pos()) < 1 :
        break


#while True:
 #   forward(200)
  #  left(170)
   # if abs(pos()) < 1:
    #    break
end_fill()

exitonclick()