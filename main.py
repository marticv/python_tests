import shutil
import os
import routes

def get_file_counter(folder_path: str, extension: str = None):
    """
    Calcula el número de archivos en un directorio dado, opcionalmente filtrando por una extensión específica.

    Parámetros:
    - directorio (str): La ruta al directorio del cual se desea calcular el número de archivos.
    - extension (str): La extensión de archivo opcional para filtrar archivos. Por defecto, todos los archivos se cuentan.

    Retorna:
    - int: El número de archivos en el directorio. Retorna -1 si el directorio no existe.
    """

    #try to count the files in folder or return -1 to indicate failure
    try:
        #Check if path exists
        if not os.path.exists(folder_path):
            print(f"El directorio {folder_path} no existe.")
            return -1

        file_counter = 0

        #Get te total of files for the selected extension in the folder
        for element in os.scandir(folder_path):
            if element.is_file() and (extension is None or element.name.endswith(extension)):
                file_counter += 1

        return file_counter
    
    except Exception as e:
        print(f"Error al contar archivos: {e}")
        return -1

#Params for the script
original_folder = routes.original_folder
destiny_folder = routes.destiny_folder
maximum_files = routes.maximum_files
file_tipe= routes.file_tipe

def move_files(source:str, destination:str, max_files:int, file_tipe:str):
    """
    Mueve los archivos .log de un directorio a otro siempre que haya espacio suficiente

    Parámetros:
    - Directorios de origen i destino
    - Maximo de archivos .log permitidos en carpeta de destino

    """
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)

        archives_in_destination = get_file_counter(destination)
        correct_files_in_source = get_file_counter(source,file_tipe)
    
        while archives_in_destination < max_files and correct_files_in_source > 0:

            files = os.listdir(source)

            for file in files:
                if file.endswith('.log'):
                    source_file = os.path.join(source, file)
                    destination_file = os.path.join(destination, file)
                    if os.path.isfile(source_file):  # Solo mover si es un archivo (avitamos alguna carpeta que acabe como .log)
                        if not os.path.exists(destination_file):  # Verificar si el archivo ya existe en el destino
                            try:
                                shutil.move(source_file, destination_file)
                                print(f"Archivo {file} movido a {destination}")
                                archives_in_destination += 1
                                correct_files_in_source -= 1
                            except Exception as e:
                                print(f"Error al mover archivo {file}: {e}")
                if archives_in_destination >= 250:
                    print("carpeta de destino llena")
                    break

        print("Todos los archivos han sido movidos.")
    
    except Exception as e:
        print(f"Ha sucedido un error al mover archivos: {e}")

move_files(original_folder, destiny_folder, maximum_files, file_tipe)