# year = int(input("년도를 입력하세요 : "))

for year in range(1900, 2020):
    if ((year % 4 == 0) and ( year % 100 != 0)) or (year % 400 == 0)  :
        print(str(year) + "년은 윤년입니다.")

    else:
        print(str(year) + "년은 윤년이 아닙니다.")