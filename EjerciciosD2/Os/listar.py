import os

# Define el directorio que quieres explorar (puedes cambiarlo según sea necesario)
directory = 'C:\\Users\\Usuario\\Documents\\Curso de Python\\EjerciciosD2\\Os'

# Define las extensiones de los archivos sensibles
sensitive_extensions = ['.db', '.sql', '.log', '.key','pem']

# Recorre el directorio
for root, dirs, files in os.walk(directory):
    for file in files:
        # Comprueba si el archivo tiene una extensión sensible
        if any(file.lower().endswith(ext) for ext in sensitive_extensions):
            # Imprime la ruta completa del archivo sensible
            print(os.path.join(root, file))
