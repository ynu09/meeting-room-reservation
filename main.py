'''
파일명: ynu_reservation_sys (main.py, login.py, reservation.py, data.py)
프로그램: Hello 회의실 예약 시스템
작성자: 서연우
작성일: 2024-08-02

test할 경우 아이디/비번 예시: user1/pass1
'''
from datetime import * 
import tkinter as tk
from tkinter import messagebox

from login import load_login_data, authenticate, register_user
from reservation import *
from data import load_reservations

'''
로그인
'''

def login_app():
    global username_entry, password_entry, root
    root = tk.Tk() # 창 생성 
    root.title("회원 로그인")

    tk.Label(root, text="아이디:").grid(row=0, column=0)
    username_entry = tk.Entry(root) # 값 입력받기 
    username_entry.grid(row=0, column=1)

    tk.Label(root, text="비밀번호:").grid(row=1, column=0)
    password_entry = tk.Entry(root, show="*") # 비밀번호 숨기게 
    password_entry.grid(row=1, column=1)

    # 로그인 버튼 
    login_button = tk.Button(root, text="로그인", command=try_login)
    login_button.grid(row=2, column=1)

    # 회원가입 버튼
    register_button = tk.Button(root, text="회원가입", command=register_app)
    register_button.grid(row=2, column=0)

    root.mainloop() # 이벤트 메시지 루프 

def try_login():
    username = username_entry.get() # 입력값 가져오기 
    password = password_entry.get()
    users = load_login_data() # csv 파일 불러오기

    # login.py 함수
    if authenticate(username, password, users):
        messagebox.showinfo("Login Success", "로그인 성공!") # 제목, 메시지 
        root.destroy() # Tkinter 창 닫기
        terminal() # 메인 함수로 
    else:
        messagebox.showerror("Login Failed", "아이디 또는 비밀번호가 잘못되었습니다.")

'''
회원가입 (로그인 창과 동일하게 구현)
'''

def register_app():
    global register_window, reg_username_entry, reg_password_entry
    register_window = tk.Toplevel(root)
    register_window.title("회원가입")

    tk.Label(register_window, text="아이디:").grid(row=0, column=0)
    reg_username_entry = tk.Entry(register_window)
    reg_username_entry.grid(row=0, column=1)

    tk.Label(register_window, text="비밀번호:").grid(row=1, column=0)
    reg_password_entry = tk.Entry(register_window)
    reg_password_entry.grid(row=1, column=1)

    register_button = tk.Button(register_window, text="확인", command = try_register)
    register_button.grid(row=2, columnspan=2)

def try_register():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if username and password:
        register_user(username, password)
        messagebox.showinfo("Register Success", "회원가입 완료되었습니다.")
        register_window.destroy()
    else:
        messagebox.showerror("Register Failed", "잘못된 입력입니다.")

'''
터미널 창 입력
'''
def terminal():
    while True:
        print("""
        ================================
        == Hello 회의실 예약 프로그램 ==
        ================================

            ************************
            1. 예약        4. 취소        
            2. 조회        5. 연장
            3. 수정        0. 종료 
            ************************
        """)

        choice = int(input("선택: "))

        # csv 파일 불러오기 
        reservations = load_reservations()
    
        
        if choice == 1:
            make_reservation(reservations)
        elif choice == 2:
            view_reservations(reservations)
        elif choice == 3:
            modify_reservation(reservations)
        elif choice == 4:
            cancel_reservation(reservations)
        elif choice == 5:
            extend_reservation(reservations)
        elif choice == 0:
            save_reservations(reservations)
            print("이용해주셔서 감사합니다.")
            break
        # 맞게 입력할 때까지 whil문 반복 
        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    print(f"최종 업데이트: {date(2024, 8, 2)}")
    login_app()
