from api_functions import *
from os_functions import *
import math


def print_scorecard(course_name, gender, tee):
    print(f"Course: {course_name}")
    print(f"Gender: {gender}, Tees: {tee['tee_name']}")
    holes = tee['holes']
    
    holes_string = "Hole    "
    par_string = "Par     "
    yardage_string = "Yards    "
    handicap_string = "Handicap"
    for i in range(len(holes)):
        
        holes_string += string_spacer(i+1)
        par_string += string_spacer(holes[i]["par"])
        yardage_string += string_spacer(holes[i]["yardage"])
        handicap_string += string_spacer(holes[i]["handicap"])

        # holes_string += f"   {i+1}   "
        # par_string += f"   {holes[i]["par"]}   "
        # yardage_string += f"  {holes[i]["yardage"]} "
        # handicap_string += f"   {holes[i]["handicap"]}   "
        
    # Instead of printing these from the function I think it would 
    # be better to return the strings so we don't have to loop 
    # through hole data everytime we print to the console 
    return f"""Course: {course_name}
Gender: {gender}, Tees: {tee['tee_name']}
{holes_string}
{par_string}
{yardage_string}
{handicap_string}"""

def string_spacer(s):
    total_len = 7
    s = str(s)
    r_space = " " * math.floor((total_len - len(s))/2)
    l_space = " " * math.ceil((total_len - len(s))/2)

    result = l_space + s + r_space
    return result

def score_updater(holes, hole):
    pass


def main():
    # print("Hello World")
    # print(check_api_health())
    # data = search_for_course("rancho park")
    # filename = "data.json"
    # with open(filename, 'w') as file:
    #     json.dump(data, file, indent=4)

    # print(f"JSON data saved to {filename}.")

    search_results = display_course_choices()
    course = choose_course(search_results)
    clear_console()
    course_name, gender, tees = select_tees(course)
    scorecard_header = print_scorecard(course_name, gender, tees)
    while True:
        clear_console()
        print(scorecard_header)
        try:
            score_update = int(input("What did you score on the hole?"))
        except TypeError:
            print()


if __name__ == "__main__":
    main()