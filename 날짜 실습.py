# 실습 1: 나의 생일까지 남은 일수 계산하기
# 오늘 날짜와 올해 생일(예: 12월 25일)까지 남은 일수를 계산해보세요
from datetime import datetime

today = datetime.today()
birthday = datetime(today.year, 9, 29)
formatted = birthday.strftime("%Y%m%d")
formatted2 = today.strftime("%Y%m%d")

print(f"{(birthday - today).days}일 남았습니다.")

# 실습 2: 요일별 인사말 출력하기
# 오늘 요일에 따라 다른 메시지를 출력해보세요
# 월~금: "오늘은 평일입니다. 힘내세요!"
# 토, 일: "오늘은 주말입니다. 푹 쉬세요!"
wd = datetime.today()
today_str = wd.strftime("%A")
workday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
offday = ["Saturday", "Sunday"]
if today_str in workday:
    print("오늘은 평일입니다. 힘내세요!")
elif today_str in offday:
    print("오늘은 주말입니다. 푹 쉬세요!")

# # 오늘 날짜를 기준으로 요일 가져오기 (0: 월요일 ~ 6: 일요일)
# today_index = datetime.date.today().weekday()
#
# # 월요일(0)부터 금요일(4)까지는 평일
# if 0 <= today_index <= 4:
#     print("오늘은 평일입니다. 힘내세요!")
# # 토요일(5), 일요일(6)은 주말
# else:
#     print("오늘은 주말입니다. 푹 쉬세요!")


# 실습 3: 현재 시간대별 인사말 만들기
# 현재 시각(hour)에 따라 다른 인사말을 출력해보세요
# 06~11시: "좋은 아침입니다"
# 12~17시: "좋은 오후입니다"
# 18~22시: "좋은 저녁입니다"
# 그 외: "늦은 밤이네요, 얼른 주무세요"
wt = datetime.today()
time_str = wt.strftime("%H")
mor = 6 <= int(time_str) < 12
noon = 12 <= int(time_str) < 18
night = 18 <= int(time_str) < 22
if today_str in workday:
    print("좋은 아침입니다.")
elif today_str in offday:
    print("좋은 오후입니다.")
elif today_str in offday:
    print("좋은 저녁입니다.")
else:
    print("늦은 밤이네요, 얼른 주무세요")

import datetime

# 현재 시각에서 시간(hour)만 가져오기 (0~23 사이의 정수)
current_hour = datetime.datetime.now().hour

# 시간대별 조건문 작성
if 6 <= current_hour <= 11:
    print("좋은 아침입니다")
elif 12 <= current_hour <= 17:
    print("좋은 오후입니다")
elif 18 <= current_hour <= 22:
    print("좋은 저녁입니다")
else:
    print("늦은 밤이네요, 얼른 주무세요")

# 실습 4: 원하는 형식으로 파일명 생성하기
# strftime을 활용해서 로그 파일명을 만들어보세요.
# 예: "backup_20261014_1530.txt"같은 형식
from datetime import datetime
now = datetime.now()
form = now.strftime("backup_%Y%m%d_%H%M.txt")
print(form)