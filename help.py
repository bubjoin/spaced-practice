def intro():
   print("\n복습계획계산기 KNOU-HOW")
   print("Spaced Practice Calculator Version 0.1.0\n")
    
   print("사용방법 요약: 엔터를 두 번 누르면\
 오늘 공부한 것을 복습할 날짜가 나옵니다.")
   print("How to use: Just press enter twice, and you will get the days\
 to repeat the work you've done today.\n")
    
def outro() -> int:
   print(f"\n감사합니다. Thank you!\n")
   print("Q 또는 q 를 입력하신 후 엔터를 누르시면 종료합니다.")
   print("If you input Q or q and press enter, it will quit.")
   end = input()
   if end.lower()=='q':
      print()
      return 0
   else:
      print()
      return 1