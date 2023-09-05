from operacoesbd import *

connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")


def listar_bd():  # função para listar as linhas do banco de dados

    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    sql = "select * from manifestacoes"
    resultado = listarBancoDados(connect, sql)
    if len(resultado) == 0:  # checa se existem linhas no banco de dados através do método len()
        print("Sem manifestações cadastradas.")
    else:
        for i in resultado:  # imprime cada linha separadamente utilizando o hífen para separar os elementos de cada
            # linha
            print(*i, sep=" - ")


def listarTipo_bd():  # função para listar as linhas do banco de dados por tipo de manifestação

    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    tipo = input("Digite o tipo de manifestação a ser listada (1 - Reclamação; 2 - Sugestão; 3 - Elogio): ")

    if tipo == "1":
        tipo_selecionado = "Reclamação"
    elif tipo == "2":
        tipo_selecionado = "Sugestão"
    elif tipo == "3":
        tipo_selecionado = "Elogio"
    else:
        print("Opção inválida!")
        return

    sql = "select * from manifestacoes where tipo = '{}'".format(tipo_selecionado)
    resultado = listarBancoDados(connect, sql)

    if len(resultado) == 0:
        print("Sem manifestações desse tipo cadastradas.")
    else:
        for i in resultado:
            print(*i, sep=" - ")


def add_bd():
    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    titulo = input("Digite o título da manifestação: ")
    descricao = input("Digite a descrição da manifestação: ")
    autor = input("Digite o nome do autor da manifestação: ")

    print("Selecione o tipo de manifestação:")
    print("1. Reclamação")
    print("2. Sugestão")
    print("3. Elogio")

    opcao = input("Digite o número correspondente à opção: ")

    if opcao == "1":
        tipo = "Reclamação"
    elif opcao == "2":
        tipo = "Sugestão"
    elif opcao == "3":
        tipo = "Elogio"
    else:
        print("Opção inválida!")
        return

    sql = "INSERT INTO manifestacoes (titulo, descricao, autor, tipo) VALUES (%s, %s, %s, %s)"
    dados = (titulo, descricao, autor, tipo)
    insertNoBancoDados(connect, sql, dados)

    print("Manifestação criada com sucesso!")


def exibirQuantidadesManifestacoes():
    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    cursor = connect.cursor()

    quantidade_geral, quantidade_reclamacoes, quantidade_elogios, quantidade_sugestoes = obterQuantidadesManifestacoes(
        cursor)

    # Display the results
    print("Quantidade Geral de Manifestações:", quantidade_geral)
    print("Quantidade de Reclamações:", quantidade_reclamacoes)
    print("Quantidade de Elogios:", quantidade_elogios)
    print("Quantidade de Sugestões:", quantidade_sugestoes)


def pesquisar_bd():
    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    codigo = input("Digite o código da manifestação a ser pesquisada: ")
    sql = "select * from manifestacoes where codigo = {}".format(codigo)
    resultado = listarBancoDados(connect, sql)

    if len(resultado) == 0:
        print("Não existe manifestação com o código informado")
    else:
        for i in resultado:
            print(*i, sep=" - ")


def editar_bd():
    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    codigo = input("Digite o código da manifestação a ser editada: ")
    sql = "SELECT codigo FROM manifestacoes WHERE codigo = {}".format(codigo)
    resultado = listarBancoDados(connect, sql)

    if resultado:  # Verifica se o resultado não está vazio
        titulo = input("Digite o novo título: ")
        descricao = input("Digite a nova descrição: ")
        sql = "UPDATE manifestacoes SET titulo = %s, descricao = %s WHERE codigo = %s"
        atualizarBancoDados(connect, sql, (titulo, descricao, codigo))
        print("Manifestação editada com sucesso!")
    else:
        print("Código inválido")


def excluir_bd():  # função para excluir manifestação do banco de dados
    connect = abrirBancoDados("localhost", "root", "root", "bdouvidoria")
    codigo = input("Digite o código da manifestação a ser excluída: ")
    sql = "delete from manifestacoes where codigo = {}".format(codigo)
    resultado = excluirBancoDados(connect, sql, ())

    if resultado:
        print("A ocorrência foi apagada com sucesso!")
    else:
        print("Código inexistente! Tente novamente.")
