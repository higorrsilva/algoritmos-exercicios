# Exercicio 01 - Tipos, variaveis e expressoes em Python
 
# variavel de texto
nome_linguagem = "Python"
print(nome_linguagem)
 
# expressao matematica simples (multiplicacao antes da soma)
resultado = 2 + 3 * 4
print(resultado)
 
# outra variavel de texto
mensagem = "Ola, Python!"
print(mensagem)
 
# guardando o mesmo calculo em outra variavel
conta = 2 + 3 * 4
print(conta)
 
# isso aqui e so um texto, nao um calculo
texto_conta = "2 + 3 * 4"
print(texto_conta)
 
# juntando texto com numero (precisa converter com str)
frase = texto_conta + " = " + str(conta)
print(frase)
 
# a mesma coisa só que usando f-string, fica mais facil de ler
frase2 = f"{texto_conta} = {conta}"
print(frase2)
 
# mostrando o tipo de cada variavel
print(type(nome_linguagem))
print(type(resultado))
print(type(mensagem))
 








