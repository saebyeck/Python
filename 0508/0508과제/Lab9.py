address = input("이메일 주소를 입력하시오: ")

id, domain = address.split("@") # split("@")로 분리함
 
print(address)
print("아이디:" + id)
print("도메인:" + domain)

# 이메일 주소 분석 Lab 