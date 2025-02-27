from modules import utils

def printOptionMenu() -> None:
    """
        Print option screen for practice games
    """
    print('Select a practice game:')
    print('-------------------------------------')
    print('1: Round the World (Singles)')
    print('2: Round the World (Doubles)')
    print('3: 501')
    print('0: Quit')


def singlesRtwMenu() -> None:
    """
        Data capture menu for Round the World (Singles) practice game
    """
    today:str = utils.getTodaysDate()
    data:list[tuple[str, str, int]] = []

    target_count:int = 1
    while target_count < 21:
        try:
            target:str = f'S{target_count}'
            attempts:int = int(input(f'{target}: '))
            data.append((today, target, attempts))
            target_count += 1
        except:
            print('Invalid input. Please try again.')
            continue
    
    utils.insertMany(table='singles_rtw', fields=('event_date', 'target', 'attempts'), data=data)

if __name__ == '__main__':
    singlesRtwMenu()