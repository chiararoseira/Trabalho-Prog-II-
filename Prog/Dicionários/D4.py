#4.2
capitais = {'Paraná': 'Curitiba', 'Bahia': 'Salvador', 'Mato Grosso': 'Cuiabá'}
estado = input('Insira o nome de um estado brasileiro: ')
capital = capitais.get(estado)
if capital:
    print('A capital desse estado', estado, 'é', capital.')
else:
    print('Não há esse estado nesse dicionário.')
