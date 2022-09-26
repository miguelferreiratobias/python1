#Cap 3 - Lista de exercícios
#Exercício 4
#Miguel Angelo Francisco Ferreira Tobias
#RM96964
#5!=5x4x3x2x1

min = int(input("Digite os minutos marcados na máquina: "))
fat = 1
while min > 1:
    fat = fat * min
    min -=1
print("Senha: LIBERDADE{}".format(fat))


