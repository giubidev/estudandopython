import random
from datetime import datetime

nome_usuario = input('Digite seu nome: ')
idade_usuario = input('Digite sua idade: ')
datacadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes)
dataaniversario =  datetime.strptime(input('Digite quando é seu aniversário: '), '%d/%m/%Y')

print('Olá {}, seu registro foi concluído com sucesso no dia {}. Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {}'.format(nome_usuario, datacadastro, sorteio))


