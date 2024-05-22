"""
with open("practica.txt", "r") as file:
    contenido= file.readlines()

    print(contenido[0:2])
    """
"""
def read_lines( num_lines):

    with open("practica.txt", "r") as file:
       
        for _ in range(num_lines):
           
            linea = file.readline() 
            print(linea)


print_lines = 3 
read_lines(print_lines)
"""




