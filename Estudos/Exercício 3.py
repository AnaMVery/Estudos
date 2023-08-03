acumulador = 0#Acummula os valores dos acompanhamentos pra se pedirem mais de um
print('Bem-vindo ao Programa de Feijoada da Ana Maria Very!')
while True:
    try:#para confirmar valores numéricos inteiros
        volumeFeijoada = int(input('Quanto você deseja de feijoada? (ml)'))
        if volumeFeijoada < 300:
            print('Não trabalhamos com medidas abaixo de 300 ml e acima de 5L')
            continue
        elif 300 <= volumeFeijoada <= 5000:
            qtd = volumeFeijoada * 0.08
            break
        elif volumeFeijoada > 5000:
            print('Não trabalhamos com medidas abaixo de 300 ml e acima de 5L')
            continue
        else:
            print('Isso não é uma quantidade. Tente novamente')
            continue
    except ValueError:
        print('Isso não é um valor numérico aceitável')
while True:
    opcaoFeijoada = input('Qual opção deseja?\n'
                   'B - Básica(Feijão + paiol + costelinha) \n'
                   'P - Premium(Feijão + paiol + costelinha + partes de porco);\n'
                   'Ou S - Suprema(Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)\n').upper()
    if opcaoFeijoada == 'B':
        multiplicador = 1
        break#os "breaks" servem para quebrar o loop
    elif opcaoFeijoada == 'P':
        multiplicador = 1.25
        break
    elif opcaoFeijoada == 'S':
        multiplicador = 1.5
        break
    else:
        print('Não temos essa opção no cardápio')
        continue
while True:
    try:#confirma os valores numéricos
        acompanhamentoFeijoada = int(input('Você desejaria acompanhamentos?\n'
                                           '0-Não desejo mais acompanhamentos (encerrar pedido)\n'
                                           '1- 200g de arroz(R$5,00)\n'
                                           '2- 150g de farofa especial(R$6,00)\n'
                                           '3- 100g de couve cozida(R$7,00)\n'
                                           '4- 1 laranja descascada(R$3,00)\n'))
        if acompanhamentoFeijoada == 0:
            total = qtd * multiplicador + acumulador
            break#fica num loop infinito até fazer essa condição se satisfazer
        elif acompanhamentoFeijoada == 1:
            print('Você gostaria de mais algum?')
            acumulador = acumulador + 5
            continue
        elif acompanhamentoFeijoada == 2:
            print('Você gostaria de mais algum?')
            acumulador = acumulador + 6
            continue
        elif acompanhamentoFeijoada == 3:
            print('Você gostaria de mais algum?')
            acumulador = acumulador + 7
            continue
        elif acompanhamentoFeijoada == 4:
            acumulador = acumulador + 3
            continue
        else:
            print('Não temos essa opção no cardápio.')
            continue
    except ValueError:
        print('Por favor use número inteiros')
print('O total da sua compra deu: R${:.2f} (volume = R${:.2f}'
      ' * opção = {} + acompanhamentos = R${:.2f})'.format(total, qtd, multiplicador, acumulador))
#termina entregando os valores conforme o exemplo