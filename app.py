import src.database as database
import src.menus as menus

if __name__ == '__main__':
    database.setupDatabase()

    while True:
        try:
            menus.printOptionMenu()
            menu_choice:int = int(input('> '))
            print()
            match menu_choice:
                case 1:
                    menus.singlesRtwMenu()
                case 2:
                    menus.doublesRtwMenu()
                case 3:
                    menus.legsStatsMenu()
                case 0:
                    break
                case _:
                    # If input is numeric but not valid option, raise ValueError
                    raise ValueError()
        except ValueError:
            print('Invalid option. Please try again.\n')
            continue
    