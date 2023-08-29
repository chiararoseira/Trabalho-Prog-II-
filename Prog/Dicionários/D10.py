#10.2
jogos_jogadores = {'Mario Party': 4, 'Munchkin': 2, 'Mario Kart': 8}
jogo = input('Digite o nome de um jogo: ')
jogadores = jogos_jogadores.get(jogo)
if jogadores:
    print('Para jogar', jogo, 'são necessários', jogadores, 'jogadores.')
else:
    print('Jogo há esse jogo nesse dicionário.')
