# - 부모 클래스가 선언한 메소드에 대해 반드시 상속받은 클래스에서 기능 구현 해야 하는 특성 (구현하지 않으면 에러 발생)
# - 추상 메서드가 포함된 부모 클래스는 객체로 만들 수 없고 단지 상속을 주기 위해서만 존재
# - 사용자 또는 프로그램 개발자가 연결되는 네트워크에 대한 구조를 몰라도 추상화를 통해 연결 기능을 제공 할 수 있음

from abc import *

class NetworkAdapter(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

class LAN(NetworkAdapter):
    def __init__(self,company):
        self.company = company
    def connect(self):
        print(f"{self.company} LAN에 연결했습니다.")

class WIFI(NetworkAdapter):
    def __init__(self,company):
        self.company = company
    def connect(self):
        print(f"{self.company} WI-FI에 연결했습니다.")

class LTE(NetworkAdapter):
    def __init__(self,company):
        self.company = company
    def connect(self):
        print(f"{self.company} LTE에 연결했습니다.")

net = input("연결할 네트워크를 선택 [1]LAN, [2]WI-FI, [3]LTE: ")
if net == "1":
    adapter = LAN("KT Megapass")
    adapter.connect()
elif net == "2":
    adapter = WIFI("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = LTE("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")