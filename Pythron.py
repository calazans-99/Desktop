print ("Condicinal")
print("Calculo da media")
#Ebtrada de dados
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
n_faltas = int(input("Faltas: "))
#Processamento 
media = (nota1 + nota2) / 2
#Saida de dados
print(f"Media: {media : .1f}")

#If / Else / elif -- Lógica.
if n_faltas > 18:
    print("Reprovado por falta")
elif media == 10 and n_faltas < 18:
    print("Super aprovado, monstro!")
elif media >= 6 and n_faltas < 18:
    print("Aprovado")
elif media >= 4 < 6 and n_faltas < 18:
    print("Exame.")
    exame = float(input("Nota do exame: "))
    media = (media + exame)/2
    if media >= 6:
        print(f"Aprovado no exame!{media : .1f}")
    else:
        print(f"Reprovado no exame também!{media : .1f}")
else: 
    print("Reprovado!")
