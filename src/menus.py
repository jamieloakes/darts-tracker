import sqlite3
from src import utils

def singlesRTWMenu() -> None:
    today:str = utils.getTodaysDate()
    data:list[tuple[str, str, int]] = [] 
    for i in range(1,21):
        attempts:int = int(input(f'S{i}: '))
        data.append((today, f'S{i}', attempts))

    print(data)

if __name__ == '__main__':
    singlesRTWMenu()