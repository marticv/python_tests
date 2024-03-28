import os
import routes

def crear_archivos_txt(carpeta):
    # Verificar si la carpeta existe, si no, crearla
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    # Crear 60 archivos de texto en la carpeta especificada
    for i in range(1, 61):
        nombre_archivo = f"archivo_{i}.txt"
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f"Contenido del archivo {i}")

    print("Se han creado 60 archivos de texto en la carpeta especificada.")

# Ejemplo de uso:
crear_archivos_txt(routes.carpeta_origen)
