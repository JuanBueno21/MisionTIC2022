#En vereda encantada  Gi, Ale y Nico  quieren saber cuanto pesan y utilizan la bascula del abuelo. Al quitarle cuatro kilos al peso de Gi se obtiene dos veces el peso de Ale y si sumamos los pesos de Gi y Ale se obtiene cinco veces el peso de Nico (todos los pesos son enteros). En la vereda encantada se dice que una persona está en etapa 'uno' si está entre 0 y 20 kilos, en etapa 'dos' si está entre 21 y 40 kilos, en etapa 'tres si está entre 41 y 80 kilos y en etapa 'cuatro' si está por encima de 80 kilos. Dado el peso de Ale, realizar un programa que imprima en la primera línea los pesos de Ale, Gi  y Nico separados por un solo espacio y en la segunda línea indique en qué etapa se encuentra Nico.
#Entrada:

#Un número entero que representa el peso de Ale

#Salida:
#En la primera línea tres números enteros separados por espacio que representan los pesos de Ale, Gi y Nico separados por un solo espacio. 
#En la segunda línea se debe indicar en qué etapa se encuentra Nico escrita en letras minúsculas.

peso_ale = int(input())

peso_gi = (peso_ale*2)+4
peso_nico = (peso_ale + peso_gi) // 5
print (peso_ale, ' ',peso_gi, ' ', peso_nico)
if peso_nico >= 0 and peso_nico <= 20:
        print("uno")
elif peso_nico >= 21 and peso_nico <=40:
        print("dos")
elif peso_nico >= 41 and peso_nico <80:
        print("tres")
else: 
        print("cuatro")
        