n=int(input("Qual o número que você quer saber se tem dois digitos iguais?: "))

igual=False


while n != 0 and not igual:
    n1=n%10
    n=n//10
    n2=n%10
    if n1 == n2:
        igual=True

if igual:
    print("sim")
else:
    print("não")
