import argparse

parser = argparse.ArgumentParser(description='Descripcion del Programa')
parser.add_argument('archivo',type=str, help='Nombre del Archivo a procesar')
parser.add_argument('--modo', choices=['lectura'])
