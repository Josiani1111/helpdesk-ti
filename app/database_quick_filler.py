import sqlite3

DATABASE = "helpdesk.db"


def conectar():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            equipamento TEXT NOT NULL,
            problema TEXT NOT NULL,
            prioridade TEXT NOT NULL,
            status TEXT NOT NULL,
            data_abertura TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

    if __name__ == "__main__":
    criar_tabela()
    print("Banco de dados criado com sucesso!")