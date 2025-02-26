import src.utils as utils 

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
    for i in range(1,21):
        attempts:int = int(input(f'S{i}: '))
        data.append((today, f'S{i}', attempts))

if __name__ == '__main__':
    singlesRtwMenu()