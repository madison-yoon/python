# 3개의 햄버거와 2개의 음료의 가격을 입력 받아 제일 싼 세트 메뉴의 가격 구하기(50원 할인)
# - prompt로 연속해서 햄버거 3개 가격과 음료 2개의 가격을 입력 받음
# - 햄버거 3개 중 가장 싼 가격을 선택하고 음료들 중 싼 음료의 가격을 합산하고 여기서 50원 할인

# mac = list(map(int,input("버거와 음료 가격: ").split()))
# burger = mac[:3]
# bev = mac[3:]
# meal = f"{int(min(burger) + min(bev))}"
# print(f"기존 가격{meal}원 세트 할인 후 {int(meal) - 50}원")

# 리스트 순회 하기 : 5대의 자동차 이름을 입력 받음
# - 범위 기반 for문으로 순회해서 출력 : for i in range()
# - 시퀀스 for문으로 순회해서 출력: for e in 시퀀스
# 오름차순, 내림차순 출력

car = list(input("차 종류를 5가지 입력하세요: ").split())
for i in range(5):
    print(car[i], end=" ")
print()
for e in car:
    print(e, end=" ")
print()
print(sorted(car))
print(sorted(car)[::-1])