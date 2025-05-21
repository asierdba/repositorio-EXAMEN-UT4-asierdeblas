from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class Receta(ABC):
    def __init__(self, nombre, ingrediente, pasos):
        self.nombre = nombre  # nombre
        self.ingredientes = ingrediente  # ingredientes
        self.pasos = pasos  # pasos

    @abstractmethod
    def mostrar(self):
        pass


# Clase para recetas vegetarianas
class RecetasVegetarianas(Receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas no vegetarianas
class RecetasNoVegetarianas(Receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase con utilidades del restaurante
class Utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(ingredientes):
        for ingrediente in ingredientes:
            print(f"* {ingrediente}")

# Función principal
def principal():
    receta1 = RecetasVegetarianas("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta2 = RecetasNoVegetarianas("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    Utilidades.imprimir_receta(receta1)
    Utilidades.imprimir_receta(receta2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ingrediente in receta1.ingredientes:
        print(f"* {ingrediente}")
    
    print("Ingredientes de Pollo al horno:")
    for ingrediente in receta2.ingredientes:
        print(f"* {ingrediente}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
