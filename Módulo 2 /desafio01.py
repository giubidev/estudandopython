passaporte = input('Você possui passaporte? ')
passagem = input('Você já comprou sua passagem? ')
idade = input('Qual sua idade? ')

# Uma pessoa só pode viajar se possui passaporte e tiver a passagem comprada e não for menor de idade
if passaporte == 'sim' and passagem == 'sim' and idade >= '18':
    print('Você cumpre todos os requisitos para viajar. Está autorizado para embarcar!')

else:
    print('Você não cumpre um dos requisitos para viajar!')

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
if (passaporte == 'sim' or passagem == 'sim') and idade >= '18':
   print('Você cumpre todos os requisitos para viajar. Está autorizado para embarcar!')

else:
    print('Você não cumpre um dos requisitos para viajar!')

# Uma pessoa só pode viajar se não possuir passaporte ou tiver passagem comprada e não for menor de idade
if passaporte == 'não' or passagem == 'sim' and idade >= '18':
    print('Você cumpre todos os requisitos para viajar. Está autorizado para embarcar!')

else:
    print('Você não cumpre um dos requisitos para viajar!')

# Uma pessoa não pode viajar se não possuir passaporte ou não tier a passagem comprada e for menor de idade
if passaporte == 'não' or passagem == 'não' and idade >= '18':
    print('Você não cumpre os requisitos para viajar')
