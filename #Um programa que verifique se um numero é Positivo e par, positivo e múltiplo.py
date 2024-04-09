#Um programa que verifique se um numero é Positivo e par, positivo e múltiplo de três, negativo e ímpar, Zero ou se não é nenhum desses
numero = float(input("Fale um numero : "))
if numero > 0 and numero % 2 == 0 :
    print ("O numero {numero} é Positivo e Par")
elif numero > 0 and numero % 2 != 0:
    print (f"O numero {numero} é Posiivo porem Impar")
elif numero < 0 and numero % 2 == 0 :
    print (f"O numero {numero} é Par porem Negativo")
elif numero < 0 and numero % 2 != 0 :
    print (f"O numero {numero} é Impar e Negativo")
else :
    print ("Error")