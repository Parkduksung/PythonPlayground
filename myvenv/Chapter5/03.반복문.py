
data = []


for i in range(1, 8):
    x = int(input(str(i) + "일차 턱걸이 횟수 >>>"))
    data.append(x)

total = sum(data)

avg = total/len(data)

print(avg)


#구구단 문제



t = int(input("몇 단을 출력할까요>>>"))

for i in range(1,10):
    print(f"{t} * {i} = {t*i}")