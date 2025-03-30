# Ejercicio 2: Calculadora de Nóminas para Empleados
# Tema: Operadores, funciones, bucles.
# Descripción:
# Crea una función que calcule el salario mensual de un empleado, considerando:

# Horas trabajadas.

# Salario por hora (USD 12.5).

# Horas extras (pagadas al 150% si trabaja más de 40 horas).

empleados = [

]

for empleado in range(0,5):
    nombre_empleado = input('Ingresa el nombre del empleado: ')
    horas_trabajadas = int(input('Ingresa las horas trabajadas: '))

    empleado_data = {
        'nombre': nombre_empleado,
        'horas': horas_trabajadas
    }

    empleados.append(empleado_data)

with open('empleados.txt','w') as archivo:
    for empleado in empleados:
        salario_h = 12.5
        incremento = 1

        if empleado['horas'] > 40:
            incremento = 2.5
        
        costo_h = (salario_h * empleado['horas']) * incremento

        archivo.write(f"{empleado['nombre']}, {empleado['horas']}, {incremento}, {costo_h}")