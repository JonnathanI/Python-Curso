import shutil
import os

# Rutas de origen y destino
source_dir = 'C:\Users\Usuario\Documents\Curso de Python\EjerciciosD2\Os'
backup_dir = 'C:\Users\Usuario\Documents\Curso de Python\EjerciciosD2'

# Crear el directorio de destino si no existe
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Copiar archivos .log
for filename in os.listdir(source_dir):
    if filename.endswith('.log'):
        full_file_name = os.path.join(source_dir, filename)
        shutil.copy(full_file_name, backup_dir)

print("Backup completado.")
