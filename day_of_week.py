def get_day_of_week_kor(time_str) -> str:
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