# 리스트 : 연속적으로 저장되는 형태의 자료형 요소
# - 크기 지정이 필요 없음
# - 같은 데이터형일 필요가 없음
# - []대괄호로 감싸서 표현, 0개 이상의 원소가 저장될 수 있음
# - 읽고 쓰기가 가능
from enum import member

# 과목의 수를 알 수 없는 성적을 입력받아, 총점과 평균 구하기
# score = list(map(int, input("성정 입력: ").split()))
# print(f"총점 : {sum(score)}, 평균 {sum(score)/len(score)}")

# mixed = ["안유진", 23, True, [100, 200, 300],["서울", "대전", "대구", "부산"], {"주소": "경기도"}]
#
# # 안유진 이름 출력
# print(mixed[0])
#
# # 100,200,300 출력
# print(mixed[3])
#
# # "안유진", 23, True 출력
# print(mixed[0:3])
#
# # 대전 출력
# print(mixed[4][1])
#
# # 경기도 출력
# print(mixed[5]["주소"])
#
# # 부산의 부 출력
# print(mixed[4][3][0])
#
# member = [
#     {
#         "name": "정경수",
#         "addr":"경기도 수원시"
#     },
#     {
#         "name": "안유진",
#         "addr": "대전시"
#     },
#     {
#         "name": "레이",
#         "addr": "인천시"
#     },
#     {
#         "name": "이서",
#         "addr": "충청남도"
#     }
# ]
#
# print(member[0])

# 요소 추가
list_a = [1,2,3]
print(list_a)
list_a.append(4)
print(list_a)
list_a.append(5)
print(list_a)
list_a.append(6)
print(list_a)
list_a.append(7)
print(list_a)
list_a.insert(1,1000)
print(list_a)

# 리스트 삭제
# pop : 인덱스가 없으면 맨 마지막값 제거, 인덱스가 있으면 위치값 제거, 보여줌
print(list_a.pop())
print(list_a)
print(list_a.pop(1))
print(list_a)
print(list_a.remove(3))
print(list_a)
print(list_a.remove(6))
print(list_a)
del list_a[1]
print(list_a)
list_a.clear()
print(list_a)

# 중복제거
my_list = ['A','E','B','D','D',"E",'C']
new_list = []
for v in my_list:
    if v not in new_list:
        new_list.append(v)
        print(new_list)
print(sorted(new_list))

test_list = {'A','E','B','D','D',"E",'C'}
print(test_list)
print(sorted(test_list)) #sorted는 무조건 리스트로 반환

# 10개의 임의의 숫자를 입력 받아 홀수와 짝수 리스트에 나눠 담아서 출력하기
import random

even_list = []
odd_list = []

selected_numbers = random.sample(range(1, 101), 10)
for random in selected_numbers:
    if random % 2 == 1:
        odd_list.append(random)
    else:
        even_list.append(random)
print(f"짝수: {even_list}")
print(f"홀수: {odd_list}")
