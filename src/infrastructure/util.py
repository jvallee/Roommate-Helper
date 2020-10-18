from typing import List
from colorama import Fore
from data.apartments import Apartment
from data.tasks import Task
from infrastructure import state


def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)


def get_number_input(message, max_input=1000):
    while True:
        try:
            int_input = int(input(message))
            if int_input > max_input:
                print("you have selected too large a number and are breaking fire code laws")
            else:
                return int_input

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def print_apartment(apartment: Apartment, show_all_info=False):
    if not show_all_info:
        print(f"\n{apartment.apartmentName} with {len(apartment.occupants)} "
              f"occupants and {len(apartment.tasks)} tasks")

    else:
        occupants= apartment.occupants
        print(f"\n Apartment: {apartment.apartmentName}")

        print("    occupants: ", *occupants)
        if apartment.tasks:
            print(f"    Tasks: ")
            for task in apartment.tasks:
                print_task(task)
        else:
            print("no tasks")
            print(f"{apartment.tasks}")


def print_task(task: Task):
    if not task:
        print("     Sorry no tasks to show")
        return
    if not task.nextDue:
        print(f"            task: {task.name}")

    else:
        print(
            f"      Task: {task.name} Last Completed: {task.lastCompleted} "
            f"Due by: {task.nextDue} Assigned to: {task.assignedTo}")


def print_apartments(apartments: List[Apartment]):
    if not apartments:
        print("Sorry no apartments to print")
        return
    print("Your apartments are")
    for apartment in apartments:
        print_apartment(apartment, False)


def user_select(items: List[str]):
    if not items:
        error_msg("No item to select, internal error")

    for i, item in enumerate(items):
        print(f"Select [{i + 1}] for {item}")

    while True:
        index = get_number_input("")
        if index < 1 or index > len(items):
            print("out of range please select again")
        else:
            return items[index - 1], index - 1


def unknown_command():
    print("Sorry we didn't understand that command. For a list of commands press [?] or [h]")


def get_action():
    """
    prompts for user input that will be used to map to an action
    @return:
    """
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def exit_app():
    """
    Ends the application
    """
    print()
    print('Good Bye! Hope you enjoyed your visit!')
    raise KeyboardInterrupt()
