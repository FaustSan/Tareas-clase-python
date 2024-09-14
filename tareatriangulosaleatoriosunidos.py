# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:55:41 2024

@author: faust
"""
import random
import math
import matplotlib.pyplot as plt
from matplotlib.path import Path

# Función para calcular la distancia entre dos puntos
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Función para calcular el área de un triángulo usando los vértices (x1, y1), (x2, y2), (x3, y3)
def area_triangulo(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

# Función para verificar si un punto está dentro de un triángulo
def punto_en_triangulo(px, py, ax, ay, bx, by, cx, cy):
    # Área del triángulo original
    area_total = area_triangulo(ax, ay, bx, by, cx, cy)
    
    # Áreas de los triángulos formados por el punto P y los lados del triángulo
    area1 = area_triangulo(px, py, bx, by, cx, cy)
    area2 = area_triangulo(ax, ay, px, py, cx, cy)
    area3 = area_triangulo(ax, ay, bx, by, px, py)
    
    # Si la suma de las áreas es igual al área total, el punto está dentro
    return math.isclose(area_total, area1 + area2 + area3, abs_tol=1e-6)

# Función para verificar si un punto está dentro de un polígono usando matplotlib.path.Path
def punto_en_poligono(px, py, polygon):
    path = Path(polygon)
    return path.contains_point((px, py))

# Función para generar un punto aleatorio fuera del polígono
def generar_punto_fuera(polygon, xmin=0, xmax=100, ymin=0, ymax=100):
    while True:
        px = random.randint(xmin, xmax)
        py = random.randint(ymin, ymax)
        if not punto_en_poligono(px, py, polygon):
            return px, py

# Función para generar el triángulo inicial con restricciones de distancia
def generar_triangulo_inicial():
    # Generar el primer vértice (ax, ay)
    ax = random.randint(0, 100)
    ay = random.randint(0, 100)
    
    # Asegurarnos que la distancia entre A y B sea menor o igual a 30
    while True:
        bx = random.randint(0, 100)
        by = random.randint(0, 100)
        if distancia(ax, ay, bx, by) <= 30:
            break
    
    # Asegurarnos que la distancia entre A-C sea menor o igual a 10 y B-C sea menor o igual a 30
    while True:
        cx = random.randint(0, 100)
        cy = random.randint(0, 100)
        if distancia(ax, ay, cx, cy) <= 10 and distancia(bx, by, cx, cy) <= 30:
            break
    
    return [(ax, ay), (bx, by), (cx, cy)]

# Función para encontrar los dos vértices más cercanos a un punto dado
def encontrar_dos_mas_cercanos(punto, vertices):
    px, py = punto
    distancias = []
    for v in vertices:
        dist = distancia(px, py, v[0], v[1])
        distancias.append((dist, v))
    # Ordenar las distancias
    distancias.sort(key=lambda x: x[0])
    # Retornar los dos vértices más cercanos
    return distancias[0][1], distancias[1][1]

# Función para dibujar el polígono y los triángulos
def dibujar(polygon, nuevos_triangulos, punto_p):
    plt.figure(figsize=(8, 8))
    
    # Dibujar el polígono
    x_polygon = [v[0] for v in polygon] + [polygon[0][0]]
    y_polygon = [v[1] for v in polygon] + [polygon[0][1]]
    plt.plot(x_polygon, y_polygon, 'b-', label='Polígono')
    plt.fill(x_polygon, y_polygon, 'cyan', alpha=0.2)
    
    # Dibujar los triángulos adicionales
    for idx, tri in enumerate(nuevos_triangulos):
        x_tri = [tri[0][0], tri[1][0], tri[2][0], tri[0][0]]
        y_tri = [tri[0][1], tri[1][1], tri[2][1], tri[0][1]]
        plt.plot(x_tri, y_tri, linestyle='--', label=f'Triángulo {idx+1}')
        plt.fill(x_tri, y_tri, alpha=0.2)
    
    # Dibujar el punto P si se proporciona
    if punto_p is not None:
        plt.scatter([punto_p[0]], [punto_p[1]], color='red', label='Nuevo Punto P')
    
   
    plt.show()

def main():
    # Generar el triángulo inicial
    polygon = generar_triangulo_inicial()
    print(f"Triángulo Inicial: A{polygon[0]}, B{polygon[1]}, C{polygon[2]}")
    
    # Lista para almacenar los nuevos triángulos
    nuevos_triangulos = []
    
    # Número de iteraciones que deseas realizar
    num_iteraciones = 5
    
    for i in range(num_iteraciones):
        # Generar un nuevo punto fuera del polígono actual
        px, py = generar_punto_fuera(polygon)
        print(f"\nIteración {i+1}: Nuevo Punto P({px}, {py})")
        
        # Encontrar los dos vértices más cercanos al nuevo punto
        v1, v2 = encontrar_dos_mas_cercanos((px, py), polygon)
        print(f"Vértices más cercanos: {v1} y {v2}")
        
        # Formar un nuevo triángulo con estos dos vértices y el nuevo punto
        nuevo_triangulo = [v1, v2, (px, py)]
        nuevos_triangulos.append(nuevo_triangulo)
        print(f"Nuevo Triángulo: {nuevo_triangulo}")
        
        # Actualizar el polígono para incluir el nuevo punto
        polygon.append((px, py))
        
        # Dibujar el estado actual
        dibujar(polygon, nuevos_triangulos, (px, py))
    
    # Dibujar el polígono final y todos los triángulos
    dibujar(polygon, nuevos_triangulos, None)
    
    # Imprimir los vértices finales del polígono
    print("\nVértices finales del polígono:")
    for idx, vertice in enumerate(polygon):
        print(f"V{idx+1}({vertice[0]}, {vertice[1]})")

if __name__ == "__main__":
    main()
