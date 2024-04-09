# Conversor de unidade de medida : MI , POL , FT , CM , M , KM
unidademedida = print('''Em qual unidade de medida está ?
1 - Milhas (mi)
2 - Polegadas (Pol)
3 - Pés (ft)
4 - Centímetros (cm)
5 - Metros (m)
6 - Quilômetro (km)\n''')
escolha = input("Escolha uma opção : ")

if escolha == "1":
    mi = float(input("Coloque a medida em Milhas : "))
    km = mi * 1.609
    pol = mi * 63360
    ft = mi * 5280
    cm = mi * 160900
    m = mi * 1609
    print(f'A medida de {mi} em Milhas\nPara Polegadas: {pol}\nPara Pés: {ft}\nPara Centímetros: {cm}\nPara Metros: {m}\nPara Quilômetros: {km}\nESSES VALORES SÃO APROXIMADOS')
    
elif escolha == "2":
    pol = float(input("Coloque a medida em Polegadas : "))
    mi = pol * 1.5782789054609e-5
    ft = pol * 0.0833333
    cm = pol * 2.539998984
    m = pol * 0.02539998984
    km = pol * 2.539998984e-5
    print(f'A medida de {pol} em Polegadas\nPara Milhas: {mi}\nPara Pés: {ft}\nPara Centímetros: {cm}\nPara Metros: {m}\nPara Quilômetros: {km}\nESSES VALORES SÃO APROXIMADOS')
    
elif escolha == "3":
    ft = float(input("Coloque a medida em Pés : "))
    mi = ft * 0.00018939
    pol = ft * 12
    cm = ft * 30.48
    m = ft * 0.3048
    km = ft * 0.0003048
    print(f'A medida de {ft} em Pés\nPara Milhas : {mi}\nPara Polegadas: {pol}\nPara Centímetros: {cm}\nPara Metros: {m}\nPara Quilômetros: {km}\nESSES VALORES SÃO APROXIMADOS')
    
elif escolha == "4":
    cm = float(input("Coloque a medida em Centímetros : "))
    mi = cm * 6.2137e-6
    pol = cm * 0.393701
    ft = cm * 0.0328084
    m = cm * 0.01
    km = cm * 1e-5
    print(f'A medida de {cm} em Centímetros\nPara Milhas: {mi}\nPara Polegadas: {pol}\nPara Pés: {ft}\nPara Metros: {m}\nPara Quilômetros: {km}\nESSES VALORES SÃO APROXIMADOS')
    
elif escolha == "5":
    m = float(input("Coloque a medida em Metros : "))
    mi = m * 0.000621371
    pol = m * 39.3701
    ft = m * 3.28084
    cm = m * 100
    km = m * 0.001
    print(f'A medida de {m} em Metros\nPara Milhas: {mi}\nPara Polegadas: {pol}\nPara Pés: {ft}\nPara Centímetros: {cm}\nPara Quilômetros: {km}\nESSES VALORES SÃO APROXIMADOS')
    
elif escolha == "6":
    km = float(input("Coloque a medida em Quilômetros : "))
    mi = km * 0.621371
    pol = km * 39370.1
    ft = km * 3280.84
    m = km * 1000
    cm = km * 100000
    print(f'A medida de {km} em Quilômetros\nPara Milhas: {mi}\nPara Polegadas: {pol}\nPara Pés: {ft}\nPara Centímetros: {cm}\nPara Metros: {m}\nESSES VALORES SÃO APROXIMADOS')
    
else:
    print("Erro: Opção inválida")
