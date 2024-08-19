# David Salamanca - Libreria Complejos Semana 1 - Ciencias Naturales y Tecnología 2024-2
import math
def sumaComplejos(m, d):
    pReal = m[0] + d[0]
    pImg = m[1] + d[1]
    return (pReal, pImg)
def productoComplejos(m, d):
    pReal = ((m[0]*d[0])-(m[1]*d[1]))
    pImg = ((m[0]*d[1])+(d[0]*m[1]))
    return (pReal, pImg)
def restaComplejos(m, d):
    return sumaComplejos(m, (-1*d[0], -1*d[1]))
def divisionComplejos(m, d):
    pReal = ((m[0]*d[0])+(m[1]*d[1]))/(d[0]**2 + d[1]**2)
    pImg = ((d[0]*m[1])-(m[0]*d[1]))/(d[0]**2 + d[1]**2)
    return(pReal, pImg)
def moduloComplejos(m):
    return math.sqrt(m[0]**2 + m[1]**2)
def conjugadoComplejos(m):
    return (m[0], -1*m[1])
def faseComplejos(m):
    return math.atan2(m[1], m[0])
def conversionPolarCartesiano(m):
    pReal = m[0]*math.cos(m[1])
    pImg = m[0]*math.sin(m[1])
    return (pReal, pImg)
def conversionCartesianoPolar(m):
    return (moduloComplejos(m), faseComplejos(m))