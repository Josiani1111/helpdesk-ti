# 🎫 HelpDesk TI

Sistema web para gerenciamento de chamados de suporte técnico, desenvolvido com **Python, FastAPI e SQLite**.

O projeto simula um sistema de HelpDesk, permitindo registrar chamados, acompanhar seu status, filtrar atendimentos e gerenciar os registros por meio de uma interface web.

## 📌 Sobre o projeto

O **HelpDesk TI** foi desenvolvido como projeto prático para aplicar conhecimentos de desenvolvimento web, APIs, banco de dados e operações CRUD.

A aplicação permite organizar chamados de suporte técnico desde sua abertura até a conclusão do atendimento.

## 🚀 Funcionalidades

* Cadastro de chamados
* Registro de usuário, equipamento e problema
* Definição de prioridade: **Baixa, Média e Alta**
* Alteração de status:

  * Aberto
  * Em andamento
  * Concluído
* Filtro de chamados por status
* Listagem dos chamados mais recentes
* Exclusão de chamados
* Confirmação antes da exclusão
* Persistência dos dados em banco SQLite
* Interface web responsiva

## 🛠️ Tecnologias utilizadas

* **Python**
* **FastAPI**
* **SQLite**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Git**
* **GitHub**

## 🔄 Operações CRUD

O projeto utiliza operações CRUD para gerenciamento dos chamados:

* **Create** — cadastro de chamados
* **Read** — consulta e listagem dos chamados
* **Update** — alteração do status
* **Delete** — exclusão de chamados

## 📁 Estrutura do projeto

```text
helpdesk-ti/
│
├── app/
│   ├── main.py
│   └── database.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ Como executar

### 1. Clone o repositório

Clone o projeto para o seu computador.

### 2. Acesse a pasta do projeto

Abra o **PowerShell** dentro da pasta `helpdesk-ti`.

### 3. Crie um ambiente virtual

```powershell
py -m venv .venv
```

### 4. Ative o ambiente virtual

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instale as dependências

```powershell
pip install -r requirements.txt
```

### 6. Execute a aplicação

```powershell
uvicorn app.main:app --reload
```

### 7. Acesse no navegador

```text
http://127.0.0.1:8000
```

## 📚 Conhecimentos praticados

Durante o desenvolvimento deste projeto, foram praticados:

* Desenvolvimento de APIs com **FastAPI**
* Criação de aplicações web com Python
* Operações **CRUD**
* Banco de dados **SQLite**
* SQL
* Manipulação de formulários HTML
* Integração entre frontend e backend
* Alteração e filtragem de dados
* Tratamento de registros
* Organização de projeto
* Git e GitHub

## 🎯 Objetivo do projeto

Este projeto faz parte da minha formação em **Análise e Desenvolvimento de Sistemas** e da construção do meu portfólio profissional em tecnologia.

O objetivo foi transformar conhecimentos estudados em uma aplicação prática, trabalhando conceitos de **desenvolvimento web, APIs, banco de dados e CRUD**.

## 👩‍💻 Desenvolvedora

**Josiani Oliveira**

Estudante do último ano de Análise e Desenvolvimento de Sistemas.

---

⭐ Obrigada por visitar este projeto!
