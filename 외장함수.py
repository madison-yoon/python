# 외장함수 : 파이썬에서 기본 제공, 단 import해서 사용

# 랜덤 함수: 난수 발생기
# randint(m,n) : 지정된 범위 안의 임의의 정수 생성
# 1번 방법
# import random
# from math import radians
#
# for i in range(20):
#     print(f"{random.randint(1,10)}", end=" ") # 1~10 사이의 임의의 값 생성
# print()
# 2번 방법
# from random import radiant
#
# for i in range(20):
#     print(f"{randint(1,10)}", end=" ") # 1~10 사이의 임의의 값 생성
# print()

# randrange(m,n,p) = randint(1,10)은 1~10 모두 활용 randrange는 1~9까지
#     print(f"{random.randrange(1,10,2)}", end=" ") # 1~9 사이의 임의의 값 생성 첫 기준으로 다음껀 빼서 홀수만 출력
# print()

# 무인도 탈출 게임
# 두개의 주사위를 굴려 같은 값이 나오면 "무인도를 탈출했습니다. 탈출 시도 횟수, 두개의 주사위 값

import random

cnt = 0

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"주사위1 ({dice1}),주사위2 ({dice2})")
    if dice1 == dice2:
        print(f"{dice1},{dice2} {cnt}번만에 무인도를 탈출 했습니다.")
        break
    else:
        cnt += 1
        print("탈출 시도")
print()

print("로또 번호 생성기")
lotto = []
while True:
    value = random.randint(1, 45)
    if value not in lotto:
        lotto.append(value)
    if len(lotto) == 6:
        break
print(sorted(lotto))

# 날짜 및 시간 관련 처리 모듈

from datetime import datetime
datetime.today()
datetime.today().year
datetime.today().month
datetime.today().day
datetime.today().hour

print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 오늘은 2024년 10월 12일 토요일 10시 31분입니다.
# 현재 시간 가져 오기
# %y : 4자리 연도
# %m : 2자리 월
# %d : 2자리 일
# %A : 요일 표시
# %H : 24시간 형식의 시간
# %M : 분 표시
now = datetime.now()
#원하는 출력 형식 만들기
formatted = now.strftime("오늘은 %Y년 %m월%d일 %A %H시%M분입니다.")
print(formatted)

