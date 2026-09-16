# 입력으로 들어오는 수의 평균을 구해서 반환
# def avg(num):
#     return sum(num) / len(num)
# num = list(map(int, input("정수 입력:").split(",")))
# print(f"{avg(num):.2f}")

def choice(x, y, z):  # 매개변수 3개를 받도록 수정
    if x > y >= z or x > z >= y:
        return x
    elif y > x >= z or y > z >= x:
        return y
    else:
        return z

# 쉼표(,)로 구분하여 3개의 정수 입력받기
x, y, z = list(map(int, input("3가지 정수 입력: ").split(",")))

# 함수를 호출할 때 입력받은 변수 a, b, c를 전달
print(f"최댓값: {choice(x, y, z)}")