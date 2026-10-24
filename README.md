# 🛒 PDV com descontos

Este programa simula um ponto de venda (PDV): registra compras, calcula descontos conforme as informações de cada venda e apresenta um resumo das compras realizadas. Ao encerrar o registro, exibe os dados no terminal e grava uma cópia em `resumo.txt`.

## ⚙️ Como funciona

1. O programa solicita o valor unitário da compra. Valores negativos são recusados; informar `0` encerra o registro de compras.
2. Para cada compra, solicita a idade do cliente, um cupom opcional e a quantidade de itens. A idade não pode ser negativa e a quantidade deve ser pelo menos `1`.
3. Calcula o valor inicial multiplicando o valor unitário pela quantidade.
4. Aplica, nesta ordem, os descontos: 20% para clientes com 65 anos ou mais; 10% se o valor após esse desconto for maior que R$ 100; e 5% se a quantidade for maior que 3. O desconto por quantidade é calculado sobre o valor inicial da compra.
5. Se o cupom informado for `FIDELIDADE10`, o programa registra 10% como desconto de cupom. No cálculo do valor final, porém, subtrai o valor inicial multiplicado pelo desconto por valor (o desconto condicionado à compra acima de R$ 100), e não pelo percentual do cupom.
6. Guarda cada compra numa lista. Depois que o valor `0` encerra a entrada, mostra uma tabela com as compras e seus descontos no terminal e salva os mesmos registros em `resumo.txt`, no diretório de execução.

## 📊 Tabela de exemplos

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---:|---:|---:|---:|---:|---:|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |

## ▶️ Como rodar

No terminal, dentro da pasta `nivel_1`, execute:

```bash
python pdv.py
```