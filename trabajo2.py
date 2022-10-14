def cesta(productos,cantidad,precio):
    total = 0.0
    if len(productos) != len(cantidad) != len(precio):
        return ("No se pudo hacer tu ticket de la compra")
    else:
        for ind in range(len(productos)):
            producto1 = productos[ind] + " -->" + str(cantidad[ind]) + " -->" + str(cantidad[ind]*precio[ind])

            print("RESUMEN DE COMPRA: " + producto1)
            total += (cantidad[ind] * precio[ind])

    print("TOTAL: -------------------------->"+str(total))


cesta(["helado", "carne", "pasta", "pastel"], [3, 5, 2, 3], [4.5, 7.2, 3.4, 12.5])