from api_functions import *
from os_functions import *
import math


def get_scorecard_header(course_name, gender, tee):
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

        if i == 8:
            holes_string += string_spacer("IN")
            par_string += string_spacer(sum([int(hole['par']) for hole in holes[0:9]]))
            yardage_string += string_spacer(sum([int(hole['yardage']) for hole in holes[0:9]]))
            handicap_string += string_spacer("")

        elif i==(len(holes)-1):
            holes_string += string_spacer("OUT")
            par_string += string_spacer(sum([int(hole['par']) for hole in holes[9:]]))
            yardage_string += string_spacer(sum([int(hole['yardage']) for hole in holes[9:]]))
            handicap_string += string_spacer("")

            holes_string += string_spacer("TOTAL")
            par_string += string_spacer(sum([int(hole['par']) for hole in holes]))
            yardage_string += string_spacer(sum([int(hole['yardage']) for hole in holes]))
            handicap_string += string_spacer("")
        
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

def score_updater(holes, current_hole):
    while True:
    
        score = input(f"What did you score on hole {current_hole}?")
        try:
            holes[current_hole-1]["score"] = int(score)
            return holes
        except TypeError:
            print("Error: Please enter an integer")
            print()
        except Exception as e:
            print(f"other error {e}")
            print()


def main():

    search_results = display_course_choices()
    course = choose_course(search_results)
    clear_console()
    course_name, gender, tees = select_tees(course)
    clear_console()
    scorecard_header = get_scorecard_header(course_name, gender, tees)
    holes = tees['holes'].copy()
    score_string = "Score   "
    
    for i in range(1, len(holes)+ 1):
        clear_console()
        print(scorecard_header)
        print()
        print(score_string)
        holes = score_updater(holes, i)
        score_string += string_spacer(holes[i-1]['score'])

    print(score_string)

        
        


if __name__ == "__main__":
    main()