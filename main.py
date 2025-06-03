from api_functions import *
from os_functions import *

def display_course_choices():

    # code to limit number of results displayed
    # list_len = 0
    # if len(search_results['courses']) <= 5:
    #     list_len = len(search_results['courses'])
    # else:
    #     list_len = 5

    while True:
        search_query = input("What is the name of the course?: ")
        search_results = search_for_course(search_query)

        if search_results['courses']:
            for i in range(len(search_results['courses'])):
                try:
                    print(f'{i+1}. {search_results['courses'][i]['course_name']}, {search_results['courses'][i]['location']['address']}')
                except KeyError:
                    pass
            
            return search_results
        else:
            print(f"No courses found with name '{search_query}'. Please enter course name again.")

def choose_course(search_results):
    

    while True:
        choice = input("Please enter the number of the course you are playing: ")
        try:
            choice = int(choice)
            return search_results['courses'][choice - 1]
        except TypeError:
            print("Error: please enter a number")
        except IndexError:
            print("Error: choice not in range of the search results")

def select_tees(course):
    while True:
        print("Genders:")
        for gender in course['tees']:
                print(gender)
        gender_choice = input("Which gender tees are you playing?: ").lower()
        try:
            tee_gender = course['tees'][gender_choice]
            print()
            break
        except KeyError:
            print("Error: Enter a gender from the choices.")
        
        print()
    while True:
        print("Tees colors:")
        for tee_color in tee_gender:
            print(f"{tee_color['tee_name']}, total yards: {tee_color['total_yards']}, par total: {tee_color['par_total']}")

        print()
        tee_choice = input("Which tee color are you playing?: ").capitalize()        
        for i in range(len(tee_gender)):
            if tee_choice == tee_gender[i]["tee_name"]:
                return course["course_name"], gender_choice, tee_gender[i]
        
        print("Error: invalid tee color, please re-enter your choice")
        print()

    

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
    print(select_tees(course))
    clear_console()


if __name__ == "__main__":
    main()