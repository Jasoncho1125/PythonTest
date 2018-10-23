import random
import turtle as t
import time

for i in range(100):
    length = random.randrange(1,101)
    angle = random.randrange(-180, 181)
    print(length)

    t.shape("turtle")

    t.setheading(angle)
    t.fd(length)

t.mainloop()

#time.sleep(3)
