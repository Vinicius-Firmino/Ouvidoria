import mysql.connector


def abrirBancoDados(host, user, password, database):
    return mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )


def encerrarBancoDados(connection):
    connection.close()


def insertNoBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id


def listarBancoDados(connection, sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    return results


def atualizarBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas


def excluirBancoDados(connection, sql, dados):
    cursor = connection.cursor()
    cursor.execute(sql, dados)
    connection.commit()
    linhasAfetadas = cursor.rowcount
    cursor.close()
    return linhasAfetadas


def obterQuantidadesManifestacoes(cursor):
    # consulta para saber a quantidade de Manifestações no total
    consulta_geral = "SELECT COUNT(*) FROM manifestacoes"
    cursor.execute(consulta_geral)
    quantidade_geral = cursor.fetchone()[0]

    # consulta para saber a quantidade de Reclações
    consulta_reclamacoes = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'reclamacao'"
    cursor.execute(consulta_reclamacoes)
    quantidade_reclamacoes = cursor.fetchone()[0]

    # consulta para saber a quantidade de Elogios
    consulta_elogios = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'elogio'"
    cursor.execute(consulta_elogios)
    quantidade_elogios = cursor.fetchone()[0]

    # consulta para saber a quantidade de Sugestões
    consulta_sugestoes = "SELECT COUNT(*) FROM manifestacoes WHERE tipo = 'sugestao'"
    cursor.execute(consulta_sugestoes)
    quantidade_sugestoes = cursor.fetchone()[0]

    return quantidade_geral, quantidade_reclamacoes, quantidade_elogios, quantidade_sugestoes
