num1 = float (input("Escolha um numero : "))
operador = str (input("Escolha um operador : "))
num2 = float (input("Escolha outro numero : "))
if operador == "+":
    print ("O resultado é = ",num1 + num2)
elif operador == "-":
    print ("O resultado é = ",num1 - num2)
elif operador == "*":
    print ("O resultado é = ", num1 * num2)
elif operador == "/":
    print ("O resultado é = ", num1 / num2)
else:
    Error "404"
# Uma calculadora :)