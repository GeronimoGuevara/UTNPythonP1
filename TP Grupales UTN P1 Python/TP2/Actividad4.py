
def cantBilletes(precio):
    while True:
        if precio >= 200:
            cant200 = precio // 200
            precio = precio % 200
            print(cant200, "billetes de 200")
        if precio >= 100:
            cant100 = precio // 100
            precio = precio % 100
            print(cant100, "billetes de 100")
        if precio >= 50:
            cant50 = precio //50
            precio = precio % 50
            print(cant50, "billetes de 50")
        if precio >= 20:
            cant20 = precio // 20
            precio = precio % 20
            print(cant20, "billetes de 20")
        if precio >= 10:
            cant10 = precio // 10
            precio = precio % 10
            print(cant10, "billetes de 10")
        if precio >= 5:
            cant5 = precio // 5
            precio = precio % 5
            print(cant5,"billetes de 5")
        if precio >= 2:
            cant2 = precio // 2
            precio = precio % 2
            print(cant2, "billetes de 2")
        if precio >= 0.5:
            mon50 = precio // 0.5
            precio = precio % 0.5
            print(mon50, "monedas de 0.50")
        if precio >= 0.25:
            mon25 = precio // 0.25
            precio = precio % 0.25
            print(mon25, "monedas de 0.25")
        if precio >= 0.10:
            mon10 = precio // 0.10
            precio = precio % 0.10
            print(mon10, "monedas de 0.10")
        if precio >= 0.05:
            mon05 = precio // 0.05
            precio = precio % 0.05
            print(mon05,"monedas de 0.05")
        if precio < 0.04:
            break
                    
precio = float(input("Ingrese el precio del producto para ver cuantos billetes necesita: "))
cantBilletes(precio)
