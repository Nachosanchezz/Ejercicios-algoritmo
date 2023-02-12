def calculate_triangle_area(base, height):
    area = base * height / 2
    return area

a = float(input("Introduce la medida del lado a: "))
b = float(input("Introduce la medida del lado b: "))

base = max(a, b)
height = min(a, b)

area = calculate_triangle_area(base, height)    
