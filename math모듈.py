# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.log(100))
print(math.ceil(100.01)) # 소수점 이하를 올림
print(math.floor(100.9)) # 소수점 이하를 절삭

# 실습 문제 1: 가위바위보 승부 판정 (random)
# 컴퓨터가 random.randint로 가위(0)/바위(1)/보(2) 중 하나를 뽑고, 사용자가 입력한 값과 비교해서 승패를 판정하는 프로그램을 작성하세요.
# 무승부가 나오면 같은 값이 나올 때가 아니라,
# 무승부 횟수를 세어 "총 N번 만에 승부가 났습니다"를 출력하도록 반복문을 구성해보세요.
# 힌트: 무인도 탈출 게임의 while True + cnt 패턴 재사용
# 출력 예시: 무승부! 다시 도전합니다... → 당신의 승리! 총 3번 만에 승부가 났습니다.

import random

choices = ["가위", "바위", "보"]
cnt = 0

while True:
    # 1. 반복문 안에서 사용자가 매번 새로 입력하도록 설정
    user = int(input("가위(0) 바위(1) 보(2) 중 선택: "))
    computer = random.randint(0, 2)
    cnt += 1

    # 2. 무승부 처리
    if user == computer:
        print(f"무승부!!! {choices[user]} 다시 도전 합니다.")
        continue

    # 3. 승패 판정 ((user - computer) % 3 공식을 활용)
    # 나머지가 1이면 사용자 승리, 2이면 컴퓨터 승리
    if (user - computer) % 3 == 1:
        print(f"당신의 승리! 총 {cnt}번 만에 승부가 났습니다.")
        break
    else:
        print(f"컴퓨터의 승리! 총 {cnt}번 만에 승부가 났습니다.")
        break
# 실습 문제 2: 로그인 시도 시간 기록기 (datetime + math)
# 사용자가 로그인을 시도할 때마다 현재 시각을 strftime으로 "%Y-%m-%d %H:%M:%S" 형식으로 출력하고,
# 최초 로그인 시각부터 현재까지 경과된 시간을 초 단위로 계산해서 math.floor로 소수점을 버린 정수 초로 출력하세요.
# (같은 코드 안에서 time.sleep으로 몇 초 지연을 준 뒤 두 번째 시각을 구해 차이를 계산하면 됩니다.)
# 힌트: (now2 - now1).total_seconds() 결과에 math.floor 적용
# 출력 예시: 로그인 시각: 2026-09-14 10:31:05 → 2번째 접속까지 경과 시간: 12초