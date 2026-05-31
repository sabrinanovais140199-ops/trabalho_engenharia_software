# Construindo um Projeto Ágil no GitHub: Gerenciador de Tarefas

## 1. Objetivo do Projeto

Este projeto visa desenvolver um sistema de gerenciamento de tarefas baseado em metodologias ágeis, simulando um cenário real de desenvolvimento de software para uma startup de logística. O sistema permitirá acompanhar o fluxo de trabalho, priorizar tarefas e monitorar o desempenho da equipe.

## 2. Escopo Inicial

O escopo inicial do projeto inclui as seguintes funcionalidades:

*   **CRUD (Create, Read, Update, Delete) de Tarefas:** Capacidade de adicionar, visualizar, editar e excluir tarefas.
*   **Visualização Kanban:** Apresentação das tarefas em um quadro Kanban com as colunas "A Fazer", "Em Progresso" e "Concluído".
*   **Testes Automatizados:** Implementação de testes unitários para garantir a qualidade do código.
*   **Integração Contínua:** Configuração de um pipeline com GitHub Actions para execução automática dos testes.

## 3. Metodologia Adotada

Foi adotada uma metodologia ágil, com foco em **Kanban**, para gerenciar o fluxo de trabalho. O Kanban permite uma visualização clara das tarefas, otimizando a entrega contínua e a adaptação a mudanças. O GitHub Projects será utilizado para simular o quadro Kanban.

## 4. Estrutura do Repositório

O repositório está organizado da seguinte forma:

*   `app.py`: Arquivo principal da aplicação Flask, contendo a lógica do CRUD e as rotas.
*   `templates/index.html`: Template HTML para a interface do usuário, exibindo o quadro Kanban.
*   `requirements.txt`: Lista de dependências do projeto Python.
*   `tests/test_app.py`: Arquivo contendo os testes unitários para a aplicação.
*   `.github/workflows/main.yml`: Configuração do pipeline de integração contínua com GitHub Actions.

## 5. Instruções para Executar o Sistema

Para executar a aplicação localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [URL_DO_REPOSITORIO]
    cd software_engineering_project
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
    A aplicação estará disponível em `http://127.0.0.1:5000/`.

## 6. Controle de Qualidade (GitHub Actions)

Um pipeline de CI/CD foi configurado usando GitHub Actions para garantir a qualidade do código. Sempre que houver um `push` ou `pull request` para a branch `main`, os testes automatizados serão executados. O workflow está definido em `.github/workflows/main.yml`.

## 7. Histórico de Commits

O histórico de commits será mantido de forma semântica e descritiva, registrando as atividades e alterações realizadas ao longo do desenvolvimento.

## 8. Gestão de Mudanças: Simulação de Alteração de Escopo
* Status: Funcionalidade de filtro por status planejada e documentada.

**Justificativa da Mudança:**

Durante o desenvolvimento, o cliente solicitou uma nova funcionalidade: a capacidade de filtrar tarefas por status. Esta mudança foi incorporada para aumentar a usabilidade do sistema e atender a uma necessidade emergente da startup de logística, que precisa de uma visão mais granular do progresso das tarefas.

**Adaptação no Kanban:**

Para acomodar essa mudança, um novo card foi adicionado ao quadro Kanban na coluna "A Fazer": "Implementar filtro de tarefas por status". Após a implementação, este card será movido para "Concluído".

## 9. Quadro Kanban (Simulação)

### A Fazer

*   Implementar filtro de tarefas por status.
*   Adicionar autenticação de usuário.

### Em Progresso

*   Refatorar código da interface de usuário

### Concluído

*   Configuração inicial do projeto Flask
*   Implementação do CRUD de tarefas
*   Criação da interface Kanban
*   Configuração de testes unitários com Pytest
*   Configuração do pipeline de CI com GitHub Actions
*   Criação do README.md inicial
* Desenvolvido por: Sabrina Novais.