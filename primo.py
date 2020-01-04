n=int(input("Digite um número inteiro: "))

primo=True
d=2

while primo and d < n:
    div=n%d
    d+=1
    if div == 0:
        primo=False

if primo:
    print("Primo")
else:
    print("não primo")
        





    
        



    
