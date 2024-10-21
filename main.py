import sqlite3
import os
import subprocess
import app.seznam as seznam


def create_table():
    conn = sqlite3.connect('ukoly.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ukoly
              (id INTEGER PRIMARY KEY, name TEXT, date TEXT, description TEXT)''')
    conn.commit()
    conn.close()

def main():
    create_table()
    print('1. Nový úkol\n2. Seznam úkolů\n3. Vymazat úkoly\n4. Kalkulačka\n5. BMI kalkulačka\nEnter Ukončit program')
    vstup = input('Zadejte volbu: ')
    if vstup == '1':
        seznam.clear()
        import app.novyukol as novyukol
        novyukol.novy_ukol()
    elif vstup == '2':
        seznam.clear()
        seznam.seznam_ukolu()
    elif vstup == '3':
        seznam.clear()
        seznam.vymazat_ukoly()
    elif vstup == '4':
        seznam.clear()
        import app.kalkulacka as kalkulacka
        kalkulacka.kalkulacka()
    elif vstup == '5':
        seznam.clear()
        import app.bmi as bmi
        bmi.bmi()
    
    elif vstup == '':
        print('Program byl ukončen')
        exit()
   
    else:
        seznam.clear()
        print('Neplatný vstup')
        main()

if __name__ == "__main__":
    seznam.install_requirements()
    seznam.init()
    seznam.clear()
    main()
