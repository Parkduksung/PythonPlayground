
data = []


for i in range(1, 8):
    x = int(input(str(i) + "일차 턱걸이 횟수 >>>"))
    data.append(x)

total = sum(data)

avg = total/len(data)

print(avg)