# Calculadora de desconto
# Dou o preço e a % de desconto e o programa me retorna com o valor com desconto

preco = float(input("Qual o preço do item? "))
porcentagem = float(input("Qual a % de desconto? "))

desconto = preco * (porcentagem / 100)
preco_final = preco - desconto

print("O preço com desconto fica R$", preco_final)
