#CONVERSOR DE NOTA EM CONCEITO (9+=A, 7.5+=B, 6+=C, 4+=D, RESTO = F)
nota = float (input("Qual a nota do aluno ? "))
if (nota >= 9):
    print ("Aluno nota A")
elif (nota >= 7.5):
    print ("Aluno nota B")
elif (nota >= 6):
    print ("Aluno nota C")
elif (nota >= 4):
    print ("Aluno nota D")
else:
    print ("Aluno nota F")