# 1- Número positivo, negativo o cero

eleccion = int(input("Ingrese un numero: "))
if eleccion < 0:
    print("El numero es negativo.")
elif eleccion > 0:
    print("El numero es positivo.")
else:
    print("El numero es cero.")


# 2- Número par o impar

numero = int(input("Ingrese un numero entero: "))
if numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")

# 3- Mayor de edad

edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

# 4- Múltiplo de 5

numero = int(input("Ingrese un numero: "))
if numero % 5 == 0:
    print(f"{numero} es múltiplo de 5")
else:
    print(f"{numero} no es múltiplo de 5")

# 5- Descuento por edad

edad = int(input("Ingrese su edad: "))
if edad >= 60:
    print("Usted Aplica para el descuento")
else:
    print("Usted No Aplica para el descuento")

# 6- Calificación aprobatoria

calif = int(input("Ingrese su calificacion (0-100): "))
if calif >= 60:
    print("Aprobado")
else:
    print("Reprobado")

# 7- Día de la semana

eleccion = input("1- Calendario normal, 2- Calendario (Adventista): ")
dia = int(input("Ingrese un numero (1-7): "))

if eleccion == "1":
    if dia == 1:
        print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miércoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sábado")
    elif dia == 7:
        print("Domingo")
    else:
        print("Día inválido")

elif eleccion == "2":
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Lunes")
    elif dia == 3:
        print("Martes")
    elif dia == 4:
        print("Miércoles")
    elif dia == 5:
        print("Jueves")
    elif dia == 6:
        print("Viernes")
    elif dia == 7:
        print("Sábado")
    else:
        print("Día inválido")

# 8- Número mayor entre dos

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if numero_1 > numero_2:
    print(f"El numero mayor es: {numero_1}")
elif numero_2 > numero_1:
    print(f"El numero mayor es: {numero_2}")
else:
    print("Los numeros son iguales.")

# 9- Mayor entre tres números

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

if num_1 >= num_2 and num_1 >= num_3:
    print(f"El numero mayor es: {num_1}")
elif num_2 >= num_1 and num_2 >= num_3:
    print(f"El numero mayor es: {num_2}")
else:
    print(f"El numero mayor es: {num_3}")

# 10- Clasificación de ángulos

angulo = int(input("Ingrese el el valor del angulo en grados: "))

if angulo < 90:
    print("El angulo es agudo.")
elif angulo == 90:
    print("El angulo es recto.")
elif angulo < 180:
    print("El angulo es obtuso.")
elif angulo == 180:
    print("El angulo es llano.")

# 11- Cálculo de impuestos

salario = int(input("Ingrese su salario mensual: "))
if salario < 10000:
    print(f"Impuesto: 0%, Salario: {salario}")

elif salario >= 10000 and salario < 30000:
    impuesto = salario * 0.1
    salario_neto = salario - impuesto
    print(f"Impuesto: 10%, Salario: {salario_neto}")
elif salario >= 30000:
    impuesto = salario * 0.2
    salario_neto = salario - impuesto
    print(f"Impuesto: 20%, Salario: {salario_neto}")

# 12- Clasificación de números

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

if num_1 > 0 and num_2 > 0 and num_3 > 0:
    print("Los tres numeros son positivos.")
elif num_1 < 0 and num_2 < 0 and num_3 < 0:
    print("Los tres numeros son negativos.")
    print("Los numeros son mixtos.")
elif num_1 < 0 or num_2 < 0 or num_3 < 0 or num_1 > 0 or num_2 > 0 or num_3 > 0:
    print("Los numeros son mixtos.")
elif num_1 == 0 or num_2 == 0 or num_3 == 0:
    print("Al menos uno de los numeros es cero.")

# 13- Verificación de año bisiesto

año = int(input("Ingrese un año: "))
if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

# 14- Conversión de calificaciones

nota = int(input("Ingresa la Calificacion (0-100): "))
estado = "Aprobado" if nota >= 70 else "Reprobado"

if nota >= 90:
    letra = "A"

elif nota >= 80:
    letra = "B"   

elif nota >= 70:
    letra = "C"

else:
    letra = "F"
    
print(nota, letra, estado)

# 15- Comparación de tres longitudes

angulo_1 = int(input("Ingrese el valor del primer angulo en grados: "))
angulo_2 = int(input("Ingrese el valor del segundo angulo en grados: "))
angulo_3 = int(input("Ingrese el valor del tercer angulo en grados: "))

if angulo_1 + angulo_2 > angulo_3 or angulo_1 + angulo_3 > angulo_2 or angulo_2 + angulo_3 > angulo_1:
    print("Los angulos pueden formar un triangulo.")
else:
    print("Los angulos no pueden formar un triangulo.")

# 16- Calculadora de descuentos

precio = float(input("Ingrese el precio del producto: "))
if precio < 50:
    print(f"Descuento: 0%, Precio final: {precio}")
elif precio >= 50 and precio < 100:
    descuento = precio * 0.05
    precio_final = precio - descuento
    print(f"Descuento: 5%, Precio final: {precio_final}")
else:
    descuento = precio * 0.1
    precio_final = precio - descuento
    print(f"Descuento: 10%, Precio final: {precio_final}")

# 17- Tipo de triángulo

lado_1 = float(input("Ingrese la longitud del primer lado: "))
lado_2 = float(input("Ingrese la longitud del segundo lado: "))
lado_3 = float(input("Ingrese la longitud del tercer lado: "))
if lado_1 == lado_2 == lado_3:
    print("El triangulo es equilatero.")
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    print("El triangulo es isosceles.")
else:
    print("El triangulo es escaleno.")

# 18- Evaluación de temperatura

temp = float(input("Ingrese la temperatura en grados Celsius: "))
if temp < 0:
    print("Hace mucho frío")
elif temp >= 0 and temp <= 20:
    print("Clima fresco")
elif temp >= 21 and temp < 30:
    print("Clima agradable")
else:
    print("Hace mucho calor")

# 19- Conversión de horas a turnos

hora = int(input("Ingrese la hora (0-23): "))
if hora >= 0 and hora <= 5:
    print("Es de madrugada")
elif hora >= 6 and hora <= 11:
    print("Es de mañana")
elif hora >= 12 and hora <= 17:
    print("Es de tarde")
else:
    print("Es de noche")

# 20- Clasificación del IMC

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
IMC = (peso / altura ** 2)
if IMC < 18.5:
    print("Bajo peso.")
elif IMC >= 18.5 and IMC < 24.9:
    print("Normal.")
elif IMC >= 25 and IMC < 29.9:
    print("Sobrepeso.")
else:
    print("Obesidad.")


"""
Nombre: Esmerlin Marchena De la rosa
Matricula: 2025-0281
"""

