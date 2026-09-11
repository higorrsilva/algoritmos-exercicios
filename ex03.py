# Exercicio 03 - Sistema de compras com entrada de dados

print("=== SISTEMA DE COMPRAS ===")

nome_cliente = input("Nome do cliente: ")
produto = input("Nome do produto: ")
preco = float(input("Preco unitario (R$): "))
quantidade = int(input("Quantidade: "))
desconto_percentual = float(input("Percentual de desconto (%): "))

subtotal = preco * quantidade
valor_desconto = subtotal * (desconto_percentual / 100)
total = subtotal - valor_desconto
valor_medio = total / quantidade

print("\n--- RECIBO ---")
print("Cliente:", nome_cliente)
print("Produto:", produto)
print("Quantidade:", quantidade)
print(f"Preco unitario: R$ {preco:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto ({desconto_percentual:.0f}%): R$ {valor_desconto:.2f}")
print(f"Total a pagar: R$ {total:.2f}")
print(f"Valor medio por unidade: R$ {valor_medio:.2f}")
print("\nObrigado pela compra!")
