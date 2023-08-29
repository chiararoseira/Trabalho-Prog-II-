#4.3
pessoas = ('Robson', 'Nilce', 'Jorge', 'André', 'Nicole')
numero = int(input('Insira um número de 1 a 5: '))
if 1 <= numero <= 5:
    nome = pessoas[numero - 1]
    print(“O nome do número inserido é :”, nome)
else:
    print(“Esse número não contém nome.”)
