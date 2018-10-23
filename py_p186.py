breads = ["호빌빵", "위트", "화이트"]
meats = ["미트볼", "소시지", "닭가슴살"]
vegis = ["양상추", "토마토", "오이"]
sauces = ["마요네즈", "허니 머스터드", "칠리"]

#print(len(breads))
count = 0

for i in range(len(breads)):
    for j in range(len(meats)):
        for k in range(len(vegis)):
            for l in range(len(sauces)):
                print(breads[i], meats[j], vegis[k], sauces[l])
                count += 1

print("전체 요리 개수는 %s개 입니다" % count)

