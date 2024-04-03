num1 = float (input("Fale um numero : "))
num2 = float (input("Fale outro numero : "))
num3 = float (input("Fale outro numero : "))
if (num1 == num2 == num3):
    print ("Error 404")
elif (num1 > num2 and num3):
    print (num1, "É o maior")
elif (num2 > num1 and num2 > num3):
    print (num2, "É o maior")
else :
    print (num3, "É o maior")

# Verificador de maior numero :)