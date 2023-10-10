from cryptography.fernet import Fernet
import os

def generar_clave():
    """
    Genera una clave de cifrado y la guarda en un archivo.
    """
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)
    print("Clave generada y guardada en 'clave.key'.")

def cargar_clave():
    """
    Carga la clave de cifrado desde un archivo.
    """
    if os.path.exists("clave.key"):
        with open("clave.key", "rb") as archivo_clave:
            clave = archivo_clave.read()
        return clave
    else:
        print("La clave no existe. Genera una clave primero.")
        return None

def cifrar_archivo(nombre_archivo, clave):
    """
    Cifra un archivo utilizando la clave proporcionada.
    """
    cipher_suite = Fernet(clave)
    try:
        with open(nombre_archivo, "rb") as archivo_original:
            data = archivo_original.read()
            data_cifrado = cipher_suite.encrypt(data)
        nombre_archivo_cifrado = "cifrado_" + nombre_archivo
        with open(nombre_archivo_cifrado, "wb") as archivo_cifrado:
            archivo_cifrado.write(data_cifrado)
        print(f"Archivo '{nombre_archivo}' cifrado y guardado como '{nombre_archivo_cifrado}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")

def descifrar_archivo(nombre_archivo_cifrado, clave):
    """
    Descifra un archivo cifrado utilizando la clave proporcionada.
    """
    cipher_suite = Fernet(clave)
    try:
        with open(nombre_archivo_cifrado, "rb") as archivo_cifrado:
            data_cifrado = archivo_cifrado.read()
            data_descifrado = cipher_suite.decrypt(data_cifrado)
        nombre_archivo_descifrado = "descifrado_" + nombre_archivo_cifrado
        with open(nombre_archivo_descifrado, "wb") as archivo_descifrado:
            archivo_descifrado.write(data_descifrado)
        print(f"Archivo '{nombre_archivo_cifrado}' descifrado y guardado como '{nombre_archivo_descifrado}'.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo_cifrado}' no se encontró.")

def main():
    while True:
        print("1. Generar una clave de cifrado")
        print("2. Cifrar un archivo")
        print("3. Descifrar un archivo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1/2/3/4): ")
        
        if opcion == "1":
            generar_clave()
        elif opcion == "2":
            clave = cargar_clave()
            if clave:
                nombre_archivo = input("Ingrese la ruta del archivo a cifrar: ")
                cifrar_archivo(nombre_archivo, clave)
        elif opcion == "3":
            clave = cargar_clave()
            if clave:
                nombre_archivo_cifrado = input("Ingrese la ruta del archivo cifrado: ")
                descifrar_archivo(nombre_archivo_cifrado, clave)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()