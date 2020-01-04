meuCartão=int(input("Digite o número do seu cartão de crédito: "))

cartãoLido=1
encontreicartão=False

while cartãoLido !=0 and not encontreicartão:
    cartãoLido = int(input("Digite o número do seu cartão de crédito: "))
    if cartãoLido == meuCartão:
        encontreicartão=True

if encontreicartão:
    print("Meu cartão está lá")
else:
    print("Não encontrei meu cartão lá")
