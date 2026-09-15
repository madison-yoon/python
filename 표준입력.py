# # 표준입력이란? 콘솔로 부터 사용자의 입력을 받음
# # - 기본적으로 문자열로 반환되며, 다른 데이터형으로 변환하려면 형변환 함수 사용해야 함
#
# # 이름(문자열), 나이(정수), 성별(문자열), 주소(문자열), 평균(실수) 입력 받아 출력해보기
# # name = input("이름 입력: ")
# # age = int(input("나이 입력: ")) #문자열로 입력 받은 나이를 정수로 변환
# # gender = input("성별입력(M/F): ").upper() #대문자로 반환
# # addr = input("주소 입력: ")
# # kor = int(input("국어점수 입력: "))
# # eng = int(input("영어점수 입력: "))
# # math = int(input("수학점수 입력: "))
# # total = (kor+eng+math)
# # avg =((kor+eng+math)/3)
# # score = list(map(int, input("국어 영어 수학: ").split()))
# # # split은 공백 기준으로 나눈다.
# #
# # print(f"이름: {name}")
# # print(f"나이: {str(age)}")
# # print(f"성별: {'남성' if gender == 'M' else '여성'}")
# # print(f"주소: {addr}")
# # print(f"총점: {sum(score)}")
# # print(f"평균: {sum(score)/3:.2f}")
#
# # 시간을 24제로 23:56:45 입력 받아 12제로 변환해서 11시56분45초 형태로 출력하기
# # split(":")
#
# # hour, minute, sec = input("24시간 시:분:초 > ").split(":")
# # hour = int(hour)
# # minute = int(minute)
# # sec = int(sec)
# # if hour == 12:
# #     print(f"오후{hour:02}시{minute:02}분:{sec:02}초")
# # elif hour > 12:
# #     hour -= 12 # hour = hour - 12
# #     print(f"오후{hour:02}시{minute:02}분:{sec:02}초")
# # else:
# #     print(f"오전{hour:02}시{minute:02}분:{sec:02}초")
#
# # 이름과 주소 입력 : " 안내 문구로 이름과 주소를 공백으로 구분해서 한 번에 입력받고 스플릿 활용하여 각각 출력
# name, addr = input("이름,주소 입력:").split()
# print(f"이름 : {name}")
# print(f"주소 : {addr}")
# "시:분:초:" "안내 문구로 14:5:9 형태의 시간을 콜론으로 입력 받아 map을 정수로 반환하여 각 자리를 2자리 폭에 0으로 출력
# hour, minute, sec = list(map(int,input("시:분:초 > ").split(":")))
# print(f"{hour:02}:{minute:02}:{sec:02}")
#
#
# # 국어 영어 수학 : 세 과목을 입력 받아 평균 60점 이상이면 합격 아니면 불합격을 삼항 연산자로 출력하세요
# kor, eng, math = list(map(int,input("국어 영어 수학 입력 : ").split()))
# avg = (kor+eng+math)/3
# print(f"{'합격' if avg >= 60 else '불합격'}")
# # if avg == 60:
# #     print(f"평균 {avg:.2f}점으로 합격입니다.")
# # elif avg > 60:
# #     print(f"평균 {avg:.2f}점으로 합격입니다.")
# # else:
# #     print(f"평균 {avg:.2f}점으로 불합격입니다.")
# #
#
