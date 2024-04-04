#VERIFICADOR DE IDADE CRIANÇA (-13 ANOS) ADOLESCENTE 13 A 17, ADULTO +18 E IDOSO +60
nome = str (input("Qual seu nome : "))
idade = int (input("Qual sua idade ? "))
if (idade <= 13):
   print (nome, "você tem", idade, "é um criança") 
elif (idade <= 17):
    print (nome, "você tem", idade, "é um adolescente")
elif (idade <= 59):
    print (nome, "você tem", idade, "é um adulto")
else :
    print (nome, "você tem", idade, "é um idoso")