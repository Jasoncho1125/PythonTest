import turtle as t

t.shape("turtle")
t.shapesize(2,2)

while True:
    direction = input("방향을 선택하세요 : ")
    if direction == "l":
        t.left(90)
        t.fd(100)
    if direction == "r":
        t.right(90)
        t.fd(100)
# t.mainloop()
