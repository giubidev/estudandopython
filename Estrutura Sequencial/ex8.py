# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês

valor = float(input("Quanto você ganha por hora: "))
hr = int(input("Qual o número de horas trabalhadas por mês: "))

salario = valor * hr
         
print("Sálario Bruto:", salario)
