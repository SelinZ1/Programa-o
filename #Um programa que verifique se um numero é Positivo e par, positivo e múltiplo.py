print('''Bem-Vindo ao Verificador de números : Selecione o numero da escolha
1 - Número Par 
2 - Número Ímpar
3 - Número Múltiplo de 3
4 - Positivo
5 - Negativo''')

numero = float(input("Qual número deseja verificar? "))

if numero == 0:
    print("O número é zero.")
elif numero > 0:
    if numero % 2 == 0 and numero % 3 == 0:
        print(f"O número {numero} é positivo, par e múltiplo de 3.")
    elif numero % 2 == 0:
        print(f"O número {numero} é positivo e par, mas não é múltiplo de 3.")
    elif numero % 3 == 0:
         print(f"O número {numero} é positivo e múltiplo de 3.")
    else:
        print(f"O número {numero} é positivo e ímpar.")
else:  # Números negativos
    if numero % 2 == 0:
        print(f"O número {numero} é negativo e par.")
    elif numero % 3 == 0:
        print(f"O número {numero} é negativo e ímpar e múltiplo de 3.")
    else:
        print(f"O número {numero} é negativo e ímpar, mas não é múltiplo de 3.")
