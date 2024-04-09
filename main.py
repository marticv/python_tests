import shutil
import os
import routes

def calcular_numero_archivos(directorio):
    if not os.path.exists(directorio):
        print(f"El directorio {directorio} no existe.")
        return -1

    contador_archivos = 0

    for elemento in os.listdir(directorio):
        ruta_elemento = os.path.join(directorio, elemento)
        if os.path.isfile(ruta_elemento):
            contador_archivos += 1

    return contador_archivos

def calcular_logs_en_origen(directorio):
    if not os.path.exists(directorio):
        print("origen de datos incorrecto")
        return -1
    
    contador_logs = 0

    for elemento in os.listdir(directorio):
        ruta_elemento = os.path.join(directorio, elemento)
        if os.path.isfile(ruta_elemento) and elemento.endswith('.log'):
            contador_logs += 1
    return contador_logs

def mover_archivos(origen, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    num_archivos_destino = calcular_numero_archivos(destino)
    num_logs_origen = calcular_logs_en_origen(origen)
   

    while num_archivos_destino < 250 and num_logs_origen>0:

        archivos = os.listdir(origen)

        for archivo in archivos:
            if archivo.endswith('.log'):
                origen_archivo = os.path.join(origen, archivo)
                destino_archivo = os.path.join(destino, archivo)
                #if os.path.isfile(origen_archivo):  # Solo mover si es un archivo
                if not os.path.exists(destino_archivo):  # Verificar si el archivo ya existe en el destino
                    shutil.move(origen_archivo, destino_archivo)
                    print(f"Archivo {archivo} movido a {destino}")
                    num_archivos_destino += 1
                    num_logs_origen = calcular_logs_en_origen(origen)
            if num_archivos_destino >= 250:
               print("carpeta de destino llena")
               break

    print("Todos los archivos han sido movidos.")

# Especifica la carpeta de origen y la carpeta de destino
carpeta_origen = routes.carpeta_origen
carpeta_destino = routes.carpeta_destino

# Llama a la función para mover archivos
mover_archivos(carpeta_origen, carpeta_destino)