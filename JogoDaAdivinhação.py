from random import randint
from time import sleep
print('-='*27)
r1 = str(input('Olá! Vamos jogar um jogo? [S/N]: ')).upper()
if r1 == 'N':
    exit('Que pena!')
elif r1 == 'S':
    print('Beleza!')
print('Me dê um momento e irei pensar em número de 0 a 10...')
n = randint(0, 10)
sleep(1.5)
r2 = int(input('Pronto! Será que você pode adivinhar o número?: '))
c = 0
c += 1
while r2 != n:
    if r2 < n:
        r2 = int(input('HAHAHA! Você errou! Tente mais alto!: '))
        c += 1
        if r2 == n:
            print(f'Parabéns! Você acertou e precisou de {c} tentativas!')
    elif r2 > n:
        r2 = int(input('HAHAHA! Você errou! Tente mais baixo!: '))
        c += 1
        if r2 == n:
            print(f'Parabéns! Você acertou e precisou de {c} tentativas!')
    elif r2 == n:
        c += 1
        print(f'Parabéns! Você acertou e precisou de {c} tentativas!')
if r2 == n and c == 0:
    c += 1
    print(f'Parabéns! Você acertou de primeira!')
print('-='*27)
