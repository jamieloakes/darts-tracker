import src.db_setup as db_setup
import src.menus as menus

if __name__ == '__main__':
    db_setup.setupDatabase()

    while True:
        try:
            menus.printOptionMenu()
            menu_choice:int = int(input('> '))
            print()
            match menu_choice:
                case 1:
                    menus.singlesRtwMenu()
                case 2:
                    # Round the World (Doubles)
                    pass
                case 3:
                    # 501
                    pass
                case 0:
                    # Quit
                    break
                case _:
                    # Invalid input
                    raise ValueError()
        except ValueError:
            print('Invalid option. Please try again.\n')
            continue
    