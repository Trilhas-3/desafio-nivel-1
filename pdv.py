# Desafio 1 - PDV com Descontos

registros = []

print("==== PDV COM DESCONTOS ====")

while True:
    valor_unitario, idade = float(), int()
    while True:
        valor_unitario = float(input("Insira o valor da compra: "))
        if valor_unitario < 0:
            print("Valor inválido! Tente novamente!")
            continue
        break

    if valor_unitario == 0:
        break

    while True:
        idade = int(input("Insira a idade do cliente: "))
        if idade < 0:
            print("Idade inválida! Tente novamente!")
            continue
        break

    cupom = str(input("Insira um cupom (opcional): "))

    while True:
        quantidade = int(input("Insira a quantidade de itens: "))
        if quantidade <= 0:
            print("Quantidade deve ser maior ou igual a 1!")
            continue
        break

    valor_final = valor_unitario * quantidade
    desconto_cupom, desconto_qtd = 0, 0
    desconto_idade, desconto_valor = 0, 0

    if idade >= 65:
        desconto_idade = 0.2
        valor_final *= 1 - desconto_idade

    if valor_final > 100:
        desconto_valor = 0.1
        valor_final *= 1 - desconto_valor

    if quantidade > 3:
        desconto_qtd = 0.05
        valor_final -= (valor_unitario * quantidade) * desconto_qtd

    if cupom == "FIDELIDADE10":
        print("Cupom FIDELIDADE10 aplicado com sucesso!")
        desconto_cupom = 0.1
        valor_final -= (valor_unitario * quantidade) * desconto_valor

    dados_compra = {
        "valor": valor_unitario,
        "quantidade": quantidade,
        "idade": idade,
        "desconto_idade": desconto_idade,
        "desconto_valor": desconto_valor,
        "desconto_qtd": desconto_qtd, 
        "desconto_cupom": desconto_cupom,
        "valor_final": valor_final, 
    }

    registros.append(dados_compra)
    print(f"A compra foi registrada!")

print("Finalizando...\n")

# Exibir registros

print("\nREGISTROS DE COMPRAS\n")

print(
    "NUM".ljust(6),
    "VALOR".rjust(10),
    "QUANT.".rjust(10),
    "IDADE".rjust(7),
    "DESC. IDADE".rjust(13),
    "DESC. VALOR".rjust(13),
    "DESC. QUANTIDADE".rjust(18),
    "DESC. CUPOM".rjust(13),
    "VALOR FINAL".rjust(13),
)

print("-" * 120)

for num, registro in enumerate(registros):
    print(
        str(num+1).ljust(6),
        f'R$ {registro["valor"]:.2f}'.rjust(10),
        str(registro["quantidade"]).rjust(10),
        str(registro["idade"]).rjust(7),
        f'{registro["desconto_idade"] * 100:.0f}%'.rjust(13),
        f'{registro["desconto_valor"] * 100:.0f}%'.rjust(13),
        f'{registro["desconto_qtd"] * 100:.0f}%'.rjust(18),
        f'{registro["desconto_cupom"] * 100:.0f}%'.rjust(13),
        f'R$ {registro["valor_final"]:.2f}'.rjust(13),
    )

# Salvar em 'resumo.txt'

with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    header = ", ".join([
            "NUM",
            "VALOR",
            "QUANT.",
            "IDADE",
            "DESC. IDADE",
            "DESC. VALOR",
            "DESC. QUANTIDADE",
            "DESC. CUPOM",
            "VALOR FINAL"
            ])
    arquivo.write(header + "\n")
    for num, registro in enumerate(registros):
        linha = ", ".join([
            str(num+1),
            f'R$ {registro["valor"]:.2f}',
            str(registro["quantidade"]),
            str(registro["idade"]),
            f'{registro["desconto_idade"] * 100:.0f}%',
            f'{registro["desconto_valor"] * 100:.0f}%',
            f'{registro["desconto_qtd"] * 100:.0f}%',
            f'{registro["desconto_cupom"] * 100:.0f}%',
            f'R$ {registro["valor_final"]:.2f}'
        ])
        arquivo.write(linha + "\n")

        