import os
import re

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
                    # Construir el nuevo nombre de la carpeta utilizando el nuevo nombre y año especificados por el usuario
                    nuevo_nombre = f"{nombre}_{ano}_{match.group(3)}"
                    nueva_ruta_carpeta = os.path.join(ruta, nuevo_nombre)
                    
                    # Verificar si el nuevo nombre es diferente al nombre actual de la carpeta
                    if carpeta != nuevo_nombre:
                        # Renombrar la carpeta
                        os.rename(ruta_carpeta, nueva_ruta_carpeta)
                        print(f"Carpeta {carpeta} renombrada a {nuevo_nombre}")
                        
                        # Cambiar el nombre de las subcarpetas
                        for subcarpeta in os.listdir(nueva_ruta_carpeta):
                            ruta_subcarpeta = os.path.join(nueva_ruta_carpeta, subcarpeta)
                            if os.path.isdir(ruta_subcarpeta):
                                nueva_ruta_subcarpeta = os.path.join(nueva_ruta_carpeta, subcarpeta.replace(carpeta, nuevo_nombre))
                                os.rename(ruta_subcarpeta, nueva_ruta_subcarpeta)
                                print(f"Subcarpeta {subcarpeta} renombrada a {subcarpeta.replace(carpeta, nuevo_nombre)}")
        
        print("\n¡Renombrado de carpetas completo!\n")

print("\n----------- Ingrese la ruta de la carpeta que desea renombrar ----------\n")
# Solicitar al usuario la ruta de la carpeta que contiene las subcarpetas
ruta_carpeta_padre = input("Ingresa la ruta de la carpeta padre: ")

# Llamar a la función para cambiar los nombres de las carpetas
cambiar_nombres_carpetas(ruta_carpeta_padre)



