import csv

# 예약 정보 데이터 불러오기 
def load_reservations():
    reservations = []
    with open('reservations.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) # 첫 행 건너뛰기 
        for row in reader:
            reservations.append(row)
    return reservations

# 예약 정보 저장 
def save_reservations(reservations):
    with open('reservations.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["room", "start time", "end time", "attendees"]) # 헤더
        writer.writerows(reservations) 
