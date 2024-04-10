# Um programa que verifica se um número é Positivo e par, positivo e múltiplo de três, negativo e ímpar, Zero ou se não é nenhum desses
numero = int(input("Fale um numero : "))

if numero == 0:
    print("O número é zero.")

elif numero > 0:
    if numero % 2 == 0 and numero % 3 == 0:
        print(f"O número {numero} é positivo, par e múltiplo de 3.")
    elif numero % 2 == 0:
        print(f"O número {numero} é positivo e par, mas não é múltiplo de 3.")
    else:
        print(f"O número {numero} é positivo e ímpar.")

else:  # Números negativos
    if numero % 2 == 0:
        print(f"O número {numero} é negativo e par.")
    elif numero % 3 == 0:
        print(f"O número {numero} é negativo e ímpar e múltiplo de 3.")
    else:
        print(f"O número {numero} é negativo e ímpar, mas não é múltiplo de 3.")
