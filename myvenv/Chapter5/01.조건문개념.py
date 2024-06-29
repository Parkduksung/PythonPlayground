
origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass == origin_pass:
    print("로그인 성공!")
elif input_pass == "":
    print("아무것도 입력하지 않음.")
else:
    print("로그인 실패!")
    
