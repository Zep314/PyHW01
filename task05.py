# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math
print("Введите координаты первой точки A1:")
X1 = float(input("Введите координату X1: "))
Y1 = float(input("Введите координату Y1: "))

print("Введите координаты второй точки A2:")
X2 = float(input("Введите координату X2: "))
Y2 = float(input("Введите координату Y2: "))

print(f'Расстояние между точками A1({X1};{Y1}) и A2({X2};{Y2}): {math.sqrt(math.pow(X2-X1,2)+math.pow(Y2-Y1,2)):.2f}')
