# - 사용자로부터 좌석번호(index)를 입력받아 예매하는 시스템이다.
# - 예매가 완료되면 해당 좌석 값을 1로 변경한다.
# - 이미 예매가 완료된 좌석은 재구매할 수 없다.
# - 한 좌석당 예매 가격은 12000원이다.
# - 프로그램 종료 후, 해당 영화관의 총 매출액을 출력한다.

# 영화표 예매하기
TICKET_PRICE = 12000
seat = [0] * 10

# 좌석 상태를 표시하는 메뉴 만들기
def print_seat():
    for e in seat: # 향상된 for문으로 좌석의 갯수 만큼 순회
        if e == 0 : print("[ ]", end="") # 판매 안된 좌석
        elif e == 1 : print("[V]", end="") # 판매 된 좌석
    print()

# 총 매출액 구하기
def amount():
    cnt = 0
    for e in seat:
        if e == 0: cnt += 1
    return cnt * TICKET_PRICE

# 좌석 예약 하기
def select_seat():
    print_seat() # 현재 예약 가능한 좌석 보여 주기
    num = int(input("좌석 번호를 선택하세요: ")) - 1 #선택된 좌석번호는 1부터 시작하고 인덱스는 0 부터 시작해서 -1
    if seat[num] == 0:
        seat[num] = 1
        print_seat()
    else:
        print("이미 예약된 좌석 입니다.")

while True:
    sel = int(input("[1]예매하기 [2]종료하기: "))
    if sel == 1: select_seat()
    elif sel == 2:
        print(f"총 매출액 : {amount()}원")
        break