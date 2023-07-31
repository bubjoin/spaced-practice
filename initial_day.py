import time
from day_of_week import get_day_of_week_kor

def get_initial_day() -> float:
    print("복습할 내용을 처음 공부한 날을 입력해주세요.")
    print("예를 들어서, 처음 공부한 날이 2023년 7월 31일이면\
 2023-07-31 이라고 입력하시면 됩니다.")
    print("그냥 엔터를 누르시면, 오늘 공부하신 걸로 가정하고 계산합니다.\n")
    print("Please input the day of the initial read.")
    print("If you just press enter, it is calculated by using today\
 as the initial.\n")
    
    initial_day = input("공부 시작일 The initial date: ")
    if initial_day == "":
        initial_day = time.time()
    else:
        initial_day = time.strptime(initial_day, "%Y-%m-%d")
        initial_day = time.mktime(initial_day)
    
    init_day_str = time.strftime("%Y-%m-%d %A", time.localtime(initial_day))
    print(f"\n공부를 시작한 날은 The initial day is {init_day_str}", end="")
    day_of_week = get_day_of_week_kor(init_day_str)
    print(f" {day_of_week}")
    
    return initial_day