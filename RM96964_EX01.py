#Cap 3 - Lista de exercícios
#Exercício 1
#Miguel Angelo Francisco Ferreira Tobias
#RM96964

print("Seja bem vindo!")
assinatura = int(input("Digite o número correspondente com sua assinatura: 1-Basic, 2-Silver, 3-Gold, 4-Platinum "))
faturamento = float(input("Digite o seu faturamento anual com o canal do YouTube, utilize ponto ao invés de vírgula: "))
if assinatura == 1:
    pct_fatur= faturamento * 0.30
    fatur_liquid= faturamento - pct_fatur
    print("Como seu plano é o Basic e seu faturamento foi {:.2f}, você deve nos pagar {:.2f}. Sendo assim te sobrará {:.2f}.".format(faturamento, pct_fatur, fatur_liquid))
elif assinatura == 2:
    pct_fatur= faturamento * 0.20
    fatur_liquid= faturamento - pct_fatur
    print("Como seu plano é o Silver e seu faturamento foi {:.2f}, você deve nos pagar {:.2f}. Sendo assim te sobrará {:.2f}.".format(faturamento, pct_fatur, fatur_liquid))
elif assinatura == 3:
    pct_fatur= faturamento * 0.10
    fatur_liquid= faturamento - pct_fatur
    print("Como seu plano é o Gold e seu faturamento foi {:.2f}, você deve nos pagar {:.2f}. Sendo assim te sobrará {:.2f}.".format(faturamento, pct_fatur, fatur_liquid))
elif assinatura == 4:
    pct_fatur= faturamento * 0.05
    fatur_liquid= faturamento - pct_fatur
    print("Como seu plano é o Platinum e seu faturamento foi {:.2f}, você deve nos pagar {:.2f}. Sendo assim te sobrará {:.2f}.".format(faturamento, pct_fatur, fatur_liquid))
else:
    print("Formato inválido. Reinicie o sistema e tente novamente!")