# 연산자 오버로딩은 내장 연산자를 사용자 정의 클래스에 대한 재정의이다.

class Vector20:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        return Vector20(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

v1 = Vector20(1, 2)
v2 = Vector20(3, 4)

v3= v1 + v2
print(v3.x,v3.y)
print(v1 == v2)