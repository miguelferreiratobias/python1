#Cap 3 - Lista de exercícios
#Exercício 2
#Miguel Angelo Francisco Ferreira Tobias
#RM96964

print("Seja bem vindo, siga as instruções abaixo para descobrir o melhor dia para realização das lives!")
vt_seg = int(input("Digite a quantidade de votos a favor de lives na segunda-feira: "))
vt_ter = int(input("Digite a quantidade de votos a favor de lives na terça-feira: "))
vt_qua = int(input("Digite a quantidade de votos a favor de lives na quarta-feira: "))
vt_qui = int(input("Digite a quantidade de votos a favor de lives na quinta-feira: "))
vt_sex = int(input("Digite a quantidade de votos a favor de lives na sexta-feira: "))
if vt_seg > vt_ter and vt_seg > vt_qua and vt_seg > vt_qui and vt_seg > vt_sex:
    print("Segunda-feira foi o dia escolhido para as lives!")
elif vt_ter > vt_seg and vt_ter > vt_qua and vt_ter > vt_qui and vt_ter > vt_sex:
    print("Terça-feira foi o dia escolhido para as lives!")
elif vt_qua > vt_seg and vt_qua > vt_ter and vt_qua > vt_qui and vt_qua > vt_sex:
    print("Quarta-feira foi o dia escolhido para as lives!")
elif vt_qui > vt_seg and vt_qui > vt_ter and vt_qui > vt_qua and vt_qui > vt_sex:
    print("Quinta-feira foi o dia escolhido para as lives!")
elif vt_sex > vt_seg and vt_sex > vt_ter and vt_sex > vt_qui and vt_sex > vt_qua:
    print("Sexta-feira foi o dia escolhido para as lives!")
else:
    print("Empate técnico entre dois ou mais dias da semana, por favor, repita a votação e tente novamente!")