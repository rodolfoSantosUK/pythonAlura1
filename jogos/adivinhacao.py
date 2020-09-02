print('################################')
print('Bem vindo ao jogo de adivinhacao')
print('################################')

numero_secreto = 42
chute = input("Digite o seu numero:  ")
numero = int(chute)
print("Voce digitou ", chute)

acertou  = numero_secreto == numero
maior = numero > numero_secreto
menor = numero < numero_secreto

if(acertou):
    print("Você acertou")
else:
    if(maior):
        print("Voce errou! Seu chute foi maior que o numero secreto")
    elif(menor):
        print("Voce errou! Seu chute foi menor que o numero secreto")

