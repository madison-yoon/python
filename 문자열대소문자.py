#대소문자 바꾸기: upper()와 lower()
a = "Hello Python Programming"
print(a.upper())
print(a.lower())

# isupper(), islower()
# 입력 받은 문자열에서 소문자는 대문자로 대문자는 소문자로 변경
for e in a:
    if e.islower():
        print(f"{e.upper()}",end="")
    elif e.isupper():
        print(f"{e.lower()}",end="")
    else:
        print(f"{e}",end="")
print()

#문자열 변경 : replace("","")
input_str = "Hello Python Program"
new_str = input_str.replace("Python", "JavaScript")
print(new_str)

# 문자 갯수 세기 : count
text = "Google kakao naver openAI oole"
print(text.count("o"))

# 문자열 길이 : len()
text = "Hello World"
print(len(text))

# 문자열 찾기 : find()와 rfind(), index()
# find(): 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 -1을 반환합니다.
# index(): 찾은 부분 문자열의 첫 번째 인덱스를 반환합니다. 부분 문자열을 찾지 못하면 ValueError 예외를 발생시킴

phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))  # 뒤에서 부터 찾지만 인덱스는 앞에서 부터

print(phrase.index("포기"))

print(phrase.find("나에게"))  # 찾는 결과 없으면 -1
# print(input_b.index("나에게"))  # 해당 단어가 없으므로 에러가 발생 합니다

new_phrase = phrase.replace("가장", "나에게")
print(new_phrase)

# 문자열 양옆의 공백제거
# - strip(): 양쪽 공백 제거
# - lstrip(): 왼쪽 공백 제거
# - rstrip(): 오른쪽 공백 제거

input_a = """
안녕하세요.

문자열 함수를 알아 봅니다.

"""

print(input_a.strip())