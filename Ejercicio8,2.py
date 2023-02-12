def calculate_interest(principal, interest_rate, time_in_months):
    interest = principal * interest_rate * time_in_months / 12 / 100
    return interest

principal = float(input("Introduce el capital: "))
interest_rate = float(input("Introduce la tasa de interés: "))
time_in_months = int(input("Introduce el tiempo en meses: "))

interest = calculate_interest(principal, interest_rate, time_in_months)
