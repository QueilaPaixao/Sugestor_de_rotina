print('-=' * 20)
titulo = str('{:^40}'.format('Hora do remédio'))
print(titulo)
print('-=' * 20)
horas =int(input('Digite a cada quantas horas o remédio deverá ser tomado: '))
print()
print(f'O seu remedio deverá ser tomado a cada \033[0;31m{horas} horas\033[m')
print()
print('Essas são as opções:')
print('')
horario = 0
inicio = 0
final = 24

while inicio <24:
    print("Começando", inicio, 'h')
    for horario in range(inicio, final, horas):
        if horario >= 24:
            horario -= 24
        if horario in range(0, 8):
            print(horario, end='')
            print('h - Dormindo')
        if horario in range(8, 19):
            print(horario, end='')
            print('h - Na Escola')
        if horario in range(19, 24):
            print(horario, end='')
            print('h - Em Casa')
    inicio += 1
    final +=1
    print('-=' * 20)

print()
