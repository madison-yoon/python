# 기본 메뉴 추가
import json

menu = {
    "americano": ["coffee", 2000, "기본 커피 입니다."],
    "espresso": ["coffee", 2500, "진한 커피 입니다."],
    "latte": ["coffee", 4000, "우유가 들어간 커피 입니다."],
    "green tea": ["tea", 4500, "녹차 입니다."],
    "black tea": ["tea",4500, "홍차 입니다."]
}

# 전체 메뉴 조회
def print_menu():
    for e in menu:
        print(f"{e} - {menu[e]}")

# 개별 메뉴 조회
def get_menu(name):
    if name in menu:
        print(f"{name} - {menu[name]}")
    else:
        print("찾는 메뉴가 없습니다.")

# 메뉴 추가
def insert_menu():
    name = input("추가할 메뉴 이름을 입력하세요: ")
    if name not in menu:
        category = input("카테고리를 입력하세요 (예: coffee, tea): ")
        price = int(input("가격을 입력하세요: "))
        desc = input("메뉴 설명을 입력하세요: ")
        print(f"'{name}' 메뉴가 추가되었습니다.")
        menu[name] = [category, price, desc]
    else:
        print("이미 존재하는 메뉴입니다.")
# 메뉴 삭제
def delete_menu():
    name = input("삭제할 메뉴 이름을 입력하세요: ")
    if name in menu:
        del menu[name]
        print(f"'{name}' 메뉴가 삭제되었습니다.")
    else:
        print("삭제할 메뉴가 존재하지 않습니다.")

# 메뉴 수정
def update_menu():
    name = input("수정할 메뉴 이름을 입력하세요: ")
    if name in menu:
        category = input("카테고리를 입력하세요 (예: coffee, tea): ")
        price = int(input("가격을 입력하세요: "))
        desc = input("메뉴 설명을 입력하세요: ")
        menu[name] = [category, price, desc]
        print(f"'{name}' 메뉴가 수정되었습니다.")
    else:
        print("수정할 메뉴가 존재하지 않습니다.")

# 파일에서 불러 오기
def load_menu():
    try: #예외가 발생하기 쉬운 구간에 사용
        with open("menu.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("해당 파일이 존재 하지 않습니다.")
    except json.JSONDecodeError:
        print("JSON 디코딩 실패")

# 파일 저장하기
def save_menu():
    with open("menu.json", "w", encoding="utf-8") as file:
        json.dump(menu, file, ensure_ascii=False, indent=4)
        print("menu.json 파일에 저장되었습니다.")

# 전체 메뉴 만들기
# [1] 전체 메뉴 보기 [2] 개별 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 메뉴 수정 [6] 종료하기
while True:
    print("메뉴를 선택 하세요: ")
    choice = int(input("[1]전체 메뉴 [2]조회 [3]추가 [4]삭제 [5]수정 [6]로딩 [7]저장 [0]종료 : "))

    if choice == 1:
        print_menu()
    elif choice == 2:
        name = input("조회할 메뉴 이름을 입력하세요: ")
        get_menu(name)
    elif choice == 3:
        insert_menu()
    elif choice == 4:
        delete_menu()
    elif choice == 5:
        update_menu()
    elif choice == 6:
        menu = load_menu()
    elif choice == 7:
        save_menu()
    elif choice == 0:
        print("프로그램을 종료합니다.")
        break