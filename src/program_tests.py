import requests
from switch import Switch
import infrastructure.state as state
import program_apartment as prog_apt
import infrastructure.util as util
invalid_address = "http://jvallee97.pythonanywhere.com/invalid" # returns a invalid json (violates our schema)
valid_address = "http://jvallee97.pythonanywhere.com" # returns a valid json


def run():
    print(' ****************** Welcome guest **************** ')
    print()

    show_commands()

    while True:
        action = util.get_action().strip().lower()
        with Switch(action) as case:
            if case('x', 'bye', 'exit', 'exit()'):
                util.exit_app()
            if case('m'):
                return
            if case('?', 'h'):
                show_commands()
            if case(''):
                pass
            if case.default:
                util.unknown_command()

        if action:
            print()


def show_commands():
    print('What action would you like to take:')
    print('[M]ain menu')
    print('e[X]it app')
    print('[?] [H]elp (displays this info)')
    print('[S]cheduler Tests (tests the Scheduler Class)')
    print()







