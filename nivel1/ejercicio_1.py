# Ejercicio 1: Gestión de Inventario de un Almacén
# Tema: Variables, condicionales, diccionarios.
# Descripción:
# Crea un sistema básico para gestionar el stock de productos en un almacén.

# Cada producto tiene: nombre, precio unitario y cantidad en stock.

# El programa debe alertar si el stock de un producto está por debajo de 10 unidades.

# Enteros, flotantes, cadenas de texto, booleanos
# Listas, tuplas, diccionarios, sets (conjuntos)

stock = []

while True:
    product = input("Ingrese el nombre del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    qty = int(input("Ingrese la cantidad en stock: "))

    product_data = {
        'name': product,
        'price': price,
        'qty': qty
    }

    stock.append(product_data)

    done = input("¿Desea agregar otro producto? (s/n) ")
    if done == 'n':
        break

with open('stock.txt', 'w') as file:
    for product in stock:
        if product['qty'] <= 10:
            file.write(f'{product["name"]}, {product["price"]}, {product["qty"]}, ¡Alerta! Stock por debajo de 10 unidades\n')
        else:
            file.write(f"{product['name']},{product['price']},{product['qty']}\n")
