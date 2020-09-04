print('################################')
print('Bem vindo ao jogo de adivinhacao')
print('################################')

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range(1,5):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("Digite o seu numero:  ")
    numero = int(chute)
    print("Voce digitou ", chute)

    if(numero < 1 or numero > 100):
        print("Você digitar um número entre 1 e 10")
        continue

    acertou  = numero_secreto == numero
    maior = numero > numero_secreto
    menor = numero < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Voce errou! Seu chute foi maior que o numero secreto")
        elif(menor):
            print("Voce errou! Seu chute foi menor que o numero secreto")

    rodada += 1

print("Fim do jogo")