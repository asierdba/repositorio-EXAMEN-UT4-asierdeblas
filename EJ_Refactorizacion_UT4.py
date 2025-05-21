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

# Función principal
def principal():
    receta1 = RecetasVegetarianas("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta2 = RecetasNoVegetarianas("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    print("== Mostrar recetas ==")
    Utilidades.imprimir_receta(receta1)
    Utilidades.imprimir_receta(receta2)

    Utilidades.mostrar_lista_ingredientes(receta1)
    Utilidades.mostrar_lista_ingredientes(receta2)


# Ejecutar el programa
if __name__ == "__main__":
    principal()
