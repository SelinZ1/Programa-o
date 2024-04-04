#Calculadora de IMC
peso = float (input("Qual seu peso ? "))
altura = float (input("Qual sua altura ? "))
imc = peso/(altura * altura)
print ("Seu IMC é =" , imc)
if (imc <= 18.4):
    print ("Esta abaixo do peso")
elif (imc <= 24.9):
    print ("Peso normal")
elif (imc <= 29.9):
    print ("Acima do peso")
else:
    print ("Obesidade")