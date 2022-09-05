from multiprocessing.connection import wait


def prinMenu():
    try:
        print("\n¿Que operación quieres realizar?\n\t1.-Suma\n\t2.-Resta\n\t3.-Multiplicación\n\t4.-Division\n\t0.-Salir\n");
        option=input("Seleccione la opción que desea: ");
        option=int(option);
        if option>4 or option<0:
            print("ERROR. No has elegido una opción correcta");
            prinMenu();
        else:
            print(f"La opción que has seleccionado es {option}");
            if option==1:
                menuSuma();
            elif option==2:
                menuResta();
            elif option==3:
                menuMultiplicar();
            elif option==4:
                menuDividir();
            elif option==0:
                print("Hasta pronto")
    except:
        print("ERROR. No has escrito un número");
        prinMenu();

def menuSuma():
    try:
        num1=float(input("Dime el primer numero a sumar: "));
        num2 = float(input("Dime el segundo numero a sumar: "));
        print(f"El resultado es {num1+num2}");
        prinMenu();
    except:
        print("ERROR. No has escrito un número");
        menuSuma();

def menuResta():
    try:
        num1 = float(input("Dime el primer numero a restar: "))
        num2 = float(input("Dime el segundo numero a restar: "))
        print(f"El resultado es {num1-num2}")
        prinMenu()
    except:
        print("ERROR. No has escrito un número")
        menuResta()

def menuMultiplicar():
    try:
        num1 = float(input("Dime el primer numero a multiplicar: "))
        num2 = float(input("Dime el segundo numero a multiplicar: "))
        print(f"El resultado es {num1*num2}")
        prinMenu();
    except:
        print("ERROR. No has escrito un número")
        menuMultiplicar()

def menuDividir():
    try:
        num1 = float(input("Dime el primer numero a dividir: "))
        num2 = float(input("Dime el segundo numero a dividir: "))
        print(f"El resultado es {num1/num2}");
        prinMenu()
    except:
        print("ERROR. No has escrito un número")
        menuDividir()

prinMenu();