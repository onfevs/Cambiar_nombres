# Script de Renombrado de Carpetas

Este script de Python permite renombrar carpetas y subcarpetas dentro de una carpeta padre. Pide al usuario ingresar un nuevo nombre y un año, y luego renombra las carpetas que contienen un guión bajo en su nombre.

## Uso

1. Ingresa la ruta de la carpeta padre que contiene las subcarpetas que deseas renombrar.
2. Ingresa el nuevo nombre y el año para las carpetas.
3. El script buscará las carpetas que contengan un guión bajo en su nombre y las renombrará usando el nuevo nombre y año proporcionados.
4. También renombrará las subcarpetas dentro de las carpetas renombradas.

**Nota:** Si en algún momento deseas salir del programa, puedes ingresar "salir" cuando se te solicite el nuevo nombre.

## Requisitos

- Python 3.x

## Créditos

Este código fue creado por @OnfeVS. Todos los derechos reservados.

## Ejemplo de Uso

```python
import os
import re

# Definición de la función para cambiar los nombres de las carpetas
def cambiar_nombres_carpetas(ruta):
    # Bucle para seguir ejecutando el programa hasta que el usuario decida salir
    while True:
        # Inicializar variables para el nombre y año
        nombre = ""
        ano = ""
        
        print("\n------------- Elige un nombre para la carpeta y el año ------------------\n")
        
        # Bucle para solicitar el nombre y año al usuario hasta que sean válidos
        while True:
            # Solicitar al usuario el nuevo nombre y año para las carpetas
            nombre = input("Ingresa el nuevo nombre (o 'salir' para salir): ")
            
            # Verificar si el usuario desea salir del programa
            if nombre.lower() == "salir":
                return
            
            ano = input("Ingresa el año: ")
            
            # Verificar si el nombre y año son válidos
            if nombre and ano.isdigit():
                break
            else:
                print("Nombre o año inválidos. Por favor, inténtalo de nuevo.")
        
        print("\n---------------------------- Renombrando carpetas ----------------------------\n")
        
        # Iterar sobre todas las carpetas en la ruta especificada
        for carpeta in os.listdir(ruta):
            ruta_carpeta = os.path.join(ruta, carpeta)
            
            # Verificar si el elemento es una carpeta y contiene un guión bajo en su nombre
            if os.path.isdir(ruta_carpeta) and "_" in carpeta:
                # Utilizar una expresión regular para dividir el nombre de la carpeta en sus componentes
                match = re.search(r'(.*)_(\d+)_(.*)', carpeta)
                if match:
                    # Construir el nuevo nombre de la carpeta utilizando el nuevo

