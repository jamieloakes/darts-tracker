import sqlite3
import utils

def singlesRTWMenu() -> None:
    today:str = utils.getTodaysDate()
    data:list[tuple[str, str, int]] = [] 
    for i in range(1,21):
        attempts:int = int(input(f'S{i}: '))
        data.append((today, f'S{i}', attempts))

if __name__ == '__main__':
    singlesRTWMenu()