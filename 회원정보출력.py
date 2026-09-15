# name = input("이름 입력 : ")
# print("이름 입력 완료")
# while True:
#     age = int(input("나이 입력 : "))
#     if 0 < age and age < 200:
#         print("나이 입력 완료")
#         break
#     else:
#         print("나이를 잘못 입력하셨습니다.")
# while True:
#     gender = input("성별 입력 : ")
#     if gender.upper() == "M":
#         gender_d = "남성"
#         print("성별 입력 완료")
#         break
#     elif gender.upper() == "F":
#         gender_d = "여성"
#         print("성별 입력 완료")
#         break
#     else:
#         print("성별을 잘못 입력하셨습니다.")
# while True:
#     print("당신의 직업은 무엇입니까?")
#     print("[1]학생")
#     print("[2]회사원")
#     print("[3]주부")
#     print("[4]무직")
#     job = int(input("직업 입력 : "))
#     if job == 1:
#         job_d = "학생"
#         break
#     elif job == 2:
#         job_d = "회사원"
#         break
#     elif job == 3:
#         job_d = "주부"
#         break
#     elif job == 4:
#         job_d = "무직"
#         break
#     else:
#         print("직업을 잘못 입력하셨습니다.")
# print(f"{name}은 {age}살 {gender_d}이며, {job_d}이다")

# while True:
#     num = int(input("숫자 입력 : "))
#
#     if num == -1:
#         print("종료")
#         break
#     elif num % 2 == 1:
#         num_d = "홀수"
#         print(f"{num}은 {num_d}입니다.\n")
#     elif num % 2 == 0:
#         num_d = "짝수"
#         print(f"{num}은 {num_d}입니다.\n")
#     else:
#         print("다시 입력하세요.\n")

# even_count = 0  # 짝수 개수
# odd_count = 0  # 홀수 개수
#
# while True:
#     num = int(input("정수 입력 (-1 입력 시 종료) : "))
#
#     if num == -1:
#         print("종료합니다.")
#         break
#     elif num % 2 == 0:
#         even_count += 1
#     elif num % 2 == 1:
#         odd_count += 1
#
# print(f"짝수 개수: {even_count}개")
# print(f"홀수 개수: {odd_count}개")

while True:
    print()
    num = int(input("몇 단을 외우시겠습니까? "))
    if num == 0:
        print("구구단을 종료합니다.")
        break
    elif 0 < num and num < 10:
        print()
        print(f"{num}단")
        for i in range(1, 10):
            print(f"{num} * {i} = {num * i}")
    else:
        print("숫자를 다시 입력하세요.")
