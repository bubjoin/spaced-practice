# Spaced Practice Calculator Ver.0.1.0
# 2023-07-31

from help import intro, outro
from initial_day import get_initial_day
from repeat_schedule import get_repeat_schedule
from spaced_practice_plan import put_spaced_practice_plan
from exception_handling import handle_input_error, handle_another_error

if __name__=="__main__":
    
    intro()

    while(1):
        try:
            initial_day = get_initial_day()
            repeat_schedule = get_repeat_schedule()

            put_spaced_practice_plan(initial_day, repeat_schedule)
    
            end=outro()
            if end==0:
                break
    
        except ValueError:
            handle_input_error()

        except:
            handle_another_error()
