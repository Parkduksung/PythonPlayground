
x= input("첫번째 숫자를 입력하세요 >>>")
y= input("두번째 숫자를 입력하세요 >>>")

#int 타입이 아니면 String 으로 판단하여 3 5 입력하면 8이 아닌 35로 나옴.
result = int(x) + int(y)

print(result)
