lista = [3,8,5,10,7,4]
acumulador_par = acumulador_impar = 0

for x in range (0, len(lista)):

    if(lista[x]%2==0):
        acumulador_par += lista[x]
    else:
        acumulador_impar += lista[x]
print('Soma dos números pares : ',acumulador_par)
print('Soma dos números ímpares : ',acumulador_impar)