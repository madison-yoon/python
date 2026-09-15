# 반복문 : 주어진 조건이 참인 동안 반복 수행 함
# while문 : 주로 반복 횟수를 알기 알 수 없을 때
# for문 : 반복 횟수가 정해져 있을 때

# n = int(input("정수 입력: "))
# total = 0 # 합계를 저장할 변수
# # while n > 0: # 반복문의 조건인 n의 값이 0보다 클 경우
# #     total += n # total = total + n
# #     n -= 1 # n = n - 1 , n의 값을 변경해서 반복문을 빠져 나가게 함
# for i in range(1, n + 1):
#     total += i
# print(f"합: {total}")

# while 문은 반복 횟수를 알 수 없을 때 사용하면 좋음
# 성별을 받는데 남성은 M, 여성은 F로 입력 받음, 잘못된 입력이면 계속 다시 입력 받음
while True:
    gender = input("성별을 입력하세요: ").upper()
    if gender == "M" or gender == "F":
        break
    print("성별을 잘못 입력하셨습니다.")

print(f"{'남성' if  gender == 'M' else '여성'}입니다.")