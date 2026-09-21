# JSON(JavaScript Objdect Notation)은 데이터를 저장하고 교환하는 데 널리 사용되는 경량 텍스트 형식입니다.
# - 파이썬에서는 json 기본 라이브러리를 통해 사용가능
# - 경량 텍스트 포맷
# - 키와 값으로 구성
# - 언어 독립적
# - 웹 API 통신, 설정 파일, 데이터 저장 및 교환 등 다양한 분야에서 활용

import json

# 파이썬 객체를 JSON으로 직렬화
# 회원정보 (이름, 주소, 나이, 성별, 전화번호 2개) => 딕셔너리
# 회원 정보가 10개 인 리스트 => 리스트

members = [
    {
        "name": "안유진",
        "addr": "대전시",
        "age": 23,
        "gender": "여성",
        "position": "리더",
        "phone": ["010-1234-5678","041-123-7899"]
    },
    {
        "name": "가을",
        "addr": "인천시",
        "age": 24,
        "gender": "여성",
        "position": "래퍼",
        "phone": ["010-2345-6789", "032-234-8900"]
    },
    {
        "name": "레이",
        "addr": "나고야시",
        "age": 22,
        "gender": "여성",
        "position": "보컬",
        "phone": ["010-3456-7890", "02-345-9011"]
    },
    {
        "name": "장원영",
        "addr": "서울시",
        "age": 22,
        "gender": "여성",
        "position": "보컬",
        "phone": ["010-4567-8901", "02-456-0122"]
    },
    {
        "name": "리즈",
        "addr": "제주시",
        "age": 22,
        "gender": "여성",
        "position": "메인보컬",
        "phone": ["010-5678-9012", "064-567-1233"]
},
    {
        "name": "이서",
        "addr": "서울시",
        "age": 19,
        "gender": "여성",
        "position": "보컬",
        "phone": ["010-6789-0123", "02-678-2344"]
    }
]

# Python 객체를 JSON으로 직렬화
json_str = json.dumps(members, ensure_ascii=False, indent=4)
print(json_str)

# JSON을 Python으로 역직렬화
obj = json.loads(json_str)
print(obj)

print("-"*130)
for e in obj:
    print(e)
print("-"*130)

# 파일로 저장하기
# with는 파일을 자동으로 닫아줌
with open('data.json',"w", encoding="utf-8") as json_file:
    json.dump(members,json_file, ensure_ascii=False, indent=4)

# 파일에서 읽기
with open('data.json',"r", encoding="utf-8") as json_file:
    data = json.load(json_file)

print(data)