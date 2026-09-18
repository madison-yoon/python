# 상속 : 부모클래스에서 만든 변수와 메서드를 물려 받아 사용할 수 있음
# 오버라이딩 : 상속 받아 재정의하는것 / 기능이 개선된 것(그대로 물려받으면 상속)
# = ex) 100마력의 자동차가 120마력으로 개선됨 (오버라이딩 O)
# != ex) 상속 전 없던 자율주행 기능이 추가됨 (오버라이딩 X)

class ProtoTV: # 상속을 주기 위한 부모 클래스
    # 전원, 채널, 볼륨을 매개변수로 하는 생성자 생성
    def __init__(self,on,channel,volume):
        self.on = on
        self.channel = channel
        self.volume = volume

    def set_on(self,on):
        if on:
            self.on = True
            print("전원이 켜졌습니다.")
        else:
            self.on = False
            print("전원이 꺼졌습니다.")


    def set_channel(self,channel):
        if 1 <= channel <= 1000:
            self.channel = channel
        elif channel == 0:
            channel = 1000
            self.channel = channel
        elif channel == 1001:
            channel = 1
            self.channel = channel

    def channel_up(self):
        self.set_channel(self.channel + 1)
        print(f"현재 채널: {self.channel}")

    def channel_down(self):
        self.set_channel(self.channel - 1)
        print(f"현재 채널: {self.channel}")

    def set_volume(self,volume):
        if 1 <= volume <= 100:
            self.volume = volume
        elif volume == 0:
            volume = 1
            print("최저 볼륨에 도달했습니다.")
            self.volume = volume
        elif volume == 101:
            volume = 100
            print("최대 볼륨에 도달했습니다.")
            self.volume = volume

    def volume_up(self):
        self.set_volume(self.volume + 1)
        print(f"현재 볼륨: {self.volume}")

    def volume_down(self):
        self.set_volume(self.volume - 1)
        print(f"현재 볼륨: {self.volume}")

    def get_on(self):
        return self.on

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

    def veiw_tv(self):
        power = ("OFF","ON")
        print(f"전원 : {power[self.on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

class ProductTV(ProtoTV):
    def set_channel(self,cnl):
        if 1 <= cnl <= 2000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

ProtoTV = ProtoTV(True, 1, 10)

while True:
    ProtoTV.veiw_tv()
    print("--- TV 리모컨 ---")
    print("1. 전원 켜기/끄기")
    print("2. 채널 올리기 (+)")
    print("3. 채널 내리기 (-)")
    print("4. 음량 올리기 (+)")
    print("5. 음량 내리기 (-)")
    print("0. 종료")

    choice = input("원하는 기능을 선택하세요: ")

    if choice == '1':
        ProtoTV.set_on(not ProtoTV.get_on())

        if not ProtoTV.get_on():
            print("TV를 종료합니다.")
            break

    elif choice == '2':
        ProtoTV.channel_up()

    elif choice == '3':
        ProtoTV.channel_down()

    elif choice == '4':
        ProtoTV.volume_up()

    elif choice == '5':
        ProtoTV.volume_down()

    elif choice == '0':
        print("TV를 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")