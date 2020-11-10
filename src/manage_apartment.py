from typing import List
from switch import Switch
import infrastructure.state as state
from infrastructure.util import user_select, get_action, unknown_command, exit_app
import services.data_services as ds
import infrastructure.util as util
import sys


def run():
    print(' ****************** Manage Apartment **************** ')

    show_commands()

    while True:
        action = get_action().strip().lower()
        with Switch(action) as case:
            if case('1'):
                add_task()
            if case('2'):
                view_tasks()
            if case('3'):
                delete_tasks()
            if case('4'):
                view_occupant()
            if case('5'):
                add_occupants()
            if case('6'):
                delete_occupant()
            if case('x', 'bye', 'exit', 'exit()'):
                exit_app()
            if case('?', 'h'):
                show_commands()
            if case(''):
                pass
            if case.default:
                unknown_command()

        if action:
            print()


def show_commands():
    """
    shows the commands that the user can use while in schedule mode
    """
    print('What action would you like to take:')
    print('[1] Add a Task')
    print('[2] View the Tasks')
    print('[3] Delete Task')
    print('[4] View Occupants')
    print('[5] Add Occupant')
    print('[6] Delete Occupant')
    print('e[X]it app')
    print('[h, ?] Help (this info)')
    print()


def add_task():
    name = input("What is the name of the task you would like to add?\n")
    while True:
        is_recurring = input("is this task recurring? [y], [n]\n")
        is_recurring = is_recurring.strip().lower()
        if is_recurring == 'y':
            frequency = util.get_number_input("how long after task is completed to be completed again (in days)\n")
            break
        elif is_recurring == 'n':
            frequency = None
            break
        else:
            print("not valid response please try again")

    print("please assign an occupant to this task")
    state.reload_apartment()
    assigned, index = user_select(state.active_apartment.occupants)
    ds.add_task_to_apartment(state.active_apartment.id, name, assigned, frequency)


def view_tasks():
    state.reload_apartment()
    util.print_apartment(state.active_apartment, True)


def delete_tasks():
    state.reload_apartment()
    tasks = state.active_apartment.tasks
    tasks_name = list(map(lambda t: t.name, tasks))
    if not tasks or len(tasks) == 0:
        print("No tasks to delete")
        return
    else:
        task_name, index = user_select(tasks_name)
        task = tasks[index]
        try:
            is_success = ds.delete_task(task, state.active_apartment.id)
            if is_success:
                util.success_msg(f"Task: \"{task_name}\" successfully deleted")
                state.reload_apartment()
        except:
            util.error_msg(f"Unexpected Error occurred deleting task: {sys.exc_info()[0]}")


def view_occupant():
    occupants: List[str] = state.active_apartment.occupants
    print("The occupants are: ")
    for occupant in occupants:
        print(f" {occupant}")


def add_occupants():
    occupant_name: str = input("What is the name of the occupant you would like to add?\n    ")
    ds.add_occupant_to_apartment(occupant_name, state.active_apartment.id)
    util.success_msg("Occupant added to apartment")


def delete_occupant():
    state.reload_apartment()
    occupants = state.active_apartment.occupants
    if not occupants or len(occupants) == 0:
        print("No occupants to delete")
        return

    occupant_name, index = util.user_select(state.active_apartment.occupants)
    try:
        is_success = ds.delete_occupant(occupant_name, state.active_apartment.id)
        if is_success:
            util.success_msg(f"Task: \"{occupant_name}\" successfully deleted")
            state.reload_apartment()

    except:
        util.error_msg(f"Unexpected Error occurred deleting task: {sys.exc_info()[0]}")