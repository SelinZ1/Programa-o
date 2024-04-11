nome = str(input("Qual o seu nome? "))
idade = int(input("Qual a sua idade? "))

if idade < 13:
    print(f"{nome}, você tem {idade} anos, é uma criança.") 
elif 13 <= idade <= 17:
    print(f"{nome}, você tem {idade} anos, é um adolescente.")
elif 18 <= idade <= 59:
    print(f"{nome}, você tem {idade} anos, é um adulto.")
else:
    print(f"{nome}, você tem {idade} anos, é um idoso.")
