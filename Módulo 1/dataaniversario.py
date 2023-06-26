from datetime import datetime

atual = datetime.now()
aniversario = datetime.strptime(input('Digite quando é seu aniversário: '), '%d/%m/%Y')
tempo = atual - aniversario
print('Faltam {} dias para o seu aniversário'.format(tempo))
