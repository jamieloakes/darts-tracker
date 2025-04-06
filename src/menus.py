import uuid

import src.utils as utils
import src.database as database

def printOptionMenu() -> None:
    """ Display option screen for practice games """
    print('Select a practice game:')
    print('-------------------------------------')
    print('1: Round the World (Singles)')
    print('2: Round the World (Doubles)')
    print('3: 501')
    print('4: Report')
    print('0: Quit')


def singlesRtwMenu() -> None:
    """ Data capture menu for Round the World (Singles) practice game """
    today:str = utils.getTodaysDate()
    data:list[tuple[str, str, str, int]] = []
    game_id:str = str(uuid.uuid4)

    target_count:int = 1
    while target_count < 21:
        try:
            target:str = f'S{target_count}'
            attempts:int = int(input(f'{target}: ')); assert attempts > 0
            data.append((game_id, today, target, attempts))
            target_count += 1
        except ValueError:
            print('Invalid input. Please try again.')
        except AssertionError:
            print('Value must be greater than 0')
        except KeyboardInterrupt:
            break
    database.insertRecords(table='singles_rtw', fields=('game_id', 'event_date', 'target', 'attempts'), data=data)
    print()


def doublesRtwMenu() -> None:
    """ Data capture menu for Round the World (Doubles) practice game """
    today:str = utils.getTodaysDate()
    data:list[tuple[str, str, str, int]] = []
    game_id:str = str(uuid.uuid4)

    target_count:int = 1
    while target_count < 21:
        try:
            target:str = f'D{target_count}'
            hits:int = int(input(f'{target}: ')); assert -1 < hits < 4
            data.append((game_id, today, target, hits))
            target_count += 1
        except ValueError:
            print('Invalid input. Please try again.')
        except AssertionError:
            print('Value must be between 0 and 3')
        except KeyboardInterrupt:
            break
    database.insertRecords(table='doubles_rtw', fields=('game_id', 'event_date', 'target', 'hits'), data=data)
    print()


def legsStatsMenu() -> None:
    """ Data capture menu for 501 practice game """
    today:str = utils.getTodaysDate()
    data:list[tuple[str, int, float, int, int]] = []

    completed:bool = False
    while completed == False:
        try:
            n_darts:int = int(input('n_darts: '))
            avg:float = float(input('avg: '))
            checkout_attempts:int = int(input('checkout_attempts: '))
            win:int = int(input('win: ')); assert -1 < win < 2
            data.append((today, n_darts, avg, checkout_attempts, win))
            completed = True
        except ValueError:
            print('Invalid input. Please try again.')
        except AssertionError:
            print('Win field must be 0 (Loss) or 1 (Win)')
        except KeyboardInterrupt:
            break
    database.insertRecords(table='legs_stats', fields=('event_date', 'n_darts', 'avg', 'checkout_attempts', 'win'), data=data)
    print()
