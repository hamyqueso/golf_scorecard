from api_functions import *
from os_functions import *


def print_scorecard(course_name, gender, tee):
    print(f"Course: {course_name}")
    print(f"Gender: {gender}, Tees: {tee['tee_name']}")
    holes = tee['holes']
    
    holes_string = "Hole "
    par_string = "Par  "
    yardage_string = "Yards "
    handicap_string = "Handicap"
    for i in range(len(holes)):
        holes_string += f"   {i+1}   "
        par_string += f"   {holes[i]["par"]}   "
        yardage_string += f"  {holes[i]["yardage"]} "
        handicap_string += f"   {holes[i]["handicap"]}   "
        
    # Instead of printing these from the function I think it would 
    # be better to return the strings so we don't have to loop 
    # through hole data everytime we print to the console 
    print(holes_string)
    print(par_string)
    print(yardage_string)
    print(handicap_string)

    

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
    while True:
        clear_console()
        print_scorecard(course_name, gender, tees)
        score_update = input("What did you score on the hole?")


if __name__ == "__main__":
    main()