import math
import main
import app.seznam as seznam

def bmi():
   while True:
    vaha = float(input('Zadej váhu v kg: '))
    vyska = float(input('Zadej výšku v cm: '))
    bmi = vaha / ((vyska / 100)**2)
    print(bmi)
    if bmi < 18.5:
        print('Podváha')
        volba = input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
        if volba == '':
            seznam.clear()
            main.main()
        else:
            seznam.clear()

    
    elif bmi >= 18.5 and bmi < 24.9:
        print('Normální váha')
        volba = input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
        if volba == '':
            seznam.clear()
            main.main()
        else:
            seznam.clear()

    
    elif bmi >= 24.9 and bmi < 29.9:
        print('Nadváha')
        volba = input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
        if volba == '':
            seznam.clear()
            main.main()
        else:
            seznam.clear()
            
    
    elif bmi >= 29.9:
        print('Obezita')
        volba = input('Stiskněte 1 pro návrat do kalkulačky\n nebo enter pro návrat do menu: ')
        if volba == '':
            seznam.clear()
            main.main()
            break
        else:
            seznam.clear()
    
    else:
        print('Chyba')
        seznam.clear()