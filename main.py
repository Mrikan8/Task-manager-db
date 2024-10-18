import math
import sqlite3
import os

def create_table():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ukoly
              (id INTEGER PRIMARY KEY, name TEXT, date TEXT, description TEXT)''')
    conn.commit()
    conn.close()

def main():
    create_table()
    print('1. Nový úkol/r2. Seznam úkolů/r3. Vymazat úkoly/r4. Ukončit program')
    vstup = int(input('Zadejte číslo: '))
    if vstup == 1:
        novy_ukol()
        os.system('cls')
    elif vstup == 2:
        seznam_ukolu()
        os.system('cls')
    elif vstup == 3:
        vymazat_ukoly()
        os.system('cls')
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
    print('Úkol byl úspěšně přidán')
    main()

def seznam_ukolu():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('SELECT * FROM ukoly')
    rows = c.fetchall()
    for row in rows:
        print(f'ID: {row[0]}, Název: {row[1]}, Datum: {row[2]}, Popis: {row[3]}')
    conn.close()
    print('Seznam úkolů byl úspěšně zobrazen, chcete nějaký úkol smazat? pro ukončení stiskněte Enter')
    volba = input('Zadejte ID úkolu, který chcete smazat, pro smazání všech napiš - vse: ')
    if volba == '':
        main()
    elif volba == 'vse':
        vymazat_ukoly()
    else:
        smazat_ukol(volba)
    input()
    main()

def vymazat_ukoly():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('DELETE FROM ukoly')
    conn.commit()
    conn.close()
    main()

def smazat_ukol(id):
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('DELETE FROM ukoly WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print('Úkol byl úspěšně smazán')
    main()

if __name__ == "__main__":
    main()
