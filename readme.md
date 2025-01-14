## Python 첫 개인 프로젝트: 회의실 예약 시스템

### 기록

| 기간 | 내용 | 파일 |
| --- | --- | --- |
| 2024.07.29 ~ 2024.08.01 | 두산로보틱스 Rokey 부트캠프 집중반 참여 ; 수강한 Python 내용 기반 회의실 예약 시스템 구현 | main.py, login.py, reservation.py, calculate.py, data.py, login.csv, reservations.csv |

### 📁 프로젝트 구조

```python
meeting-room-reservation/
├── main.py              # 실행 파일
├── login.py             # 사용자 로그인 인증
├── reservation.py       # 회의실 예약 및 관리
├── data.py              # 예약 정보 파일 처리
├── login.csv            # 사용자 로그인 데이터
├── reservations.csv     # 회의실 예약 데이터
```

### 🎯 주요 기능

| 기능 | 설명 |
| --- | --- |
| 로그인 시스템 | login.csv 파일을 사용하여 ID와 비밀번호 비교 및 검증, 성공 또는 실패 여부를 GUI 팝업으로 알림 |
| 예약 관리 | 특정 시간에 대한 회의실 예약 → 예약 조회(정보 확인), 수정(시간/인원 변경), 취소(특정 예약 삭제), 시간 연장 기능 제공 |
| 데이터 저장 | CSV 파일로 예약 정보 저장 및 불러오기, 새로운 예약 추가 시 reservations.csv 파일 자동 업데이트 |

### 기술 스택

| 분류 | 기술 |
| --- | --- |
| 개발 환경 | Ubuntu 22.04 |
| 개발 언어 | Python |
| UI | tkinter |
| 데이터 저장소 | CSV 파일 |

### 주어진 미션 및 구상

![img1](https://github.com/user-attachments/assets/1b6a9c25-20f9-4cd2-9a8f-1fce27916174)
![img2](https://github.com/user-attachments/assets/15560088-9ae0-42e8-af71-6faffc95af87)

[구상.pdf](./구상.pdf)

### 결과물

[View PDF Document](./ynu_reservation_sys.pdf)

### 실행 영상

[![Watch the video](https://img.youtube.com/vi/Qd0D5gxUApQ/hqdefault.jpg)](https://www.youtube.com/watch?v=Qd0D5gxUApQ)

### 실행 방법

```python
python3 main.py
```
