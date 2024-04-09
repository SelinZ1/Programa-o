#CALCULADORA DE JUROS SIMPLES (teremos Valor principal, taxa de juros e o periodo)
valor = float (input ("Qual o valor total ? "))
juros = float (input ("Qual a taxa de juros ? "))
periodo = int (input ("Qual o periodo em meses ? "))
juroSimples = (valor * juros * periodo )
print (f'Irá ter que pagar {juroSimples} por {periodo} meses')
#1 - Pega o valor total 2 - Pega a taxa de juros 3 - Pega o periodo em meses 4 - Faz o calculo de juros simples 5 - Mostra na tela 
