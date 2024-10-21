import sqlite3
import os
import subprocess
from colorama import init, Fore, Style

def install_requirements():
    subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def clear():
    os.system('cls')

def create_table():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ukoly
              (id INTEGER PRIMARY KEY, name TEXT, date TEXT, description TEXT)''')
    conn.commit()
    conn.close()

def main():
    create_table()
    print('1. Nový úkol\n2. Seznam úkolů\n3. Vymazat úkoly\n4. Ukončit program')
    vstup = int(input('Zadejte číslo: '))
    if vstup == 1:
        clear()
        novy_ukol()
    elif vstup == 2:
        clear()
        seznam_ukolu()
    elif vstup == 3:
        clear()
        vymazat_ukoly()
    elif vstup == 4:
        print('Program byl ukončen')
        exit()
    else:
        print('Neplatný vstup')
        main()

def novy_ukol():
    ukol = input('Zadej název úkolu:')
    datum = input('Zadej datum splnění:')
    text = input('Zadej popis úkolu:')
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('INSERT INTO ukoly (name, date, description) VALUES (?, ?, ?)', (ukol, datum, text))
    conn.commit()
    conn.close()
    input('Úkol byl úspěšně přidán, stiskni enter pro návrat do menu')
    clear()
    main()

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
        main()
    elif volba == 'vse':
        vymazat_ukoly()
    else:
        smazat_ukol(volba)
    input()
    clear()
    main()

def vymazat_ukoly():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('DELETE FROM ukoly')
    conn.commit()
    conn.close()
    clear()
    main()

def smazat_ukol(id):
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('DELETE FROM ukoly WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print('Úkol byl úspěšně smazán')
    clear()
    main()

if __name__ == "__main__":
    install_requirements()
    init()
    clear()
    main()
