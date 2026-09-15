# 딕셔너리: 별도의 키를 통해 각 요소를 접근 할 수 있도록 만들어진 데이터 타입
# Map은 key : value 형태의 자바(HashMap)
# map은 파이썬에서 가공된 배열을 만드는(int,input()) 저장받은 자료를 인트형으로 가공 map(함수,시퀀스) 시퀀스+함수
# {}로 선언, 각 요소는 콤마(,)를 사용해 구분
# 키와 값의 한쌍으로 구성되고, 이 둘은 콜론(:)으로 구분
# []대괄호, {}중괄호,()소괄호

coffee_menu = {"Americano" : 2500,
               "Esspresso" : 2500,
               "Latte" : 4000,
               "Moca" : 4500}
print(coffee_menu)
print(coffee_menu["Americano"]) #키로 값 확인
print(coffee_menu.get("Latte"))

# 추가, 삭제, 키 존재 여부 확인
coffee_menu["Coldbrew"] = 5500 # 새로운 키와 값 추가
print(coffee_menu)
del coffee_menu["Latte"] #키와 값 제거
print(coffee_menu)

for e in coffee_menu: #존재 여부 확인
    print(f"키: {e}, 값: {coffee_menu[e]}")

# update 함수 사용하기 : 딕셔너리 데이터를 한꺼번에 변경 가능
coffee_menu.update({"Americano" : 3000,"Esspresso" : 3000,"Latte" : 4500,"Moca" : 5000, "Smoothie": 5500})
print(coffee_menu)

# 파이썬 딕셔너리 및 반복문 실습 문제

# 문제 1. 딕셔너리 생성 및 출력
# 학생 3명의 이름을 키로, 점수를 값으로 하는 딕셔너리 student_score를 만들고 전체를 출력하세요. (예: 철수 90, 영희 85, 민수 78)
student_score = {"철수":90, "영희":85, "민수":78}
print(student_score)

# 문제 2. 값 조회
# coffee_menu에서 "Moca"의 가격을 get() 함수를 이용해 출력하세요. 만약 존재하지 않는 메뉴("Cappuccino")를
# get()으로 조회하면 어떻게 출력되는지도 확인해보세요.
coffee_menu.get("Moca")
print(coffee_menu)
coffee_menu.get("Cappuccino")
print(coffee_menu)

# 문제 3. 추가와 삭제
# coffee_menu에 "Cappuccino": 4800을 새로 추가하고, "Moca"를 삭제한 뒤 결과를 출력하세요.
del coffee_menu["Moca"]
print(coffee_menu)
coffee_menu.update({"Cappuccino" : 4800})
print(coffee_menu)

# 문제 4. 반복문과 조건문 활용
# coffee_menu를 반복문으로 순회하면서, 가격이 4000원 이상인 메뉴만 "메뉴명 - 가격" 형태로 출력하세요.
for e in coffee_menu:
    if coffee_menu[e] >= 4000:
        print(f"메뉴명: {e} - 가격: {coffee_menu[e]}")

# 문제 5. update() 활용 및 키 존재 확인
# update() 함수를 사용해 coffee_menu의 모든 가격을 10% 인상하세요.
# (힌트: 반복문으로 새 딕셔너리를 만든 뒤 update()로 반영) 그리고 "in" 연산자를 사용해 "라떼"라는 키가 존재하는지 확인하는 코드도 작성하세요.
# 2. 10% 인상된 값을 담을 빈 딕셔너리 생성

for key, value in coffee_menu.items():
    coffee_menu[key] = int(value * 1.1)
print(coffee_menu)
if "Latte" in coffee_menu:
    print("라떼가 있습니다.")
else:
    print("라떼가 없습니다.")


# updated_menu = {}
# for e in coffee_menu:
#     updated_menu[e] = int(coffee_menu[e] * 1.1)
# coffee_menu.update(updated_menu)
# if "라떼" in coffee_menu:
#     print("'라떼' 메뉴가 존재합니다.")
# else:
#     print("'라떼' 메뉴가 존재하지 않습니다.")
# print("인상된 메뉴 결과:", coffee_menu)