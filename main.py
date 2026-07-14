def calcular_total(precio, cantidad):
    descuento = 0.10
    total = precio * cantidad
    total = total - (total * descuento)
    return total

resultado = calcular_total(50, 3)

print(resultado)