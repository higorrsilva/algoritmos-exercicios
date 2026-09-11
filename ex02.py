# Exercicio 02 - Calculo do carrinho de compras

titulo = "Calculo no carrinho de compras"
descricao = "Um cliente comprou dois livros, cada um por: "
texto_desconto = " e recebeu um desconto de: "
pergunta = "Quanto ele gastou?"
resposta = "Ele gastou: "

preco = 35.00
quantidade = 2
desconto = 10.00

subtotal = preco * quantidade
valor_final = subtotal - desconto

# :.2f deixa o numero com 2 casas decimais
print(f"""
{titulo}
{descricao}R$ {preco:.2f}{texto_desconto}R$ {desconto:.2f}
{pergunta}
{resposta}R$ {valor_final:.2f}
""")
