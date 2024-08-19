# David Salamanca - Prueba Libreria Complejos Semana 1 - Ciencias Naturales y Tecnología 2024-2
import unittest
import libreriaComplejos
class TestLibreriaComplejos(unittest.TestCase):    
    def testSumaComplejos(self):
        self.assertEqual(libreriaComplejos.sumaComplejos((1, 1), (2, 2)), (3, 3))
        self.assertEqual(libreriaComplejos.sumaComplejos((1, 2), (1, 2)), (2, 4))
    def testProductoComplejos(self):
        self.assertEqual(libreriaComplejos.productoComplejos((1, 1), (2, 2)), (0, 4))
        self.assertEqual(libreriaComplejos.productoComplejos((1, 2), (1, 2)), (-3, 4))
    def testRestaComplejos(self):
        self.assertEqual(libreriaComplejos.restaComplejos((1, 1), (2, 2)), (-1, -1))
        self.assertEqual(libreriaComplejos.restaComplejos((1, 2), (1, 2)), (0, 0))
    def testDivisionComplejos(self):
        self.assertEqual(libreriaComplejos.divisionComplejos((1, 1), (2, 2)), (0.5, 0))
        self.assertEqual(libreriaComplejos.divisionComplejos((1, 2), (1, 2)), (1.0, 0))
    def testModuloComplejos(self):
        self.assertEqual(libreriaComplejos.moduloComplejos((3, 4)), 5.0)
        self.assertEqual(libreriaComplejos.moduloComplejos((6, 2)), 6.32)
    def testConjugadoComplejos(self):
        self.assertEqual(libreriaComplejos.conjugadoComplejos((3, 4)), (3, -4))
        self.assertEqual(libreriaComplejos.conjugadoComplejos((6, 2)), (6, -2))
    def testFaseComplejos(self):
        self.assertEqual(libreriaComplejos.faseComplejos((3, 4)), 0.93)
        self.assertEqual(libreriaComplejos.faseComplejos((6, 2)), 0.32)
    def testConversionPolarCartesiano(self):
        self.assertEqual(libreriaComplejos.conversionPolarCartesiano((3, 4)), (-1.96, -2.27))
        self.assertEqual(libreriaComplejos.conversionPolarCartesiano((6, 2)), (-2.5, 5.46))
    def test_conversion_cartesiano_polar(self):
        self.assertEqual(libreriaComplejos.conversionCartesianoPolar((3, 4)), (5.0, 0.93))
        self.assertEqual(libreriaComplejos.conversionCartesianoPolar((6, 2)), (6.32, 0.32))
if __name__ == '__main__':
    unittest.main()