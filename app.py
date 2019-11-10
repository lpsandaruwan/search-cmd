import logging

from config import MODELS
from utility import initialize_query_data
from utility import search_records
from utility import validate_field_and_get_field_type
from utility import validate_model_index_and_get_model

logging.basicConfig()
logging.root.setLevel(logging.INFO)


def print_main_menu():
    print("Type 'quit' to exit at anytime, Press Enter to continue\n")
    print("        Select search options:")
    print("            * Press 1 to search Zendesk")
    print("            * Press 2 to view a list of searchable fields")
    print("            * Type 'quit' to exit\n")


def print_models_menu():
    menu_description = 'Select '
    for model in MODELS:
        menu_description = menu_description + str(model['index']) + ') ' + model['display_name'] + \
                           [lambda: '', lambda: ' or '][MODELS.index(model) + 1 < len(MODELS)]()
    print(menu_description)


def print_fields():
    for model in MODELS:
        print('-----------------------------------------------------------')
        print('Search %s with ' % model['display_name'])
        for field in model['fields']:
            print(field)
        print('\n')


def print_results_pretty(model, results):

    print('\n')


def print_quit_message():
    print('Good bye!\n')


def main():
    initialize_query_data()
    user_input = None
    while user_input != 'quit':
        print_main_menu()
        user_input = input()
        if user_input == '1':
            print_models_menu()
            user_input = input()
            if user_input == 'quit':
                print_quit_message()
                break
            validation_passed, model = validate_model_index_and_get_model(user_input)
            if validation_passed:
                print('Enter search term')
                user_input = input()
                if user_input == 'quit':
                    print_quit_message()
                    break
                field_name, field_type = validate_field_and_get_field_type(model, user_input)
                if field_name is not None and field_type is not None:
                    print('Enter search value')
                    user_input = input()
                    if user_input == 'quit':
                        print_quit_message()
                        break
                    results = search_records(field_name, field_type, user_input, model['query_db_file'])
                    print_results_pretty(model, results)
                else:
                    print('Invalid input. Select second option from main menu to get a list of searchable fields\n')
                    continue
            else:
                print('Invalid input. No such model exists for the user input\n')
                continue
        elif user_input == '2':
            print_fields()
        elif user_input == 'quit':
            print_quit_message()
        else:
            print('Invalid input. Menus are available only for the given items int the main menu\n')
            continue


if __name__ == '__main__':
    main()
