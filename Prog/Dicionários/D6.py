calorias = {'Sushi': 40, 'Doce de abóbora': 130, 'Almôndega': 60}
alimento = input('Digite o nome de um alimento: ')
calorias = calorias.get(alimento)
if calorias:
    print(alimento, 'tem', calorias, 'calorias.')
else:
    print('Não há esse alimento nesse dicionário.')
