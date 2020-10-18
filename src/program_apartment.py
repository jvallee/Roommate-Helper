from typing import List
from switch import Switch
import infrastructure.state as state
import manage_apartment as ma
import services.data_services as svc
import infrastructure.util as util
from data.apartments import Apartment


def run():
    print(' ****************** Hello and Welcome! **************** ')
    print()

    while state.active_account is None:
        not_logged_in()

    show_commands()

    while True:
        action = util.get_action().strip().lower()
        with Switch(action) as case:
            if case('m'):
                return
            if case('a'):
                manage_apartment()
            if case('c'):
                create_apartment()
            if case('v'):
                view_apartments()
            if case('x', 'bye', 'exit', 'exit()'):
                util.exit_app()
            if case('?', 'h'):
                show_commands()
            if case(''):
                pass
            if case.default:
                util.unknown_command()

        if action:
            print()


def not_logged_in():
    while True:
        print("Welcome! To move along further we require you to be logged in.")
        selection = input("Select [1] To create an account\nSelect [2] to log into an existing account\n")
        try:
            if selection == "1":
                create_account()
                break
            elif selection == "2":
                log_into_account()
                break
            else:
                print("Sorry we didn't understand that command.")
        except KeyboardInterrupt:
            action = input("Would you like to [q]uit the application?")
            if action.strip().lower() == "q":
                raise KeyboardInterrupt


def show_commands():
    """
    shows the commands that the user can use while in schedule mode
    """
    print('What action would you like to take:')
    print('[C]reate an apartment')
    print('Manage [A]partment')
    print('Change [M]ode (test)')
    print('[V]iew Apartments')
    print('e[X]it app')
    print('[h, ?] Help (this info)')
    print()


def create_account():
    """
    will create an account in our database using the name and email from the inputs
    """
    print(' ****************** REGISTER **************** ')
    name = input("What is your name?\n  ")
    email = input("What is your email?\n  ")
    old_account = svc.find_account_by_email(email)
    if old_account:
        util.error_msg(f"ERROR: the email {email} already associated with an account")
        return

    while True:
        password1 = input("What is your password?\n  ")
        password2 = input("Confirm your password?\n  ")
        if password1 != password2:
            print("passwords do not match, please try again")
        else:
            break
    state.active_account = svc.create_account(name, email, password1)
    util.success_msg(f"Created New Account with id {state.active_account}")


def log_into_account():
    """
    will prompt the user for an email then create an account with that email
    """
    print(' ****************** LOGIN **************** ')
    email = input("What is your email?\n    ").strip().lower()
    password = input("What is your password?\n    ").strip().lower()
    account = svc.find_account_by_email(email)

    if not account or password != account.password:
        util.error_msg("No account found matching this email or incorrect password, to exit login press \"ctrl-c\"")
        log_into_account()
        return
    state.active_account = account
    util.success_msg("Successfully logged in")


def create_apartment():
    print("Welcome, let's start making your apartment")
    apartment_name = input("What is the name of the apartment\n    ")
    number_occupants = util.get_number_input("How many people live in the apartment?\n")
    occupants = [f"{state.active_account.name}"] * number_occupants
    for i in range(0, number_occupants):
        occupant = input(f'What is the {i + 1}th occupants name?')
        occupants[i] = occupant

    account = svc.find_account_by_email(state.active_account.email)
    apartment = svc.create_apartment(apartment_name, occupants, account)

    state.reload_account()
    return apartment


def view_apartments():
    state.reload_account()
    apartments = svc.get_user_apartments(state.active_account)
    util.print_apartments(apartments)


def manage_apartment():
    print("What apartment would you like to manage")
    state.reload_account()
    apartments: List[Apartment] = svc.get_user_apartments(state.active_account)
    select, index = util.user_select(list(map(lambda x: x.apartmentName, apartments)))
    state.active_apartment = apartments[index]
    ma.run()
