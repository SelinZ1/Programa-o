#VERIFICAÇÃO DE TRIANGULO E TIPO DE TRIANGULO ( DIZER SE COM OS 3 COMPRIMENTOS QUE VOCE FORNECEU É POSSIVEL FORMAR UM TRIANGULO) E DIZER DEPOIS QUAL E O TIPO DO TRIANGULO ( EQUILATERO, ISOCELES E ESCALENO)
lado1 = (input("Digite o tamanho do primeiro lado: "))
lado2 = (input("Digite o tamanho do segundo lado: "))
lado3 = (input("Digite o tamanho do terceiro lado: "))
if (a + b < c) or (a + c < b) or (b + c < a):
    print ("Não é um triangulo")
elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("É um triângulo equilátero.")
elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("É um triângulo escaleno.")
else:
    print("É um triângulo isósceles.")