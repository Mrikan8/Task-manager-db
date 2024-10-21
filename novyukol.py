import main
import sqlite3
import os
import seznam

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
    seznam.clear()
    main.main()