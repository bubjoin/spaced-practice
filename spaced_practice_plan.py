import time
from day_of_week import get_day_of_week_kor

def put_spaced_practice_plan(initial_day, study_schedule):
    for i, day in enumerate(study_schedule):
        study_day = initial_day + (60 * 60 * 24 * day)
        study_day = time.localtime(study_day)
        study_day = time.strftime("%Y-%m-%d %A", study_day)
        print(f"복습 Repeat {i+1}: {study_day}", end="")
        day_of_week = get_day_of_week_kor(study_day)
        print("\t", end="")
        print(f"{day_of_week}")