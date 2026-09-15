# Exercicio 04 - Classificador de acesso (if, elif, else)
# Regras:
# menor de 16 anos -> acesso nao permitido
# 16 ou mais + tem ingresso -> entrada liberada
# 16 ou mais + sem ingresso -> precisa comprar ingresso

idade = int(input("Digite sua idade: "))
resposta = input("Voce possui ingresso? (sim/nao): ").lower()

tem_ingresso = resposta == "sim"

if idade < 16:
    mensagem = "Acesso nao permitido"
elif idade >= 16 and tem_ingresso:
    mensagem = "Entrada liberada"
else:
    mensagem = "Compre um ingresso"

print("\n--- RESULTADO ---")
print("Idade:", idade)
print("Tem ingresso:", tem_ingresso)
print("Status:", mensagem)
