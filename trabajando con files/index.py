import os
'''Automatizar el nombrado de archivos:en una carpeta, se insertan archivos y se renombran automaticamente.'''

# Prefijo para renombrar los archivos
prefijo = "new_"

# Ruta del directorio sel script index.py (ubicacion actual)
ruta_del_script = os.getcwd() 

# Obdtenre la ruta del folder que contiene los files a renombrar.
carpeta_path = ruta_del_script+ '\\trabajando con files\carpeta_rename\\'


# Obtener la lista de los nombres de las files a renombrar de la carpeta que las contiene.
list_files = os.listdir(carpeta_path)

# iterar entre los nombres de los files de la carpeta, para optener cada nombre.
for file_name in list_files:
    # Obtener ruta completa de cada file.
    ruta_del_file = os.path.join(carpeta_path, file_name)

    print(f"ruta del file: {ruta_del_file}")
    
    # Validar si es un archivo y que sea distinto del script index.py.
    if os.path.isfile(ruta_del_file) and file_name != 'index.py':

        # Renombrar los files
        new_file = prefijo + file_name
        #Obtener 
        new_path_file = os.path.join(carpeta_path, new_file)

        # Renombramos el file con la ruta completa.
        os.rename(ruta_del_file, new_path_file)
print('END')