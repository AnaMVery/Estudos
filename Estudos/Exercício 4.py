produtos = []#Cria um conjunto em branco pra permitir o usuário adicionar itens
print('Bem-vindo ao Controle de Estoque da Mercearia da Ana Maria Very')
#-------------------divisão para organizar
def cadastrarProduto(cod):#Define a função "cadastrarProduto" pra usar mais a frente, em parênteses define qual variável vai enviar pro código principal
    print('Você selecionou a opção de cadastrar um produto.')
    print('Código do produto: {}'.format(cod))
    nome_produto = input('Nome do produto:')
    fabricante_produto = input('Fabricante do produto:')
    valor_produto = float(input('Valor do produto:'))
    lalala = {'Código do prouto' : cod,
              'Nome do produto'       : nome_produto,
              'Fabricante do produto' : fabricante_produto,
              'Valor do produto'      : valor_produto}
    produtos.append(lalala.copy())
#-------------------divisão para organizar
def consultarProduto():#Define a função "consultarProduto" pra usar mais a frente
    print('Você selecionou a opção de consultar produtos.')
    while True:
        try:
            consulta = int(input('Escolha a opção desejada:\n'
                              '1 - Consultar todos os produtos\n'
                              '2 - Consultar produtos por código\n'
                              '3 - Consultar produtos por fabricante\n'
                              '4 - Voltar\n'
                              '>>'))
            if consulta == 1:
                for product in produtos:
                    for key, value in product.items():
                        print('{} : {}'.format(key, value))
            elif consulta == 2:
                entrada = int(input('Digite o código do produto: '))
                for product in produtos:
                    if(product ['Código do prouto'] == entrada):
                        for key, value in product.items():
                            print('{} : {}'.format(key, value))
            elif consulta == 3:
                entry = input('Digite a marca do produto: ')
                for product in produtos:
                    if (product['Fabricante do produto'] == entry):
                        for key, value in product.items():
                            print('{} : {}'.format(key, value))
            elif consulta == 4:
                return#volta pro código principal
            else:
                print('Não temos essa opção.')
        except ValueError:
            print('Use números inteiros por favor')
#-------------------divisão para organizar
def removerProduto():#Define a função "removerProduto" pra usar mais a frente
    print('Você selecionou a opção de remover um produto.')
    entrada = int(input('Digite o código do produto que deseja remover: '))
    for product in produtos:
        if (product['Código do prouto'] == entrada):
            produtos.remove(product)
#-------------------divisão para organizar
codigo = 0
while True:
    try:#pra caso tentem usar números com vírgula, código principal
        geral = int(input('Escolha a opção desejada:\n'
                      '1 - Cadastrar produtos\n'
                      '2 - Consultar produto(s)\n'
                      '3 - Remover produto\n'
                      '4 - Sair\n'
                      '>>'))
        if geral == 1:
            codigo = codigo + 1
            cadastrarProduto(codigo)#usa a contagem codigo como referência para sua função
        elif geral == 2:
            consultarProduto()
        elif geral == 3:
            removerProduto()
        elif geral == 4:
            print('Fim do programa.')
            break
        else:
            print('Não temos essa opção.')
            continue
    except ValueError:#em caso de erro volta pro início do programa principal
        print('Use números inteiros por favor')
        continue