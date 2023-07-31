# Spaced Practice Calculator Ver.0.1.0
# 2023-07-31

from initial_day import get_initial_day
from repeat_schedule import get_repeat_schedule
from spaced_practice_plan import put_spaced_practice_plan

if __name__=="__main__":
    initial_day = get_initial_day()
    repeat_schedule = get_repeat_schedule()
    put_spaced_practice_plan(initial_day, repeat_schedule)
    print(f"\n감사합니다. Thank you!\n")