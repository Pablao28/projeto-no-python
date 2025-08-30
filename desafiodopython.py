INGRESSOS_DISPONIVEIS = 100
LIMITE_CONVIDADOS = 20

alunos = int(input("Quantos alunos vão participar? "))
monitores = int(input("Quantos monitores? "))
convidados = int(input("E quantos convidados? "))

total_pessoas = alunos + monitores + convidados

if convidados > LIMITE_CONVIDADOS:
    print("Vish! Não vai dar. O número de convidados passou do limite de 20.")
elif total_pessoas > INGRESSOS_DISPONIVEIS:
    print("Ih, lotou! O número total de pessoas é maior que 100. Não pode fazer o evento.")
else:
    print("Perfeito! O evento pode acontecer sem problemas.")
    print(f"No total, teremos {total_pessoas} pessoas.")
    print(f"Ainda sobram {INGRESSOS_DISPONIVEIS - total_pessoas} ingressos.")