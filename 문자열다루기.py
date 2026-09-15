# 문자열 : 문자가 연속으로 존재하는 것, 파이썬은 문자와 문자열을 구분하지 않음(전부 문자열)
# " ",' ',""" """,''' '''
# from 연산자 import current_year

#인덱싱과 슬라이싱
#인덱싱은 인덱스로 원하는 값을 추출
# text = "안녕하세요. 파이썬 입니다"
# print(text[0]) #안
# print(text[7]) #파
# print(text[-1]) #다
#
# print(text[7:10])
# print(text[::2])
# print(text[::-1])
# print(text[9:6:-1])
# print(text[:5])

from datetime import datetime

current_year = datetime.now().year
jumin = input("주민등록번호: ")
key = int(jumin[7])
year = int(jumin[:2])
mon = int(jumin[2:4])
day = int(jumin[4:6])

if key == 1 or key == 2:
    birth_year = year + 1900
    print(f"{birth_year}년{mon:02d}월{day:02d}일")
else:
    birth_year = year + 2000
    print(f"{birth_year}년{mon:02d}월{day:02d}일")

if key == 1 or key == 3:
    print("성별: 남성")
else:
    print("성별: 여성")

# 두 자리 year가 아닌 4자리 birth_year를 빼야 정상적인 나이가 계산됩니다.
print(f"나이: {current_year - birth_year}살")