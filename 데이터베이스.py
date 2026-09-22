import pymysql

# 1. DB 연결
def get_connection():
    conn = pymysql.connect(host="127.0.0.1", user="root", port=3306,
                           password="1234", database="mysqlDB", charset="utf8")
    return conn

def create_user_table(conn):
    cur = conn.cursor()

    # 2. 기존 테이블 삭제 및 생성
    cur.execute("DROP TABLE IF EXISTS userTable")
    cur.execute("""
        CREATE TABLE userTable (
            id CHAR(10) PRIMARY KEY,
            pwd CHAR(15),
            name CHAR(20),
            email CHAR(20),
            addr CHAR(50)
        )
    """)
    conn.commit()
    conn.close()

# 3. 초기 데이터 삽입
def create_insert_user(conn):
    cur = conn.cursor()
    users = [
        ('ayj1234', '12345678', '안유진', 'ayj@gmail.com', '서울시 강남구'),
        ('jwy1234', '12345678', '장원영', 'jwy@gmail.com', '서울시 강남구'),
        ('fall1234', '12345678', '가을', 'fall@gmail.com', '서울시 강남구'),
        ('ys1234', '12345678', '이서', 'ws@gmail.com', '서울시 강남구'),
        ('lay1234', '12345678', '레이', 'lay@gmail.com', '서울시 강남구'),
        ('liz1234', '12345678', '리즈', 'liz@gmail.com', '서울시 강남구')
    ]

    for user in users:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", user)

    # 4. 커밋 및 연결 종료
    conn.commit()
    conn.close()

# 신규 회원 추가
def insert_user(conn):
    cur = conn.cursor()
    id = input("아이디 : ")
    if id == 'exit': return "exit"
    pwd = input("패스워드 : ")
    name = input("이름 : ")
    mail = input("이메일 : ")
    addr = input("주소 : ")
    try:
        cur.execute("INSERT INTO userTable VALUES(%s, %s, %s, %s, %s)", (id, pwd, name, mail, addr))
        conn.commit()
        print("성공적으로 등록되었습니다.")
    except Exception as e:
        print(f"오류 발생 : {e}")
    finally:
        cur.close() # 커서만 닫아줌


# from datetime import datetime
#
# def signup_user(conn):
#     cur = conn.cursor()
#
#     name = input("이름 : ")
#     user_id = input("이메일 : ")
#     if user_id == 'exit':
#         return "exit"
#     pwd = input("패스워드 : ")
#
#     register_date = datetime.now().strftime('%Y%m%d')
#
#     try:
#         sql = "INSERT INTO userTable (name, email, pwd, register_date) VALUES (%s, %s, %s, %s)"
#         cur.execute(sql, (name, email, pwd, register_date))
#         conn.commit()
#         print("성공적으로 회원가입이 되었습니다.")
#
#     except pymysql.err.IntegrityError as e:
#         # MySQL 중복 키 에러 번호인 1062번 확인
#         if e.args[0] == 1062:
#             print("오류 발생 : 이미 존재하는 아이디입니다.")
#         else:
#             print(f"오류 발생 : {e}")
#
#     except Exception as e:
#         print(f"오류 발생 : {e}")
#
#     finally:
#         cur.close()


# 2. 회원 수정 (원하는 항목만 수정, 엔터 시 기존 값 유지)
def update_user(conn):
    cur = conn.cursor()
    id = input("수정할 사용자의 아이디: ")

    # 해당 아이디가 존재하는지 확인하고 기존 정보 가져오기
    # 테이블 구조: id(0), pwd(1), name(2), email(3), addr(4) 라고 가정
    cur.execute("SELECT * FROM userTable WHERE id = %s", (id,))
    user = cur.fetchone()

    if not user:
        print("존재하지 않는 아이디입니다.")
        return

    print(f"\n[{user[2]}님 정보 수정] 변경하지 않고 유지하려면 그냥 엔터를 누르세요.")

    # 기존 값을 변수에 미리 담아둡니다.
    orig_name = user[2]
    orig_pwd = user[1]
    orig_email = user[3]
    orig_addr = user[4]

    # 새롭게 입력받되, 빈 문자열("")이면 기존 값을 그대로 사용합니다.
    new_name = input(f"새 이름 [{orig_name}]: ") or orig_name
    new_pwd = input(f"새 패스워드 [기존 유지]: ") or orig_pwd
    new_email = input(f"새 이메일 [{orig_email}]: ") or orig_email
    new_addr = input(f"새 주소 [{orig_addr}]: ") or orig_addr

    try:
        sql = "UPDATE userTable SET name = %s, pwd = %s, email = %s, addr = %s WHERE id = %s"
        cur.execute(sql, (new_name, new_pwd, new_email, new_addr, id))
        conn.commit()
        print("성공적으로 수정되었습니다.")
    except Exception as e:
        print(f"수정 중 오류 발생: {e}")
    finally:
        cur.close()


# 3. 회원 삭제
def delete_user(conn):
    cur = conn.cursor()
    id = input("삭제할 사용자의 아이디: ")

    # 존재 여부 확인
    cur.execute("SELECT * FROM userTable WHERE id = %s", (id,))
    if not cur.fetchone():
        print("존재하지 않는 아이디입니다.")
        return

    confirm = input(f"정말 '{id}' 사용자를 삭제하시겠습니까? (y/n): ")
    if confirm.lower() == 'y':
        try:
            cur.execute("DELETE FROM userTable WHERE id = %s", (id,))
            conn.commit()
            print("삭제되었습니다.")
        except Exception as e:
            print(f"삭제 중 오류 발생: {e}")
    else:
        print("삭제가 취소되었습니다.")

    cur.close()


# 4. 회원 조회
def search_user(conn):
    cur = conn.cursor()
    id = input("조회할 사용자의 아이디: ")

    try:
        cur.execute("SELECT id, name, email, addr FROM userTable WHERE id = %s", (id,))
        user = cur.fetchone()

        if user:
            print(f"\n--- [회원 정보] ---")
            print(f"아이디 : {user[0]}")
            print(f"이름   : {user[1]}")
            print(f"이메일 : {user[2]}")
            print(f"주소   : {user[3]}")
        else:
            print("존재하지 않는 사용자입니다.")
    except Exception as e:
        print(f"조회 중 오류 발생: {e}")
    finally:
        cur.close()


# 5. 사용자 전체 조회 (메뉴 5번용)
def search_all_users(conn):
    cur = conn.cursor()
    try:
        cur.execute("SELECT id, name, email, addr FROM userTable")
        users = cur.fetchall()

        if not users:
            print("등록된 사용자가 없습니다.")
            return

        print("\n==================== 전체 사용자 목록 ====================")
        print(f"{'아이디':<10} | {'이름':<10} | {'이메일':<20} | {'주소'}")
        print("-" * 60)
        for user in users:
            print(f"{user[0]:<10} | {user[1]:<10} | {user[2]:<20} | {user[3]}")
        print("========================================================")
    except Exception as e:
        print(f"전체 조회 중 오류 발생: {e}")
    finally:
        cur.close()

# 메뉴 출력
def print_menu():
    print("\n===== 사용자 관리 메뉴 =====")
    print("1. 사용자 추가")
    print("2. 사용자 수정")
    print("3. 사용자 삭제")
    print("4. 사용자 조회")
    print("5. 사용자 전체 조회")
    print("0. 종료")
    print("============================")

def main():
    conn = get_connection() # DB 연결
    create_user_table(conn) # 테이블 생성
    conn = get_connection() # DB 연결
    create_insert_user(conn)# 초기 회원 정보 추가

    while True:
        conn = get_connection()
        print_menu()
        choice = input("선택: ")

        if choice == "1":
            insert_user(conn)
        elif choice == "2":
            update_user(conn)
        elif choice == "3":
            delete_user(conn)
        elif choice == "4":
            search_user(conn)
        elif choice == "5":
            search_all_users(conn)
        elif choice == "0":
            print("프로그램을 종료 합니다.")
            conn.close()
            break
        else:
            print("잘못된 선택입니다. 다시 입력하세요.")


    # while True:
    #     conn = get_connection()
    #     rst = new_user_insert(conn)
    #     if rst == "exit": break

if __name__ == "__main__":
    main()
