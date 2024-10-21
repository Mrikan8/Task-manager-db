import main
import sqlite3
import os
import subprocess
from colorama import init, Fore, Style

def install_requirements():
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def clear():
    os.system('cls')

def seznam_ukolu():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ukoly')
    rows = c.fetchall()
    for row in rows:
        print(Fore.YELLOW + f'ID: {row[0]}, Název: {row[1]}, Datum: {row[2]}, Popis: {row[3]}' + Style.RESET_ALL)
    conn.close()
    print('Seznam úkolů byl úspěšně zobrazen, chcete nějaký úkol smazat? pro ukončení stiskněte Enter')
    volba = input('Zadejte ID úkolu, který chcete smazat, pro smazání všech napiš - vse: ')
    if volba == '':
        clear()
        main.main()
    elif volba == 'vse':
        vymazat_ukoly()
    else:
        smazat_ukol(volba)
    input()
    clear()
    main.main()

def vymazat_ukoly():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('DELETE FROM ukoly')
    conn.commit()
    conn.close()
    clear()
    main.main()

def smazat_ukol(id):
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('DELETE FROM ukoly WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print('Úkol byl úspěšně smazán')
    clear()
    main.main()