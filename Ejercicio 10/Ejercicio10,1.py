def calculate_triangle_area(base, height):
    area = base * height / 2
    return area

base = float(input("Introduce la base del triángulo: "))
height = float(input("Introduce la altura del triángulo: "))

area = calculate_triangle_area(base, height)

print("El área del triángulo es: ", area)