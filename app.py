from src import db_setup, menus

if __name__ == '__main__':
    db_setup.setupDatabase()

    while True:
        try:
            menus.printMenu()
            menu_choice:int = int(input('> '))
            print()
            match menu_choice:
                case 1:
                    # Round the World (Singles)
                    pass
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
                    raise ValueError()
        except ValueError:
            print('Invalid option. Please try again.\n')
            continue
    