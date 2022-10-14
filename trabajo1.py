def divide(n):
    list=[]
    list.append(n)
    if (n-1) % 2 == 1 and n>0:
        while n>1 and (n-1) % 2 ==1:
            n=n/2
            list.append(int(n))
        if list [-1]==1:
            print("Si, es potencia de dos ")
        else: print("Se puede dividir entre dos pero solo hasta este punto")
    else:
        print("no es divisibre entre dos" )
    return (list)
print(divide(64))