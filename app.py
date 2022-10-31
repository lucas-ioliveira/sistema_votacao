# Sistema de votação
import os
from time import sleep

total_bolsonaro = 0
total_lula = 0

while True:
    print('*' * 20)
    print(f'Total Bolsonaro: {total_bolsonaro}')
    print(f'Total Lula: {total_lula}')

    print('''
    Para quem deseja votar?
    [13] - Lula
    [22] - Bolsonaro
    [555] - Sair
    ''')
    voto = int(input('Digite seu voto: '))
    print('Processando...')
    sleep(2)
    try:
        if voto == 13:
            total_lula += 1
        elif voto == 22:
            total_bolsonaro += 1
        elif voto == 555:
            print(f'Bolsonaro: {total_bolsonaro}')
            print(f'Lula: {total_lula}')
            break
        else:
            pass
    except:
        print('Digite apenas 13 ou 22')
    os.system('cls')
