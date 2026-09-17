class Television: #클래스 이름은 대문자로 시작
    def __init__(self, name, on, channel, volume): # 생성자
        self.name = name
        self.on = on
        self.channel = channel
        self.volume = volume

    def set_on(self, on):
        self.on = on

    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
        else:
            print("볼륨값 입력 범위를 초과했습니다.")

    def get_on(self):
        return self.on

    def get_channel(self):
        return self.channel

    def get_volume(self):
        return self.volume

    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨 : {self.volume}")

lg_tv = Television("LG", True, 10, 110)
lg_tv.view_tv()
samsung_tv = Television("Samsung", False, 20, 20)
samsung_tv.view_tv()
