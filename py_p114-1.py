from datetime import datetime

thisYear = datetime.today().year
age = int(input("올해 나이는 : "))
nextAge = 2050 - thisYear + age + 1
print("올해는 " + str(thisYear) + "년 입니다.")
print("2050년은 %s살 이시네요" % str((2050 - thisYear + age)))


