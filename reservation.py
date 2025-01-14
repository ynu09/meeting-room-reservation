from datetime import * 
from data import save_reservations

# 회의실 3개로 구성 
def assign_room(attendees):
    if attendees >= 10:
        return {1: '대 회의실'}
    elif attendees > 5:
        return {2: '중 회의실'}
    else:
        return {3: '소 회의실'}

# 예약
def make_reservation(reservations):
    while True:
        start_time_str = input("예약 시작 시간 (YYYY-MM-DD HH:MM): ")
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
        if start_time > datetime.now():
            break
        else:
            print("예약 시작 시간은 현재 시간 이후여야 합니다.\n")
    
    while True:
        end_time_str = input("예약 끝 시간 (YYYY-MM-DD HH:MM): ")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
        if end_time > start_time:
            break
        else:
            print("예약 끝 시간은 시작 시간 이후여야 합니다.\n")

    for res in reservations:
        res_start = datetime.strptime(res[1], "%Y-%m-%d %H:%M")
        res_end = datetime.strptime(res[2], "%Y-%m-%d %H:%M")
        if (start_time < res_end and end_time > res_start):
            print("예약 시간이 겹칩니다. 다른 시간으로 시도해 주세요.")
            return

    attendees = int(input("참석 인원: "))
    room = assign_room(attendees)

    reservations.append([list(room.keys())[0], start_time_str, end_time_str, attendees])
    print(f"[{list(room.keys())[0]}번] '{list(room.values())[0]}'이 예약되었습니다.")
    save_reservations(reservations)

# 조회
def view_reservations(reservations):
    for index, reservation in enumerate(reservations):
        print(f"예약 번호: {index + 1}, 회의실 번호: {reservation[0]}, 시작 시간: {reservation[1]}, 끝 시간: {reservation[2]}, 참석 인원: {reservation[3]}")

# 수정
def modify_reservation(reservations):
    view_reservations(reservations)
    index = int(input("수정할 예약 번호: ")) - 1
    print()
    if 0 <= index < len(reservations):
        while True:
            start_time_str = input("새 예약 시작 시간 (YYYY-MM-DD HH:MM): ")
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M")
            if start_time > datetime.now():
                break
            else:
                print("예약 시작 시간은 현재 시간 이후여야 합니다.\n")
        
        while True:
            end_time_str = input("새 예약 끝 시간 (YYYY-MM-DD HH:MM): ")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")
            if end_time > start_time:
                break
            else:
                print("예약 끝 시간은 시작 시간 이후여야 합니다.\n")

        for res in reservations:
            if res != reservations[index]:
                res_start = datetime.strptime(res[1], "%Y-%m-%d %H:%M")
                res_end = datetime.strptime(res[2], "%Y-%m-%d %H:%M")
                if (start_time < res_end and end_time > res_start):
                    print("새 예약 시간이 겹칩니다. 다른 시간으로 시도해 주세요.")
                    return
        
        attendees = int(input("새 참석 인원: "))  
        room = assign_room(attendees) # 참석 인원에 따라 자동 할당

        reservations[index] = [list(room.keys())[0], start_time_str, end_time_str, attendees]
        save_reservations(reservations)
        print("예약이 수정되었습니다.")
    else:
        print("잘못된 번호입니다.")

# 취소
def cancel_reservation(reservations):
    view_reservations(reservations)
    index = int(input("취소할 예약 번호: ")) - 1
    if 0 <= index < len(reservations):
        reservations.pop(index) # 선택한 인덱스 요소 제거
        save_reservations(reservations)
        print("예약이 취소되었습니다.")
    else:
        print("잘못된 번호입니다.")

# 연장
def extend_reservation(reservations):
    view_reservations(reservations)
    index = int(input("연장할 예약 번호: ")) - 1
    if 0 <= index < len(reservations):
        extra_time = input("연장할 시간 (분 단위): ")
        old_time = datetime.strptime(reservations[index][2], "%Y-%m-%d %H:%M") # 끝 시간에 추가 
        new_time = old_time + timedelta(minutes=int(extra_time))
        reservations[index][2] = new_time.strftime("%Y-%m-%d %H:%M")
        save_reservations(reservations)
        print("예약이 연장되었습니다.")
    else:
        print("잘못된 번호입니다.")
