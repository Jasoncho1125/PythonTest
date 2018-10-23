import turtle as t

t.shape("turtle")
t.up()
t.goto(120, 0)
t.write("거북이가 여기로 오면 0 입니다.")
t.goto(120,100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(120, -100)
t.write("거북이가 여기로 오면 음수입니다.")

t.home() # 거북이 원래 홈으로 이동하기
t.down()

s = int(t.textinput("", "숫자를 입력하시오: "))

if s == 0:
    t.goto(100,0)
elif s < 0 :
    t.goto(100, -100)
else:
    t.goto(100,100)

t.mainloop()
