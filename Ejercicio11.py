def calculate_overtime_pay(monthly_salary, overtime_hours):
    weekly_salary = monthly_salary / 12 *52 / 35
    hourly_rate = weekly_salary / 35

    if overtime_hours <= 8:
        return 0
    elif overtime_hours <= 36:
        return (overtime_hours - 8) * hourly_rate
    elif overtime_hours <= 43:
        return (36 - 8) * hourly_rate + (overtime_hours - 36) * hourly_rate * 1.25
    else: 
        return (36 - 8) * hourly_rate + (43 - 36) * hourly_rate * 1.25 + (overtime_hours - 43) * hourly_rate * 1.5
    
monthly_salary = float(input("Introduce el salario mensual: "))
overtime_hours = float(input("Introduce las horas extras: "))
result = calculate_overtime_pay(monthly_salary, overtime_hours)

print("El importe de las horas extras es: ", result)


