import time
print("Spaced Practice Calculator Version 0.1.0\n")

print("Please input the day of the initial read.")
print("If you just press enter, it is calculated by using today as the initial.\n")

initial = input("The initial date: ")
if initial=="":
    initial = time.time()

print("\nPlease enter your repeat schedule.")
print("If you just press enter, it would be 0, 1, 4, 7, 14, 30 days from the initial day.\n")

study_schedule = input("Your study schedule: ")
if study_schedule=="":
    study_schedule=[0, 1, 4, 7, 14, 30]

print()

for i, day in enumerate(study_schedule):
    study_day = initial + (60 * 60 * 24 * day)
    study_day = time.localtime(study_day)
    study_day = time.strftime("%Y. %m. %d. %A", study_day)
    print(f"Repeat {i+1}: {study_day}")

