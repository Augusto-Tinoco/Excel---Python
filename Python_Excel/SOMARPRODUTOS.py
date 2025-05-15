lista = [3,8,5,10,7,4]

acumulador_par = acumulador_impar = 0

for x in range (0, len(lista)):

    if(lista[x]%2==0): #Caso um item x (0,1,2,3...) da lista seja par, ele irá ser somado ao acumulador_par
        acumulador_par += lista[x]

    else:
        acumulador_impar += lista[x] #Caso contrário, ele irá ser somado ao acumulador_impar

print('Soma dos números pares : ',acumulador_par)

print('Soma dos números ímpares : ',acumulador_impar)