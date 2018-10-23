import turtle
import random
import time

t = turtle.Turtle()

t.speed(0)
t.width(3)
colors  = ["red","green","blue","orange","purple","pink","yellow"]

for angle in range(100):
    t.color(random.choice(colors))
    t.left(angle * 7)
    t.circle(100)

time.sleep(3)
# t.mainloop()
