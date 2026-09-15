# # order = int(input("구매할 음료를 선택하세요 : "))
# # if  1 > order or order > 4:
# #     print("존재하지 않는 메뉴입니다.")
# # if 1 <= order <= 4:
# #     if order == 1:
# #         coke = int(input("콜라를 선택하셨습니다. 얼마를 투입하시겠습니다?"))
# #         price = 1100
# #         change = coke - price
# #         if coke >= price:
# #             print(f"콜라가 나왔습니다.잔돈{change}원을 거슬러드립니다.")
# #         else:
# #             shortage = price - coke
# #             print(f"{shortage}원이 부족합니다.")
#
# print("[메뉴]")
# print("[메뉴1 : 콜라(1100원)]")
# print("[메뉴2 : 사이다(1000원)]")
# print("[메뉴3 : 커피(700원)]")
# print("[메뉴4 : 생수(600원)]")
# choice = int(input("구매할 음료를 선택하세요 : "))
#
# if choice == 1:
#     name = "콜라"
#     price = 1100
# elif choice == 2:
#     name = "사이다"
#     price = 1000
# elif choice == 3:
#     name = "커피"
#     price = 700
# elif choice == 4:
#     name = "생수"
#     price = 600
# else:
#     name = "없음"
#     price = 0
#
# if name == "없음":
#     print("존재하지 않는 메뉴입니다.")
# else:
#     print(f'{name}({price}원)을 선택했습니다.')
#     money = int(input("투입할 금액을 입력하세요: "))
#
#     if money < price:
#         print(f"투입 금액이 부족합니다.{price - money}원 부족")
#     else:
#         change = money - price
#         print(f"{name}가 나왔습니다. 잔돈 {change}원을 거슬러 드립니다.")