def calculated_weighted_mean(num1, num2, num3, weight1, weight2, weight3):
    weighted_mean = (num1 * weight1 + num2 * weight2 + num3 * weight3) / (weight1 + weight2 + weight3)
    return weighted_mean

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
weight1 = float(input("Introduce el coeficiente de ponderación para el primer número: "))
weight2 = float(input("Introduce el coeficiente de ponderación para el segundo número: "))
weight3 = float(input("Introduce el coeficiente de ponderación para el tercer número: "))

weighted_mean = calculated_weighted_mean(num1, num2, num3, weight1, weight2, weight3)

print("La media ponderada de los tres números es: ", weighted_mean)

