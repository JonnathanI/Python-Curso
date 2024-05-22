import random

def guess_the_number():
    numero= random.randint(1,50)
    intentos=0

    while True:
        intentos += 1
        try:
            juego= int(input("Adivina el Numero"))
            if juego<1 or juego>50:
                print("Ingrese un numero entre 1 y 50")
            else:
                if juego < numero:
                    print("El Numero es demaciado Bajo")
                elif juego > numero:
                    print("El Numero es Demaciado Alto")
                else:
                    print("Adivinaste el Numero")

                    break
            except ValueError:
                 print("Error no es el numero")
            
            guess_the_number()
