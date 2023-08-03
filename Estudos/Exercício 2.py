acumulador = 0 #Recebe o valor das pizzas e soma como valor total
print('Bem-vindo a pizzaria da Ana Maria Very!')
print('---------------------Cardápio-----------------------\n'
      '| Código | Descrição  | Pizza Média | Pizza Grande |\n'
      '|   21   | Napolitana |   R$20,00   |   R$26,00    |\n'
      '|   22   | Margherita |   R$20,00   |   R$26,00    |\n'
      '|   23   | Calabresa  |   R$25,00   |   R$32,50    |\n'
      '|   24   | Toscana    |   R$30,00   |   R$39,00    |\n'
      '|   25   | Portuguesa |   R$30,00   |   R$39,00    |\n'
      '----------------------------------------------------')
while True:
  tamanho = input('Qual o tamanho da pizza que deseja? (M/G)').upper()
  #uso do "upper" para transformar as respostas em maiúsuclo mesemo quando digitadas em minúsculo para não ocorrer erros
  if tamanho == 'M':
    multiplicador = 1
  elif tamanho == 'G':
    multiplicador = 1.3
  else:
       print('Opção inválida!')
       continue #volta para o começo do while True
  codigo = input ('Digite o código do sabor desejado:')
  if codigo == '21':
     print('Você escolheu uma Pizza Napolitana')
     valor_pizza = 20 * multiplicador
  elif codigo == '22':
     print('Você escolheu uma Pizza Margherita')
     valor_pizza = 20 * multiplicador
  elif codigo == '23':
     print('Você escolheu uma Pizza de Calabresa')
     valor_pizza = 25 * multiplicador
  elif codigo == '24':
     print('Você escolheu uma Pizza Toscana')
     valor_pizza = 30 * multiplicador
  elif codigo == '25':
     print('Você escolheu uma Pizza Portuguesa')
     valor_pizza = 30 * multiplicador
  else:
     print('Opção inválida')
     continue
  acumulador = acumulador + valor_pizza #somatório dos valores das pizzas
  pedido = input('Deseja pedir mais alguma coisa?\n'
                 'S - Sim\n'
                 'N - Não\n').upper()
  if pedido == 'S':
      continue
  else:
      print('O total a ser pago é: R${:.2f}'.format(acumulador)) #total a ser pago em formato monetário
  break




