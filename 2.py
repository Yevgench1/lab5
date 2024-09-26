import math

Ax, Ay = map(float, input("Введіть координати точки A (x, y): ").split())
Bx, By = map(float, input("Введіть координати точки B (x, y): ").split())
Cx, Cy = map(float, input("Введіть координати точки C (x, y): ").split())

def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

distance_A = distance_from_origin(Ax, Ay)
distance_B = distance_from_origin(Bx, By)
distance_C = distance_from_origin(Cx, Cy)

if distance_A <= distance_B and distance_A <= distance_C:
    print("Точка A найближча до центру координат")
elif distance_B <= distance_A and distance_B <= distance_C:
    print("Точка B найближча до центру координат")
else:
    print("Точка C найближча до центру координат")
