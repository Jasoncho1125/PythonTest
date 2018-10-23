import turtle as t
import random

t.bgcolor("black")
colors = ["red", "blue", "purple", "green", "yellow", "orange"]

t.speed(0)
t.width(3)

for i in range(100):
    t.color(random.choice(colors))
    t.left(89)
    t.fd(1 + i * 5)

t.mainloop()
