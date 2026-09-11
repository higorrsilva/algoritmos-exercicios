# Exercicio 05 - match/case em Python

# 1) match case simples com nota do aluno
nota = float(input("Digite a nota do aluno (0 a 10): "))

match nota:
    case nota if nota >= 9.0:
        classificacao = "EXCELENTE"
    case nota if nota >= 7.0:
        classificacao = "BOM"
    case nota if nota >= 5.0:
        classificacao = "REGULAR"
    case _:
        classificacao = "INSUFICIENTE"

print(f"Nota {nota} -> {classificacao}")


# 2) match case com uma lista (comando digitado pelo usuario)
print("\nExemplos de comando: login maria / buscar python / sair")
comando = input("Digite um comando: ").split()

match comando:
    case ["login", usuario]:
        print(f"Autenticando {usuario}")
    case ["buscar", termo]:
        print(f"Buscando {termo}")
    case ["sair"]:
        print("Sessao encerrada")
    case _:
        print("Comando invalido")


# 3) match case com nota e faltas do aluno
nome = input("\nNome do aluno: ")
nota2 = float(input("Nota do aluno: "))
faltas = int(input("Numero de faltas: "))

match faltas:
    case f if f > 10:
        situacao = "REPROVADO POR FALTA"
    case _:
        if nota2 >= 7.0:
            situacao = "APROVADO"
        elif nota2 >= 5.0:
            situacao = "EM RECUPERACAO"
        else:
            situacao = "REPROVADO"

print(f"{nome}: {situacao}")
