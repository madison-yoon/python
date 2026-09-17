# 에어컨 만들기
# 전원 ON/OFF
# 현재 온도 표시 기능 : 기본값은 20도로 설정
# 온도 조절 기능 (1도씩 조절 가능), 원하는 온도 설정
# 바람 세기 조절 기능 (1단계, 2단계, 3단계)

class AC:
    def __init__(self, name, on, status, temp, force): # 생성자
        self.name = name
        self.on = on
        self.status = status
        self.temp = temp
        self.force = force

    def set_name(self, name):
        self.name = name

    def set_on(self,on):
        self.on = on

    def set_status(self, status):
        self.status = status
        print(f"현재온도 {self.temp} 바람세기 {self.force}")

    def set_temp(self, temp):
        if 16 <= temp <= 32:
            self.temp = temp
        elif temp < 16:
            self.temp = temp
            print("최저 온도입니다.")
        else:
            self.temp = 32
            print("최대 온도입니다.")

    def temp_up(self):
        self.set_temp(self.temp + 1)

    def temp_down(self):
        self.set_temp(self.temp - 1)

    def set_force(self, force):
        if 1 <= force <= 3:
            self.force = force
        elif force < 1:
            self.force = 1
            print("최소 세기는 1단계입니다.")
        else:
            self.force = 3
            print("최대 세기는 3단계입니다.")

    def force_up(self):
        self.set_force(self.force + 1)

    def force_down(self):
        self.set_force(self.force - 1)

    def get_name(self):
        return self.name

    def get_on(self):
        return self.on

    def get_status(self):
        return self.status

    def get_temp(self):
        return self.temp

    def get_force(self):
        return self.force

    def view_ac(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.on]}")
        print(f"현재 온도 : {self.temp}°C")
        print(f"바람 세기 : {self.force}단계\n")

career = AC("career", True, True, 20, 3)
career.view_ac()

career = AC("career", True, True, 20, 3)
career.view_ac()

while True:
    career.view_ac()
    print("--- 에어컨 리모컨 ---")
    print("1. 전원 켜기/끄기")
    print("2. 온도 올리기 (+)")
    print("3. 온도 내리기 (-)")
    print("4. 바람세기 올리기 (+)")
    print("5. 바람세기 내리기 (-)")
    print("0. 종료")

    choice = input("원하는 기능을 선택하세요: ")

    if choice == '1':
        career.set_on(not career.get_on())
        print(f"전원이 {'켜졌습니다.' if career.get_on() else '꺼졌습니다.'}")

    elif choice == '2':
        career.temp_up()

    elif choice == '3':
        career.temp_down()

    elif choice == '4':
        career.force_up()

    elif choice == '5':
        career.force_down()

    elif choice == '0':
        print("에어컨 프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")