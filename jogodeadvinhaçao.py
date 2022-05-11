#programa jogo de adivinhação
print('********************************')
print('Bem vindo ao Jogo de Adivinhação')
print('********************************')

from random import randint
numero = randint(1,100)
print('Eu pensei em um número entre 1 e 100.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
tentativas = 0
while not acertou:
    usuário = int(input('Qual é o número? '))
    tentativas +=1
    if usuário == numero:
        acertou = True
    else:
        if usuário < numero:
            print('O número é maior... Jogue mais uma vez.')
        elif usuário > numero:
            print('O número é menor... Jogue mais uma vez.')
print('Você acertou com {} tentativas. Parabéns!'.format(tentativas))
print('FIM DO JOGO')