from api_functions import *

def display_course_choices():
    search_query = input("What is the name of the course?: ")
    search_results = search_for_course(search_query)

    list_len = 0
    if len(search_results['courses']) <= 5:
        list_len = len(search_results['courses'])
    else:
        list_len = 5

    for i in range(len(search_results['courses'])):
        try:
            print(f'{i+1}. {search_results['courses'][i]['course_name']}, {search_results['courses'][i]['location']['address']}')
        except KeyError:
            pass
def main():
    # print("Hello World")
    # print(check_api_health())
    # data = search_for_course("rancho park")
    # filename = "data.json"
    # with open(filename, 'w') as file:
    #     json.dump(data, file, indent=4)

    # print(f"JSON data saved to {filename}.")

    display_course_choices()


if __name__ == "__main__":
    main()