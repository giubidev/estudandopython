import random #Importar

print(random.random()) # Gera um valor de 0.0 a 1.0

print(random.uniform(4, 10)) # Gera um valor decimal Valor Mín e Máx

print(random.randint(4, 10)) # Gera um valor inteiro Valor Mín e Máx

cores = ['verde', 'vermelho', 'azul']
# EScolher opção aleatória
print(random.choices(cores))
# EScolher opção aleatória e mostrar x opções
print(random.choices(cores, k=2))

cartas_de_um_baralho = ['carta1', 'carta2', 'carta3'] 
#Embaralhar listas
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)
