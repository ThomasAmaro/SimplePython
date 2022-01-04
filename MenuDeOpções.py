print('='*16)
print(' MENU DA JUREMA ')
print('='*16)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('='*24)
while True:
    opcao = int(input('''O que deseja fazer?
[1] - Somar
[2] - Multiplicar
[3] - Checar qual o maior número
[4] - Digitar novos números
[5] - Sair
-> '''))
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1+n2}')
        print('='*35)
        continue
    if opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1*n2}')
        print('='*35)
        continue
    if opcao == 3:
        if n1 > n2:
            print(f'O número {n1} é maior que o número {n2}!')
            print('='*35)
            continue
        elif n2 > n1:
            print(f'O número {n2} é maior que o número {n1}!')
            print('='*35)
            continue
        elif n1 == n2:
            print(f'Você digitou números iguais!')
            print('='*35)
            continue
    if opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        continue
    if opcao == 5:
        print('Até a próxima!')
        break
        