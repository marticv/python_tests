import shutil
import os
import time
import routes

def calcular_numero_archivos(directorio):
    # Verificar si el directorio existe
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe.")
        return -1

    # Inicializamos el contador de archivos
    contador_archivos = 0

    # Iteramos sobre llos archivos del directorio
    for elemento in os.listdir(directorio):
        ruta_elemento = os.path.join(directorio, elemento)
        # Verificar si el elemento es un archivo
        if os.path.isfile(ruta_elemento):
            contador_archivos += 1
    print("numero de archivos = "+str(contador_archivos))

    return contador_archivos

def mover_archivos(origen, destino):
    # Verificamos si la carpeta destino existe o sino la creamos
    if not os.path.exists(destino):
        os.makedirs(destino)    

    archivos_iniciales = calcular_numero_archivos(origen)

    while archivos_iniciales > 0:

        # Obtenemos lista de ficheros en directorio
        archivos = os.listdir(origen)

        # Movemos la el archivo al destino siempre que haya menos de 50 archivos en destino para que no colapse
        for archivo in archivos:
            if calcular_numero_archivos(destino)<50:
                #transformamos a path para ver si es archivo y si lo es lo movemos
                origen_archivo = os.path.join(origen, archivo)

                if os.path.isfile(origen_archivo):
                    destino_archivo = os.path.join(destino, archivo)
                    shutil.move(origen_archivo, destino_archivo)
                    print(f"Archivo {archivo} movido a {destino}")
            else:
                print(f"limite de archivos en {destino}")
                time.sleep(5)
        archivos_iniciales = calcular_numero_archivos(origen)

    print("todos los archivos pasados")


# Especifica la carpeta de origen y la carpeta de destino
carpeta_origen = routes.original_folder
carpeta_destino = routes.destiny_folder


# Llama a la función para mover archivos
mover_archivos(carpeta_origen, carpeta_destino)