def handle_input_error():
    print("\n******************************************************")
    print("오류가 발생하였습니다, 입력값의 형식과 타입을 확인해주세요.")
    print("공부 시작일은 2023-07-31 같은 형식으로 입력 또는 생략합니다.")
    print("복습 주기는 0 1 4 7 14 30 60 같은 형식으로 입력 또는 생략합니다.")
    print("Please check the format and the type of the input.")
    print("The initial date would be like 2023-07-31")
    print("The repeat schedule would be like 0 1 4 7 14 30")
    print("******************************************************\n")

def handle_another_error():
    print("\n알 수 없는 오류가 발생하였습니다. 프로그램을 종료합니다.")
    print("An unknown error occur. The program will now terminate.")
    exit(1)