# Spaced Practice Calculator Ver.0.1.0
# 2023-07-31

import time

def get_day_of_week_kor(time_str):
    day_of_week = time_str.split()[-1]
    if day_of_week == 'Sunday':
        return "일요일"
    elif day_of_week =='Monday':
        return "월요일"
    elif day_of_week =='Tuesday':
        return "화요일"
    elif day_of_week =='Wednesday':
        return "수요일"
    elif day_of_week =='Thursday':
        return "목요일"
    elif day_of_week =='Friday':
        return "금요일"
    else:
        return "토요일"

print("\n복습계획계산기 KNOU-HOW")
print("Spaced Practice Calculator Version 0.1.0\n")

print("사용방법 요약: 엔터를 두 번 누르면 오늘 공부한 것을 복습할 날짜가 나옵니다.")
print("How to use: Just press enter twice, and you will get the days to repeat\
 the work you've done today.\n")

print("복습할 내용을 처음 공부한 날을 입력해주세요.")
print("예를 들어서, 처음 공부한 날이 2023년 7월 31일이면 2023-07-31 이라고\
 입력하시면 됩니다.")
print("그냥 엔터를 누르시면, 오늘 공부하신 걸로 가정하고 계산합니다.\n")
print("Please input the day of the initial read.")
print("If you just press enter, it is calculated by using today\
 as the initial.\n")

initial = input("공부 시작일 The initial date: ")
if initial=="":
    initial = time.time()
else:
    initial = time.strptime(initial, "%Y-%m-%d")
    initial = time.mktime(initial)

initial_str = time.strftime("%Y-%m-%d %A", time.localtime(initial))
print(f"\n공부를 시작한 날은 The initial day is {initial_str}", end="")
day_of_week = get_day_of_week_kor(initial_str)
print(f" {day_of_week}")

print("\n복습주기를 입력해주세요.")
print("예를 들어서, 공부한 날, 다음 날, 처음 공부하고 3일 뒤 복습하면 0 1 3 이라고\
 입력하면 됩니다.")
print("그냥 엔터를 누르시면 복습 주기를 0일(처음 공부한 날), 1일, 4일, 7일, 14일, 30일로\
 계산합니다.")
print("\nPlease enter your repeat schedule.")
print("If you just press enter, it would be 0, 1, 4, 7, 14, 30 days\
 from the initial day.\n")

study_schedule = input("복습 주기 Your study schedule: ")
if study_schedule=="":
    study_schedule=[0, 1, 4, 7, 14, 30]
else:
    study_schedule=list(map(int, study_schedule.split()))

print()

for i, day in enumerate(study_schedule):
    study_day = initial + (60 * 60 * 24 * day)
    study_day = time.localtime(study_day)
    study_day = time.strftime("%Y-%m-%d %A", study_day)
    print(f"복습 Repeat {i+1}: {study_day}", end="")
    day_of_week = get_day_of_week_kor(study_day)
    print("\t", end="")
    print(f"{day_of_week}")
    
print(f"\n감사합니다. Thank you!\n")