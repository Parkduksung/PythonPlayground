
animals = ["가물치", "벼메뚜기", "비단뱀", "도룡뇽"]

empty = []

print(animals[2]) 
print(animals[-1]) # 거꾸로 첫번째
print(animals[-2]) 

animals.append("고라니")
print(animals)

animals[0] = "청개구리"
print(animals)

del animals[0]
print(animals)

print(animals[1:3])
print(animals[:])
print(animals[:3])
print(animals[1:])

print(len(animals))
animals.sort(reverse=True)
print(animals)
