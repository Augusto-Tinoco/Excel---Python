lista = [3, 8, 5, 10, 7, 4]
acumulador_par = acumulador_impar =  0


for num in lista:
    if num % 2 == 0:
        acumulador_par += num
    else:
        acumulador_impar += num
print('Os números são : ',lista)
print('Soma dos números pares :', acumulador_par)
print('Soma dos números ímpares :', acumulador_impar)