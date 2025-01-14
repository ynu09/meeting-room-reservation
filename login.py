import csv

# 로그인 데이터 불러오기
def load_login_data():
    users = {} # 사용자 정보 저장
    with open('login.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) # 첫 행 건너뛰기 
        for row in reader:
            users[row[0]] = row[1] # 빈 딕셔너리에 아이디, 비번 저장 
    return users

# 사용자 인증
def authenticate(username, password, users):
    if username in users and users[username] == password: # 사용자 정보에 있는지 확인 
        return True
    return False

# 회원가입
def register_user(username, password):
    with open('login.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])