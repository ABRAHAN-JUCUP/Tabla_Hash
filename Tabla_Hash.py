import csv
from collections import defaultdict

class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = defaultdict(list)

    def _funcion_hash(self, clave):
        return hash(clave) % self.tamaño

    def insertar(self, clave, valor):
        indice = self._funcion_hash(clave)
        self.tabla[indice].append((clave, valor))
        print(f"Clave '{clave}' con valor '{valor}' insertada en el índice: {indice}")

    def buscar_por_clave(self, clave):
        indice = self._funcion_hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None

    def buscar_por_valor(self, valor):
        for indice in range(self.tamaño):
            for k, v in self.tabla[indice]:
                if v == valor:
                    return k
        return None

    def cargar_desde_csv(self, ruta):
        try:
            with open(ruta, mode='r') as archivo:
                lector_csv = csv.reader(archivo)
                for fila in lector_csv:
                    if len(fila) == 2:
                        clave, valor = fila
                        self.insertar(clave, valor)
            print(f"Datos cargados exitosamente desde {ruta}")
        except FileNotFoundError:
            print(f"Archivo {ruta} no encontrado. Omitiendo carga de CSV.")

def main():
    tabla_hash = TablaHash(tamaño=10)

    while True:
        print("\nMenú:")
        print("1. Insertar clave y valor")
        print("2. Buscar por clave")
        print("3. Buscar por valor")
        print("4. Cargar datos desde archivo CSV")
        print("5. Mostrar tabla hash completa")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            clave = input("Introduce la clave: ")
            valor = input("Introduce el valor: ")
            tabla_hash.insertar(clave, valor)
        elif opcion == "2":
            clave = input("Introduce la clave a buscar: ")
            resultado = tabla_hash.buscar_por_clave(clave)
            if resultado:
                print(f"Valor para la clave '{clave}': {resultado}")
            else:
                print(f"Clave '{clave}' no encontrada.")
        elif opcion == "3":
            valor = input("Introduce el valor a buscar: ")
            resultado = tabla_hash.buscar_por_valor(valor)
            if resultado:
                print(f"Clave para el valor '{valor}': {resultado}")
            else:
                print(f"Valor '{valor}' no encontrado.")
        elif opcion == "4":
            ruta_csv = input("Introduce la ruta del archivo CSV: ")
            tabla_hash.cargar_desde_csv(ruta_csv)
        elif opcion == "5":
            print("Tabla hash completa:")
            for indice, cubeta in tabla_hash.tabla.items():
                print(f"Índice {indice}: {cubeta}")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
    input("Presiona Enter para salir...")
