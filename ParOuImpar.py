from random import randint
c = randint(0, 10)
print('~'*30)
print('Vamos jogar Par ou Ímpar!')
e = str(input('Qual você quer? [PAR/IMPAR]: ')).strip().upper()
print('~'*30)
if e == 'PAR':
    print('Você escolheu PAR, eu serei ÍMPAR!')
elif e == 'IMPAR':
    print('Você escolheu ÍMPAR, eu serei PAR!')
else:
    e = str(input('Por favor, escolha uma opção correta [PAR/IMPAR]: ')).strip().upper()
j = int(input('Escolha seu número: '))
print('~'*30)  
r = j + c
v = 0
while True:
    if e == 'PAR':
        if r % 2 == 0:
            print(f'Você escolheu {j}, eu escolhi {c}, o resultado é {r}, par, você venceu!')
            print('~'*30)
            v += 1
            cont = str(input('Deseja continuar? [Y/N]: ')).strip().upper()
            print('~'*30)
            if cont == 'Y':
                c = randint(0, 10)
                e = str(input('Qual você quer? [PAR/IMPAR]: ')).strip().upper()
                print('~'*30)
                if e == 'PAR':
                    print('Você escolheu PAR, eu serei ÍMPAR!')
                elif e == 'IMPAR':
                    print('Você escolheu ÍMPAR, eu serei PAR!')
                else:
                    e = str(input('Por favor, escolha uma opção correta [PAR/IMPAR]: ')).strip().upper()
                j = int(input('Escolha seu número: '))
                print('~'*30)
                r = j + c
            elif cont == 'N':
                print('Obrigado por jogar!')
                break
            else:
                cont = str(input('Digite uma opção correta, deseja continuar? [Y/N]: '))
        else:
            print(f'Você escolheu {j}, eu escolhi {c}, o resultado é {r}, ímpar, você perdeu!')
            if v == 1:
                print('Você venceu uma vez!')
            elif v > 1:
                print(f'Você venceu {v} vezes!')
            else:
                print('Você não venceu nenhuma vez!')
            break
    if e == 'IMPAR':
        if r % 2 == 1:
            print(f'Você escolheu {j}, eu escolhi {c}, o resultado é {r}, ímpar, você venceu!')
            print('~'*30)
            v += 1
            cont = str(input('Deseja continuar? [Y/N]: ')).strip().upper()
            print('~'*30)
            if cont == 'Y':
                c = randint(0, 10)
                e = str(input('Qual você quer? [PAR/IMPAR]: ')).strip().upper()
                print('~'*30)
                if e == 'PAR':
                    print('Você escolheu PAR, eu serei ÍMPAR!')
                elif e == 'IMPAR':
                    print('Você escolheu ÍMPAR, eu serei PAR!')
                else:
                    e = str(input('Por favor, escolha uma opção correta [PAR/IMPAR]: ')).strip().upper()
                j = int(input('Escolha seu número: '))
                print('~'*30)
                r = j + c
            elif cont == 'N':
                print('Obrigado por jogar!')
                break
            else:
                cont = str(input('Digite uma opção correta, deseja continuar? [Y/N]: '))
        else:
            print(f'Você escolheu {j}, eu escolhi {c}, o resultado é {r}, par, você perdeu!')
            if v == 1:
                print('Você venceu uma vez!')
            elif v > 1:
                print(f'Você venceu {v} vezes!')
            else:
                print('Você não venceu nenhuma vez!')
            break
