from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from app.database import conectar
from datetime import datetime

app = FastAPI(title="HelpDesk TI")


@app.get("/", response_class=HTMLResponse)
def home():

    conexao = conectar()

    chamados = conexao.execute("""
        SELECT *
        FROM chamados
        ORDER BY id DESC
    """).fetchall()

    conexao.close()

    linhas = ""

    for c in chamados:

        status = c["status"].lower()

        if status == "aberto":
            cor = "#dc2626"
        elif status == "em andamento":
            cor = "#d97706"
        else:
            cor = "#16a34a"

        linhas += f"""
        <tr data-status="{c['status'].lower().replace(' ', '-')}">

            <td>{c["id"]}</td>

            <td>{c["usuario"]}</td>

            <td>{c["equipamento"]}</td>

            <td>{c["problema"]}</td>

            <td>{c["prioridade"]}</td>

            <td>

                <select
                    class="status-select {c['status'].lower().replace(' ', '-')}"
                    onchange="alterarStatus({c['id']}, this.value)"
                >

                    <option {"selected" if c["status"].lower() == "aberto" else ""}>
                        Aberto
                    </option>

                    <option {"selected" if c["status"].lower() == "em andamento" else ""}>
                        Em andamento
                    </option>

                    <option {"selected" if c["status"].lower() == "concluído" else ""}>
                        Concluído
                    </option>

                </select>

            </td>

            <td>{c["data_abertura"]}</td>

            <td>

                <button
                    class="btn-excluir"
                    onclick="excluirChamado({c['id']})"
                >
                    Excluir
                </button>

            </td>

        </tr>
        """

    return f"""
    <!DOCTYPE html>

    <html lang="pt-br">

    <head>

        <meta charset="UTF-8">

        <meta name="viewport"
              content="width=device-width, initial-scale=1.0">

        <title>HelpDesk TI</title>

        <style>

            body {{
                font-family: Arial, sans-serif;
                background: #eef3f8;
                margin: 0;
                padding: 40px;
            }}

            h1 {{
                color: #1e3a8a;
            }}

            .card {{
                background: white;
                padding: 25px;
                border-radius: 12px;
                margin-bottom: 25px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.10);
            }}

            input, select {{
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                box-sizing: border-box;
                border: 1px solid #ccc;
                border-radius: 6px;
            }}

            .status-select {{
                font-weight: bold;
            }}

            .status-select.aberto {{
                color: #dc2626;
            }}

            .status-select.em-andamento {{
                color: #d97706;
            }}

            .status-select.concluído {{
                color: #16a34a;
            }}

            button {{
                background: #2563eb;
                color: white;
                border: none;
                padding: 10px 15px;
                border-radius: 8px;
                cursor: pointer;
                font-weight: bold;
            }}

            button:hover {{
                background: #1d4ed8;
            }}

            .btn-excluir {{
                background: #dc2626;
            }}

            .btn-excluir:hover {{
                background: #b91c1c;
            }}

            .tabela {{
                overflow-x: auto;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}

            th, td {{
                padding: 10px;
                border: 1px solid #ddd;
                text-align: left;
            }}

            th {{
                background: #1e3a8a;
                color: white;
            }}

        </style>

    </head>

    <body>

        <h1>HelpDesk TI</h1>


        <div class="card">

            <h2>Novo Chamado</h2>

            <form action="/chamados" method="post">

                <input
                    name="usuario"
                    placeholder="Usuário"
                    required
                >

                <input
                    name="equipamento"
                    placeholder="Equipamento"
                    required
                >

                <input
                    name="problema"
                    placeholder="Descreva o problema"
                    required
                >

                <select name="prioridade">

                    <option>Baixa</option>
                    <option>Média</option>
                    <option>Alta</option>

                </select>

                <button type="submit">
                    Abrir Chamado
                </button>

            </form>

        </div>


        <div class="card">

            <h2>Chamados Registrados</h2>

            <label for="filtroStatus">
                Filtrar por status:
            </label>

            <select id="filtroStatus">

                <option value="todos">
                    Todos
                </option>

                <option value="aberto">
                    Aberto
                </option>

                <option value="em-andamento">
                    Em andamento
                </option>

                <option value="concluído">
                    Concluído
                </option>

            </select>


            <div class="tabela">

                <table>

                    <tr>
                        <th>ID</th>
                        <th>Usuário</th>
                        <th>Equipamento</th>
                        <th>Problema</th>
                        <th>Prioridade</th>
                        <th>Status</th>
                        <th>Data de abertura</th>
                        <th>Ação</th>
                    </tr>

                    {linhas}

                </table>

            </div>

        </div>


        <script>

            async function alterarStatus(id, status) {{

                const dados = new FormData();

                dados.append("status", status);

                const resposta = await fetch(
                    `/chamados/${{id}}`,
                    {{
                        method: "PUT",
                        body: dados
                    }}
                );

                if (resposta.ok) {{

                    window.location.href = "/";

                }} else {{

                    alert("Erro ao alterar o status.");

                }}

            }}


            async function excluirChamado(id) {{

                const confirmar = confirm(
                    "Deseja realmente excluir este chamado?"
                );

                if (!confirmar) {{

                    return;

                }}

                const resposta = await fetch(
                    `/chamados/${{id}}`,
                    {{
                        method: "DELETE"
                    }}
                );

                if (resposta.ok) {{

                    window.location.reload();

                }} else {{

                    alert("Erro ao excluir o chamado.");

                }}

            }}


            document.getElementById("filtroStatus")
                .addEventListener("change", function() {{

                    const filtro = this.value;

                    const linhas = document.querySelectorAll(
                        "table tr[data-status]"
                    );

                    linhas.forEach(function(linha) {{

                        const status = linha.getAttribute("data-status");

                        if (filtro === "todos" || filtro === status) {{

                            linha.style.display = "";

                        }} else {{

                            linha.style.display = "none";

                        }}

                    }});

                }});

        </script>


    </body>

    </html>
    """


@app.post("/chamados")
def criar_chamado(
    usuario: str = Form(...),
    equipamento: str = Form(...),
    problema: str = Form(...),
    prioridade: str = Form(...),
):

    conexao = conectar()

    status = "Aberto"

    data_abertura = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    conexao.execute("""
        INSERT INTO chamados
        (usuario, equipamento, problema, prioridade, status, data_abertura)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        usuario,
        equipamento,
        problema,
        prioridade,
        status,
        data_abertura
    ))

    conexao.commit()
    conexao.close()

    return RedirectResponse(
        url="/",
        status_code=303
    )


@app.get("/chamados")
def listar_chamados():

    conexao = conectar()

    chamados = conexao.execute("""
        SELECT *
        FROM chamados
        ORDER BY id DESC
    """).fetchall()

    conexao.close()

    return [dict(chamado) for chamado in chamados]


@app.put("/chamados/{chamado_id}")
def atualizar_chamado(
    chamado_id: int,
    status: str = Form(...),
):

    conexao = conectar()

    conexao.execute("""
        UPDATE chamados
        SET status = ?
        WHERE id = ?
    """, (
        status,
        chamado_id
    ))

    conexao.commit()
    conexao.close()

    return {
        "mensagem": "Chamado atualizado com sucesso!"
    }


@app.delete("/chamados/{chamado_id}")
def excluir_chamado(chamado_id: int):

    conexao = conectar()

    conexao.execute("""
        DELETE FROM chamados
        WHERE id = ?
    """, (chamado_id,))

    conexao.commit()
    conexao.close()

    return {
        "mensagem": "Chamado excluído com sucesso!"
    }