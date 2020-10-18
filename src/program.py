import program_apartment
import program_tests
from data import mongo_setup
from colorama import Fore


def main():
    mongo_setup.global_init()
    print_header()

    try:
        while True:
            if find_user_intent() == 'test':
                program_tests.run()
            else:
                program_apartment.run()
    except KeyboardInterrupt:
        return


def print_header():
    reference = \
        """ 
                       foo$$$$$$$$$$$$$$$$$$$$$$
                    $$$foo$$$$$$$$$$$$$$$$$$$$$$$$o     
                 $$oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ooo         
               $$o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$oo       
            $$o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$oooo       
          $$$o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$ooo    
         $$$$$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
         $o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    
         $$$$$$$$$$$$$$$$$$$Jason$is$Great$$$$$$$$$$$$$$$$$$       
         $$$$$$$$$$$$$$$$$$$$$$$$nice$guy$to$work$with$$$$$$
         $$$$$  $$$$$$$$$$$and$a$good$listener$$$$$$  o$$$oo
         $$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   $$$0oo
          $$$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$0
            $$$o       $$$$$$$$$$$$$$$$$$$$$         $$$$
              $$$o            $$$$$$$$$$$          o$$$$
               $$$$o                             0o$$$
                $$$$o      o$$$$$$o$$$$o       oo$$$
                  $$$$$oo     $$$$o$$$$$o    o00o$
                     $$$$$ooo   $$$o$$$$$$$$$00
                       ))$$$$$$$oo $$$$$$$$$$
                                    $$$$$$$$$$$
                                     $$$$$$$$$$$
                                      $$$$$$$$$
                                       $$$$$$ """

    print(Fore.WHITE + '****************  Jason Vallee\'s Scheduler  ****************')
    print(Fore.GREEN + reference)
    print(Fore.WHITE + '*********************************************')
    print()
    print("Welcome to Jason's Pairing Scheduler!")
    print("What would you like to do?")
    print()


def find_user_intent():
    print("[t] Conduct tests")
    print("[r] Run the application\n")
    choice = input()
    if choice.strip().lower() == 'r':
        return 'run'

    return 'test'


if __name__ == '__main__':
    main()
