# 함수(function)는 코드의 특정 블록을 하나의 아름으로 묶어둔 것
# 반복적으로 사용해야 하는 코드나 논리적인 작업을 함수로 정의하면, 재사용성, 가독성, 유지보수성을 높일 수 있음
# 함수는 생성 이 후 호출을 해야 실행 됨
# def 키워드 사용
#일반적으로 식별자뒤에() 소괄호가 있으면 함수

# 함수의 재 사용: 매개변수는 존재하고, 반환값이 없음
# def name_card(name, addr, phone):
#     print(f"이름: {name}")
#     print(f"주소: {addr}")
#     print(f"번호: {phone}")
#     print("-"*30)

# name_card("안유진","서울시 강남구 역삼동", "010-1234-5678")
# name_card("장원영","서울시 강남구 삼성동", "010-1234-9999")
# name_card("가을","수원시 권선구 권선동", "010-1234-1111")

# 1. 이름(name), 나이(age), 취미(hobby)를 매개변수로 받아서 아래 형식으로 출력하는 함수 intro_card()를 작성하시오.
# def intro_card(name,age,hobby):
#     print(f"이름: {name}")
#     print(f"나이: {age}")
#     print(f"취미: {hobby}")
#
# # 1-2 과목명(subject)과 점수(score)를 매개변수로 받아 "수학 점수: 90점"
# # 형식으로 출력하는 함수 print_score()를 작성하고, 서로 다른 3개 과목으로 호출해보시오.
# def report_card(subject, score):
#     print(f"{subject} 점수: {score}점")
#     print("-" * 15)
#
# report_card("과학", 90)
# report_card("사회", 70)
# report_card("수학", 80)
#
# # 매개변수 0, 반환값 0
# # 2-1 두 정수를 입력받아 큰 수를 반환하는 함수 get_max(a, b)를 작성하시오. (if문 사용)
# def get_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a, b = list(map(int,input("정수 입력: ").split(",")))
# result = get_max(a,b)
# print(f"큰 수는 {result}")
#
# # 2-2 원의 반지름을 입력받아 원의 넓이를 반환하는 함수 circle_area(r)를 작성하시오. (원주율은 3.14 사용)# 2-2 원의 반지름을 입력받아 원의 넓이를 반환하는 함수 circle_area(r)를 작성하시오. (원주율은 3.14 사용)
# def circle_area(r):
#     return r * r * 3.14
#
# print(f"원의 넓이: {circle_area(5)}")
#
# # 2-3 정수를 입력받아 짝수면 "짝수", 홀수면 "홀수"를 반환하는 함수 check_even_odd(num)를 작성하시오.
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "짝수"
#     else:
#         return "홀수"
#
# num = int(input("정수 입력: "))
# result = check_even_odd(num)
# print(f"{num}은 {result}입니다.")

# 기본값 인자 : 함수 선언 시 매게 변수에 대한 기본값을 정의
# - 매개변수에 기본값이 정의 되어 있는 경우 함수 호출 시 인자값을 넣지 않으면 기본값으로 호출
# def profile(name, age=0, job="무직", addr="대한민국"):
#     print(f"이름: {name}")
#     print(f"나이: {age}")
#     print(f"직업: {job}")
#     print(f"주소: {addr}")
#
# profile("안유진",23,"아이돌","대전시")
# profile("장원영",22,"아이돌")
# profile("이서")

# 가변 매개 변수
# def profile(name, age, *lang):
#     print(f"이름: {name}, 나이: {age}", end= " ")
#     for e in lang:
#         print(e, end= " ")
#     print()
#
# profile("나희도", 18, "Python", "Java", "C", "C++", "React", "Kotlin")
# profile("조세호", 38, "Python", "Java")
# profile("유재석", 48, "Python", "Java", "C", "C++")

# 실습 문제: 표준 체중 계산기

# 키(cm)와 성별을 입력받아 표준 체중을 계산하는 함수를 작성하시오.

# 조건

# 함수 이름은 std_weight로 하고, 매개변수는 키(h)와 성별(sex) 두 개를 받는다.
# 표준 체중 공식은 다음과 같다.
# 남성: (키(m))² × 22
# 여성: (키(m))² × 21
# 단, 입력받은 키는 cm 단위이므로 함수 내부에서 m 단위로 변환해야 한다. (h / 100)
# 함수는 계산된 표준 체중 값을 반환(return) 해야 한다. (출력 X)
# input()을 이용해 사용자로부터 키(cm)와 성별을 입력받는다.
# 키는 정수로 변환하여 저장 (int(input(...)))
# 성별은 "남성" 또는 "여성" 문자열로 입력받음
# 함수 호출 결과를 아래 형식으로 출력하시오. (소수점 둘째 자리까지)
# def std_weight(h,sex):
#     if sex == "남성":
#         return ((h/100)**2) * 22
#     else:
#         return ((h/100)**2) * 21
#
#
# sex = input("성별 입력: ")
# h = int(input("키 입력: "))
# result = std_weight(h,sex)
# print(f"{result:.2f}")

# 소수 판별하기
# def is_prime_func(n):
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#     return is_prime
#
# n = int(input("정수 입력: "))
# if is_prime_func(n):
#     print(f"{n}은 소수입니다.")
# else:
#     print(f"{n}은 소수가 아닙니다.")


# 소수의 합 구하기
def prime_func(n): # 소수로 기본값을 정의
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False # 소수가 아닌 경우
    if is_prime:
        return n # 소수인 경우만 값 반환
    else:
        return 0

n = int(input("정수 입력: "))
total = 0
for i in range(2, n):
    total += prime_func(i)
print(total)