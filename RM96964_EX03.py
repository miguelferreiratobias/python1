#Cap 3 - Lista de exercícios
#Exercício 3
#Miguel Angelo Francisco Ferreira Tobias
#RM96964

print("Seja bem vindo ao sistema que compara as notas das metades de sua sala Mr. Sant'ana")

nota_total_impar = 0
for aluno in range (1,51,2):
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(aluno)))
    nota_total_impar = nota_total_impar + nota
nota_media_impar = float(nota_total_impar / 25)
print("A média da turma ímpar foi de {:.2f}. Continue no sistema e insira as notas pares a seguir!".format(nota_media_impar))

nota_total_par = 0
for aluno in range (2,51,2):
    nota = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(aluno)))
    nota_total_par = nota_total_par + nota
nota_media_par = float(nota_total_par / 25)
print("A média da turma par foi de {:.2f}.".format(nota_media_par))

print("-------")
print("Ímpares:\nMédia:{}\nTotal:{}".format(nota_media_impar, nota_total_impar))
print("-------")
print("Pares:\nMédia:{}\nTotal:{}".format(nota_media_par, nota_total_par))

if nota_media_par == nota_media_impar:
    print("As duas salas tiveram a mesma nota média de {}".format(nota_media_par))
elif nota_media_par > nota_media_impar:
    print("A turma par teve uma média de {}, superando o desempenho dos ímpares.".format(nota_media_par))
elif nota_media_par < nota_media_impar:
    print("A turma ímpar teve uma média de {}, superando o desempenho dos pares.".format(nota_media_impar))