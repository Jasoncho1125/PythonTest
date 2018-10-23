import turtle as t

name = t.textinput("", "이름을 입력하시오: ")
t.write("안녕하세요. %s 터틀 인사드립니다." % name)

t.mainloop()
