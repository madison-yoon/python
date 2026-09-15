# for 문 : 정해진 범위만큼 반복 수행 할 때 효과적
# for 요소 in 시퀀스:
# for 변수 in range(시작값, 최종값, 증감값):

# ive = ["안유진","장원영","이서","가을","레이","리즈"]
# for e in ive: #시퀀스형 데이터를
#     print(e, end=" ")
#
# print()
#
# for i in range(0,6,1):
#     print(ive[i], end=" ")

# 1 ~ 1000 사이 출력
# cnt = 0
# for i in range(1, 100 + 1):
#     if i % 3 == 0:
#         print(f"{i:3}", end =" ")
#         cnt += 1
#         if cnt > 10:
#             print()
#             cnt = 0

# 입력 받은 숫자의 범위 내의 7의 배수를 구하고
# cnt = 0
# for i in range(1, 1000 + 1):
#     if i % 7 == 0:
#         print(f"{i:5}", end=" ")
#         cnt += 1
#         if cnt >= 10:
#             print()
#             cnt = 0
# print()

# 입력 받은 문자열을 뒤집어 출력
# abcdef >fedcba
# text = input("문자열 입력 : ")
# for i in range(len(text) - 1,- 1,-1):
#     print(f"{text[i]}", end = "")

# print()
# # 입력 받은 문자열에서 대문자는 소문자로, 소문자는 대문자로 변경해서 출력하기
# eng = input("문자열 입력 : ")
# new = ""
# for e in eng:
#     if e.isupper():
#         new += e.lower()
#     elif e.islower():
#         new += e.upper()
#     else:
#         new += e
# print(new)
# for i in range(len(eng)):
#     print(eng[i].swapcase(), end="")

# 정수값을 입력 받아 3의 배수, 5의 배수이면 출력, 한줄에 5개씩 출력
# cnt = 0
# num = int(input("정수 입력: "))
#
# for e in range(1, num + 1):  # 이 부분을 range로 감싸주어야 합니다!
#     if e % 3 == 0 or e % 5 == 0:
#         print(e, end=" ")
#         cnt += 1
#         if cnt == 5:
#             print()
#             cnt = 0

# 이중 for문
# 입력 받은 수가 10이라면 10 * 10의 행렬 출력
# num = int(input("정수 입력: "))
# for i in range(1, num + 1): # 1 ~ num
#     for j in range(1, num + 1):
#         print("*", end=" ")
#     print()
# #
# num = int(input("정수 입력: "))
# cnt = 0
# for i in range(1, num + 1): # 1 ~ num
#     for j in range(1, num + 1):
#         cnt += 1
#         print(f"{cnt:4}", end="")
#     print()

# 단일 for문으로 변경해서 출력해보기
# num = int(input("정수 입력: "))
# for i in range(1, num * num + 1):
#     print(f"{i:4}", end="")
#     if i % num == 0:
#         print()

# 2 ~ 9단까지 구구단 출력하기
mul = [2, 3, 4, 5, 6, 7, 8, 9]

for m in mul:  # 2부터 9까지의 단을 하나씩 가져옴
    for i in range(1, 10):  # 1부터 9까지 곱해줌
        print(f"{m} * {i} = {m * i}")
    print()  # 단이 끝날 때마다 줄바꿈