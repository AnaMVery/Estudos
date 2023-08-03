valor = float(input('Qual o valor do produto?\n'))
qtd = int(input('Quantos itens você deseja comprar?\n'))
if 0 < qtd <= 4:
    desconto = valor * qtd * 0
elif 5 <= qtd <= 19:
    desconto = valor * qtd * 0.03 
elif 20 <= qtd <= 99:
    desconto = valor * qtd * 0.06
elif qtd >= 100:
    desconto = valor * qtd * 0.1
else: print('erro')
fin=input('Você confirma?'+qtd +'itens, de' + valor + 'reais.(S/N)')
if fin == 'S': total = float(valor * qtd)
else: print('erro')
print('O total deu' + total + 'reais')