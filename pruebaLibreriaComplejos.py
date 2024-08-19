# David Salamanca - Prueba Libreria Complejos Semana 1 - Ciencias Naturales y Tecnología 2024-2
import libreriaComplejos
def main():
    print("\nPruebas Funciones Números Complejos:")
    # Suma Números Complejos
    print("\nSuma de (1, 1) + (2, 2):", libreriaComplejos.sumaComplejos((1, 1), (2, 2)))
    print("Suma de (1, 2) + (1, 2):", libreriaComplejos.sumaComplejos((1, 2), (1, 2)))
    # Producto Números Complejos
    print("\nProducto de (1, 1) + (2, 2):", libreriaComplejos.productoComplejos((1, 1), (2, 2)))
    print("Producto de (1, 2) + (1, 2):", libreriaComplejos.productoComplejos((1, 2), (1, 2)))
    # Resta Números Complejos
    print("\nResta de (1, 1) + (2, 2):", libreriaComplejos.restaComplejos((1, 1), (2, 2)))
    print("Resta de (1, 2) + (1, 2):", libreriaComplejos.restaComplejos((1, 2), (1, 2)))
    # División Números Complejos
    print("\nDivisión de (1, 1) + (2, 2):", libreriaComplejos.divisionComplejos((1, 1), (2, 2)))
    print("División de (1, 2) + (1, 2):", libreriaComplejos.divisionComplejos((1, 2), (1, 2)))
    # Modulo Números Complejos
    print("\nModulo de (3, 4):", libreriaComplejos.moduloComplejos((3, 4)))
    print("Modulo de (6, 2):", libreriaComplejos.moduloComplejos((6, 2)))
    # Conjugado Números Complejos
    print("\nConjugado de (3, 4):", libreriaComplejos.conjugadoComplejos((3, 4)))
    print("Conjugado de (6, 2):", libreriaComplejos.conjugadoComplejos((6, 2)))
    # Fase Radianes Números Complejos
    print("\nFase de (3,4):", libreriaComplejos.faseComplejos((3, 4)))
    print("Fase de (6,2):", libreriaComplejos.faseComplejos((6, 2)))
    # Conversión Polar Cartesiano
    print("\nConversión Polar a Cartesiano de (3, 4):", libreriaComplejos.conversionPolarCartesiano((3, 4)))
    print("Conversión Polar a Cartesiano de (6, 2):", libreriaComplejos.conversionPolarCartesiano((6, 2)))
    # Conversión Cartesiano Polar
    print("\nConversión Cartesiano a Polar de (3, 4):", libreriaComplejos.conversionCartesianoPolar((3, 4)))
    print("Conversión Cartesiano a Polar de (6, 2):", libreriaComplejos.conversionCartesianoPolar((6, 2)), "\n")
main()