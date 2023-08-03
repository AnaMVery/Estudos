print ('Bem-vindo a loja da Ana Maria Very!')
valor = float(input('Qual o valor do produto?')) #valor do produto em float pois pode conter decimais
qtd = int(input('Quantos itens você deseja comprar?')) #quantidade de itens

#Valores dos descontos
#Sem desconto até 4 itens
if 0 <= qtd <= 4:
    desconto = valor * qtd * 0
    descontoX = 'Não há desconto'
#3% de desconto de 5 à 19 itens
elif 5 <= qtd <= 19:
    desconto = valor * qtd * 0.03
    descontoX = 'Desconto de 3%'
#6% de desconto de 20 à 99 itens
elif 20 <= qtd <= 99:
    desconto = valor * qtd * 0.06
    descontoX = 'Desconto de 6%'
#10% de desconto de 100 itens ou acima
elif 100 <= qtd:
    desconto = valor * qtd * 0.1
    descontoX = 'Desconto de 10%'
#valor total da compra SEM o desconto
print ('O valor sem desconto foi: {:.2f}.'.format(valor * qtd))
#valor total da compra COM o desconto
print ('O valor com desconto foi: {:.2f} ({})'.format(valor * qtd - desconto, descontoX))


