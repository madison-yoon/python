# 입력으로 들어오는 수의 평균을 구해서 반환
# def avg(num):
#     return sum(num) / len(num)
# num = list(map(int, input("정수 입력:").split(",")))
# print(f"{avg(num):.2f}")

# 세자리 정수 중 큰 수 구하기
def slice_num(num):
    x = num // 100
    y = (num % 100) // 10
    z = num % 10
    return (x, y, z)
num = int(input("3자리 수 입력: "))
x, y, z = slice_num(num)
if x > y >= z or x > z >= y:
    print(f"'{x}' 100의 자리 수가 가장 큽니다.")
elif y > x >= z or y > z >= x:
    print(f"'{y}' 10의 자리 수가 가장 큽니다.")
else:
    print(f"'{z}' 1의 자리 수가 가장 큽니다.")
