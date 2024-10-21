import math
import main
import seznam

def kalkulacka():
    print('1. Sčítání\n2. Odčítání\n3. Násobení\n4. Dělení\n5. Mocnina\n6. Druhá odmocnina\n7. Faktoriál\n8. Návrat do menu\n9. Ukončit program')
    vstup = int(input('Zadejte číslo: '))
    if vstup == 1:
        seznam.clear()
        scitani()
    elif vstup == 2:
        seznam.clear()
        odcitani()
    elif vstup == 3:
        seznam.clear()
        nasobeni()
    elif vstup == 4:
        seznam.clear()
        deleni()
    elif vstup == 5:
        seznam.clear()
        mocnina()
    elif vstup == 6:
        seznam.clear()
        odmocnina()
    elif vstup == 7:
        seznam.clear()
        faktorial()
    elif vstup == 8:
        seznam.clear()
        main.main()
    elif vstup == 9:
        seznam.clear()
        exit()
    else:
        print('Neplatný vstup')
        kalkulacka()

def scitani():
    cislo1 = int(input('Zadej první číslo: '))
    cislo2 = int(input('Zadej druhé číslo: '))
    print(f'Výsledek je: {cislo1 + cislo2}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()

def odcitani():
    cislo1 = int(input('Zadej první číslo: '))
    cislo2 = int(input('Zadej druhé číslo: '))
    print(f'Výsledek je: {cislo1 - cislo2}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()

def nasobeni():
    cislo1 = int(input('Zadej první číslo:'))
    cislo2 = int(input('Zadej druhé číslo:'))
    print(f'Výsledek je: {cislo1 * cislo2}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()

def deleni():
    cislo1 = int(input('Zadej první číslo:'))
    cislo2 = int(input('Zadej druhé číslo:'))
    if cislo2 == 0:
        print('Nelze dělit nulou')
    else:
        print(f'Výsledek je: {cislo1 / cislo2}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()

def mocnina():
    cislo1 = int(input('Zadej číslo:'))
    cislo2 = int(input('Zadej mocninu:'))
    print(f'Výsledek je: {math.pow(cislo1, cislo2)}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()

def odmocnina():
    cislo1 = int(input('Zadej číslo:'))
    print(f'Výsledek je: {math.sqrt(cislo1)}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()

def faktorial():
    cislo1 = int(input('Zadej číslo:'))
    print(f'Výsledek je: {math.factorial(cislo1)}')
    input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
    if input == '':
        seznam.clear()
        main.main()
    else:
        seznam.clear()
        kalkulacka()