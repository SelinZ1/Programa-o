soma = 0
contador = 1
while True:
    numero = int(input(f"Qual o {contador} numero ? "))
    if numero == 0:
        print ("Fim")
        break
    soma = soma + numero
    contador = contador + 1
print (f"{soma}")