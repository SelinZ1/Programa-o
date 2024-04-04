#VERIFICADOR DE ANO BISSEXTO (DIGITA UM ANO E DIZ SE É OU NAO)
ano = int (input("Qual ano que deseja verificar : "))
if (ano % 4 == 0):
    print ("Esse ano é bissexto")
else:
    print ("Esse ano não é bissexto")