from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, n, i, p):
        self.n = n  # nombre
        self.i = i  # ingredientes
        self.p = p  # pasos

    @abstractmethod
    def mostrar(self):
        pass


# Clase para recetas vegetarianas
class recV(receta):
    def mostrar(self):
        print(f"Receta vegetariana: {self.n}")
        print("Ingredientes:")
        for ing in self.i:
            print(f"- {ing}")
        print("Pasos:")
        for paso in self.p:
            print(f"{paso}")


# Clase para recetas no vegetarianas
class recNV(receta):
    def mostrar(self):
        print(f"Receta NO vegetariana: {self.n}")
        print("Ingredientes:")
        for ing in self.i:
            print(f"- {ing}")
        print("Pasos:")
        for paso in self.p:
            print(f"{paso}")


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(r):
        print("====================================")
        r.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for l in lista:
            print(f"* {l}")

# Función principal
def principal():
    r1 = recV("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    r2 = recNV("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(r1)
    utilidades.imprimir_receta(r2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in r1.i:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in r2.i:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    principal()
