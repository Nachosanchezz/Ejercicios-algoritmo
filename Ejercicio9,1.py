def calculate_mean(num1, num2, num3):
    mean = (num1 + num2 + num3) / 3
    return mean

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

mean = calculate_mean(num1, num2, num3)

print("La media de los tres números es: ", mean)

