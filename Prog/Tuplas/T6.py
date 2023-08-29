#6.3
cores = ('Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Azul', 'Anil', 'Violeta')
cor = input('Insira uma cor: ')
if cor in cores:
    print('Essa cor', cor, 'pertence à tupla arco-íris.')
else:
    print('Essa cor', cor, 'não pertence à tupla arco-íris.')
