# while
# for i in range(초기값, 최종값, 증감값)
# for i in 시퀀스

# n = int(input("정수 입력: "))
# total = 0
# while n > 0:
#     total += n
#     n -= 1
#
# for i in range(1,n + 1):
#     total += i
#
# while True:
#     total += n
#     n -= 1
#     if n == 0: break
#
# print(total)

# 입력 받은 숫자의 합 구하기 (리스트)
# score = list(map(int, input("정수 입력: ").split()))
# # total = 0
# # for i in range(0, len(score)):
# #     total += score[i]
# for e in range(len(score)-1, - 1, -1):
#     # total += e
#     print(score[e], end=" ")

# 구구단
# for dan in range(2, 10):
#     print()
#     print(f"{dan}단")
#     for num in range(1, 10):
#         print(f"{dan} * {num} = {dan * num}")

# 입력 5
# n = int(input("갯수 지정 : "))
# for i in range(n):
#     for j in range(n - i):
#         print("*", end=" ")
#     print()

# continue : 반복문에서 아래의 문장을 수행하지 않고 반목문으로 이동
# n = int(input("정수 입력: "))
# for i in range(n):
#     if i % 2 == 0: continue
#     print(i)
# 2로 나눈 몫이 0일 때 짝수일 경우 컨티뉴문을 만나 홀수만 걸러내는 구문

n = int(input("정수 입력: "))
for i in range(n):
    if i % 3 == 0 or i % 5 == 0: continue
    print(i)