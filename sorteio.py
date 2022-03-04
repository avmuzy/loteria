import random
n1 = int(input(("Digite o primeiro numero:")))
n2 = int(input(("Digite o segundo numero:")))
n3 = int(input(("Digite o terceiro numero:")))
n4 = int(input(("Digite o quarto numero:")))
n5 = int(input(("Digite o quinto numero:")))
n6 = int(input(("Digite o sexto numero:")))
digitados = [n1, n2, n3, n4, n5, n6]
sorteio = [random.randint(1, 60) for x in range(6)]
print(sorteio)
print(digitados)
if digitados == sorteio:
    print("Parabens voce acertou!")
else:
    print("Que pena, voce errou")
