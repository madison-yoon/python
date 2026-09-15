# # 정수 출력
# print(30)
# age = 23
# print("나이: " + str(age))
# print(f"나이: {age}") #f-string 방식으로 출력
#
# # 실수 출력
# avg = 76.6667
# print(f"성적: {avg:.2f}")
#
# # 문자열 출력
# name = "곰돌이사육사"
# print(f'이름: {name}')
# print("이름: " + name)
#
# # 리스트 출력 : 파이썬은 기본적으로 배열이 없고 리스트로 연속된 데이터를 관리함
# score = [99, 88, 77]
#
# # 총합과 평균 계산
# total = sum(score)
# average = total / len(score) #len 요소의 갯수를 세는 방법
#
# # 출력 결과 확인
# print(f"총합: {total}")
# print(f"평균: {average}")
#
# # 여러 줄 출력
# print("""애국가(愛國歌)는 ‘나라를 사랑하는 노래’라는 뜻이에요. 우리나라는 애국가에 특별한 이름을 붙이지 않고 국가(國歌)로 사용하고 있어요.
# 한 세기 가까운 세월 동안 슬플 때나 기쁠 때나 우리 겨레와 운명을 같이 해 온 애국가를 부를 때마다 우리 모두 선조들의 나라 사랑 정신을 새롭게 되새겨보아요.""")
#
# # 줄바꿈 문자 확인
# '''
# \n (Newline / LF - Line Feed): 커서를 바로 아래 다음 줄로 이동시키는 문자입니다.
# 유닉스, 리눅스, 맥OS 및 현재 대부분의 프로그래밍 환경에서 표준 줄바꿈으로 사용됩니다.
# \r (Carriage Return): 커서를 해당 줄의 맨 앞(가장 왼쪽)으로 이동시키는 문자입니다.
# 타자기를 칠 때 글자를 다 치면 캐리지(종이를 넣고 움직이는 부분)를
# 오른쪽에서 왼쪽으로 쾅 하고 밀어 원위치시키던 동작에서 유래했습니다.
# end="\n"으로 원래는 끝나는 것이 숨겨져 있어 새로운 문장에서 한 줄이 밀려나는 것
# '''
#
# # \t \"
# print('apple\tbanana\torange')
#
# # 제어문자, escape sequnce : \n \t \r \\ \b
# print("동해물과\t백두산이\n 마르고 닳도록\b 하느님이")
# print("보우하사\n우리나라 \\만세")
#
# print("안녕하세요. '장원영'님 환영 합니다.")
# print("안녕하세요. \"장원영\"님 환영 합니다.")
#
# print("파이썬")
# print("파"+"이"+"썬")
# print("파""이""썬")
# print("파","이","썬")
#
# # end : 문자열을 출력하고 난 다음의 동작, 기본값이 줄바꿈(\n)
# # sep(seperate) : 문자열 사이에서 콤마를 만나면 동작, 기본값이 스페이스
#
# print("life is short, you need python")
# print("life is short,", "you need python")
#
# print("life is short,", end=" & ")
# print("you", "need", "python", sep="\n")
#
# # 정렬과 포맷 지정
# # < : 왼쪽 정렬
# # > : 오른쪽 정렬 (기본값)
# # ^ : 중앙 정렬
#
# num1 = 10
# num2 = 100
# num3 = 1000
#
# print(f"|{num1:<9}|")
# print(f"|{num2:>9}|")
# print(f"|{num3:^9}|")
#
# # 소수점 이하 출력
# PI = 3.141592
# print(f"{PI}")
# print(f"{PI:.2f}")
#
# # 다양한 출력 스타일
# name = "곰돌이"
# age = 23
# gender = 'M'
# job = "개발자"
# addr = "충남 천안시"
#
# # 파이썬 스타일 2, 가장 최근에 추가된 방식(f-string), 3.6이후
# # f와{}를 사용합니다.
# print("====== 파이썬 스타일2 =====")
# print(f"이름 : {name}")
# print(f"나이 : {age}")
# print(f"성별 : {gender}")
# print(f"직업 : {job}")
# print(f"주소 : {addr}")
#
# # 자바 스타일
# print("====== 자바 스타일 =====")
# print("이름 :" + name)
# print("나이 :" + str(age))
# print("성별 :" + gender)
# print("직업 :" + job)
# print("주소 :" + addr)
#
# # \n, \t를 사용하여 아래와 같은 형태로 자기소개를 한 줄의 print() 문으로 출력하세요.
# name = "김민준"
# job = "백엔드 개발자"
#
# print(f"{name}은 {job}이다.")
#
# # 따옴표 출력하기
# print("\"오늘도 좋은 하루 되세요!\"")
#
# # \r로 커서 이동 확인하기
# print("사과\r바나나\r키위")
#
# # "010" "1234" "5678" 세 문자열을 sep="-"을 활용하여 010-1234-5678로 출력하시오
# print("010","1234","5678", sep = "-")
#
# # 아래 세 개의 print() 문을 각각 장성하되, end 옵션을 이용해 최종적으로 한 줄의 문장이 되도록 만드시오
# # 결과 : 파이썬은 재미있다.
# print("결과 :", end = " ")
# print("파이썬은", end = " ")
# print("재미있다",)
#
# # 두가지 스타일로 자기소개 출력하기
# print(f"이름: {name}")
# print(f"직업: {job}")
# print(f"나이: {age}")
# print("나이: " + str(age))
# print("이름: " + name)
# print("직업: " + job)
#
# # 정렬로 표 만들기
# num1 = 7
# num2 = 42
# num3 = 365
# print(f"|{num1:^6}|")
# print(f"|{num2:^6}|")
# print(f"|{num3:^6}|")
#
# #원이 반지를 r=5를 이용해 원의 넓이(3.14159 * r * r)을 구한 뒤, 폭 10칸 오른쪽 정렬, 소수점 둘째 자리까지 출력
# # 넓이 : 78.54
# PI = 3.141592
# r = 5
# cir = PI * r * r
# print(f"넓이: {cir:>10,.2f}")