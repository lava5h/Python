import math

def square(side):

    if not isinstance(side, (int, float)):
        raise TypeError("Длина стороны должна быть числом")

    area = side * side
    return math.ceil(area) if not isinstance(area, int) else area

side1 = 4.5
area1 = square(side1)
print(f"Площадь квадрата со стороной {side1} равна {area1}")

side2 = 5
area2 = square(side2)
print(f"Площадь квадрата со стороной {side2} равна {area2}")