#5.2
cidades_populacoes = {'São Paulo': 12106920, 'Rio de Janeiro': 6718903, 'Brasília': 3055149, 'Salvador': 2886698, 'Fortaleza': 2669342}
cidade_maior_populacao = max(cidades_populacoes, key=cidades_populacoes.get)
print('A cidade com a maior população é:', cidade_maior_populacao)
