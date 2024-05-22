with open ("palabra.txt", "r") as file:
    num= file.readline()
    conteo = len(num.split())
    print(conteo)