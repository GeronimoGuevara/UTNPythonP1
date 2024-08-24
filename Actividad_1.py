nombre= input("ingrese su nombre: ")
print("Bienvenido", nombre)

num1= 7
num2= 25

print("la suma entre ",num1, "y",num2,"es:",num1 + num2 )
print("la resta entre ",num1, "y",num2,"es:",num1 - num2 )
print("la multiplicacion entre ",num1, "y",num2,"da:",num1 * num2 )
print("la division entre ",num1, "y",num2,"da:",num1 / num2 )
print("el resto de la division de los numeros:",num1, "y",num2,"es:",num1 % num2 )

num3= 5
num4= 6
if num3 == num4:
    print("el numero", num3, "y el numero", num4, "son iguales")
else:
    if num3<num4:
        print("el numero mas grande es el",num4)
    else:
        print("el numero mas grande es el", num3)

num5= int(input("ingrese un numero por teclado para verificar si es divisible por 2 "))
if num5 %2 == 0:
    print("el numero SI es divisible por 2 ")
else:
    print("el numero NO es divisible por 2")

num6= float(input("ingrese un numero por teclado para calcular su precio final con IVA"))
numFinal=float(num6 + num6 * 0.21)
print("el precio final es de:", numFinal)
num7= 1
while num7< 101:
    print(num7)
    num7 = num7 + 1

for num8 in range(1,101,):
    print(num8)

for num9 in range(1,101,1):
    if num9 % 2 == 0:
        print(num9)
    else:
        if num9 % 3 == 0:
            print(num9)
            
