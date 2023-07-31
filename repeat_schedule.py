def get_repeat_schedule() -> list:
    print("\n복습주기를 입력해주세요.")
    print("예를 들어서, 공부한 날, 다음 날, 처음 공부하고 3일 뒤 복습하면\
 0 1 3 이라고 입력하면 됩니다.")
    print("그냥 엔터를 누르시면 복습 주기를\
 0일(처음 공부한 날), 1일, 4일, 7일, 14일, 30일로 계산합니다.")
    print("\nPlease enter your repeat schedule.")
    print("If you just press enter, it would be 0, 1, 4, 7, 14, 30 days\
 from the initial day.\n")

    study_schedule = input("복습 주기 Your study schedule: ")
    if study_schedule=="":
        study_schedule=[0, 1, 4, 7, 14, 30]
    else:
        study_schedule=list(map(int, study_schedule.split()))
        
    print()
    
    return study_schedule