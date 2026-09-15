# duty = int(input("주간/야간근무를 선택하세요 : "))
# if duty == 1:
#     schedule = "주간근무"
#     fee = 10320
# elif duty == 2:
#     schedule = "야간근무"
#     fee = int(10320 * 1.5)
# else:
#     schedule = "없음"
#
# if schedule == "없음":
#     print("해당 근무형태는 없습니다.")
# else:
#     print(f"{schedule}을 선택하였습니다.")
#     time = int(input("근무 시간을 입력해 주세요 : "))
#     if time <= 0:
#         print("정산받을 급여가 없습니다.")
#     else:
#         print(f"{time}시간동안 근무한 {schedule} 급여는 {fee * time:,}원입니다.")
#
#
# work_type = int(input("[1]주간근무 [2]야간근무 를 입력 : "))
# work_time = int(input("근무 시간 입력 : "))
# HOUR_PAY = 10030  # 코드내에서 변경 불가의 의미로 대문자 사용
#
# if work_type == 1:
#     pay = work_time * HOUR_PAY  # 주간 근무에 대한 급여
# else:
#     pay = work_time * HOUR_PAY * 1.5  # 야간 근무에 대한 급여
#
# print(f"{work_time}시간 동안 근무한 {work_type == 1 and '주간' or '야간'} 급여는 {pay:,.0f}원 입니다.")