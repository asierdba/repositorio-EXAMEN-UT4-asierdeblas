from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Receta(ABC):
    def __init__(self, nombre, ingrediente, pasos):
        self.nombre = nombre  
        self.ingredientes = ingrediente 
        self.pasos = pasos 

    @abstractmethod
    def mostrar(receta):
        if isinstance(receta, RecetasVegetarianas): # Filtra el tipo de receta.
            print(f"Receta vegetariana: {receta.nombre}")
        elif isinstance(receta, RecetasNoVegetarianas): # Filtra el tipo de receta.
            print(f"Receta NO vegetariana: {receta.nombre}")
        print("Ingredientes:")
        for ingrediente in receta.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in receta.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class RecetasVegetarianas(Receta):
    def mostrar(self):
        super().mostrar() # Se accede a traves de super() a la función abstracta.

# Clase para recetas no vegetarianas
class RecetasNoVegetarianas(Receta):
    def mostrar(self):
        super().mostrar()


# Clase con utilidades del restaurante
class Utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(receta):
        print(f"Ingredientes de {receta.nombre}: ")
        for ingrediente in receta.ingredientes:
            print(f"* {ingrediente}")

    @staticmethod
    def crear_receta(eleccion):
        salir = ""
        ingredientes = []
        pasos = []
    
        nombre = input("Nombre de la receta: ")
        while salir != "s":
            ingrediente = str(input("Añade un ingrediente: "))
            ingredientes.append(ingrediente)
            salir = str(input("¿Quieres salir? (Pulsa 's'):"))
        salir = ""
        while salir != "s":
            paso = str(input("Añade un paso: "))
            pasos.append(paso)
            salir = str(input("¿Quieres salir? (Pulsa 's'): "))

        if eleccion.lower() == "vegetariana":
            receta = RecetasVegetarianas(nombre, ingredientes, pasos)
        elif eleccion.lower() == "carnivora":
            receta = RecetasNoVegetarianas(nombre, ingredientes, pasos)
        
        return receta

# Función principal
def principal():
    recetas = []

    while True:

        opcion = str(input("¿Quieres crear/imprimir/ingredientes/salir una receta?: "))
        
        match opcion.lower():

            case "crear":
                tipo_receta = str(input("¿Qué tipo de receta quieres crear? (Vegetariana / Carnivora): "))
                receta = Utilidades.crear_receta(tipo_receta)
                recetas.append(receta)

            case "imprimir":
                for receta in recetas:
                    Utilidades.imprimir_receta(receta)

            case "ingredientes":
                for receta in recetas:
                    Utilidades.mostrar_lista_ingredientes(receta)

            case "salir":
                break

            case _:
                print("Opción no válida")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
