def calculate_tii(price_without_taxes, vat_percentage):
    vat_value = price_without_taxes * vat_percentage / 100
    tii = price_without_taxes + vat_value
    return tii

price_without_taxes = float(input("Introduce el precio sin impuestos: "))


