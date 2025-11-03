# 📂 Projeto 2: Sistemas de Gestão em Python (CRUD Completo)

Este repositório contém dois sistemas de gestão completos (CRUD - Create, Read, Update, Delete) desenvolvidos em Python, focando na aplicação de Programação Orientada a Objetos (POO) e no uso eficaz de estruturas de dados nativas do Python (Listas, Dicionários, Tuplas e Sets).

## 🧑‍💻 Tecnologias Utilizadas

| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3** | Linguagem principal para a lógica de negócio e interface de linha de comando (CLI). |
| **JSON** | Utilizado para persistência de dados no Sistema de Controle de Estoque. |
| **POO (Classes)** | Arquitetura principal para separar a Lógica de Negócio (`ControleEstoque`, `ControleEscolar`) da Interface de Usuário (`SistemaEstoqueCLI`, `SistemaEscolarCLI`). |

---

## 📦 1. Sistema de Controle de Estoque (Projeto 1)

Sistema de gestão de produtos com persistência de dados (salvos em `estoque.json`), focado no controle de código, preço, categoria e quantidade.

### Estruturas de Dados Aplicadas:

* **Lista de Dicionários:** `lista_produtos` armazena todos os dados de estoque.
* **Set:** `codigos_registrados` garante que cada produto tenha um código único (sem duplicatas).
* **Tupla:** `tupla_categorias` armazena as categorias fixas permitidas (Alimento, Limpeza, Higiene, Outros).

### ⚙️ Menu e Funcionalidades

O sistema é operado via CLI (Command Line Interface).

| Opção | Funcionalidade (CRUD) | Descrição |
| :---: | :--- | :--- |
| **[1]** | **Create** (Cadastrar) | Adiciona um novo produto, validando se o código já existe. |
| **[2]** | **Read** (Listar) | Exibe todos os produtos e seus detalhes. |
| **[3]** | **Read** (Buscar por Código) | Exibe os detalhes de um produto específico. |
| **[4]** | **Update** | Permite alterar qualquer campo de um produto (Nome, Preço, etc.) pelo seu código. |
| **[5]** | **Delete** (Excluir) | Remove um produto permanentemente pelo seu código. |
| **[6-8]**| **Relatórios/Busca** | Funções de filtro (por nome, categoria e estoque baixo). |
| **[9]** | Sair | Salva os dados no JSON e encerra o programa. |

---

## 🎓 2. Sistema de Controle de Alunos e Notas (Projeto 2)

Sistema simples de gestão escolar focado em registrar notas, calcular médias e verificar o status de aprovação (`Média ≥ 7.0`).

### Estruturas de Dados Aplicadas:

* **Dicionário:** `alunos_e_dados` é a estrutura principal. A **chave** é a `matrícula` do aluno, e o **valor** é uma tupla contendo o nome e a tupla de notas: `{'M001': ('Ana', (8.0, 7.5))}`.
* **Set:** `matrículas_set` garante que cada matrícula gerada seja única.
* **Tupla:** Armazena as notas de cada aluno de forma imutável após o registro.

### ⚙️ Menu e Funcionalidades

| Opção | Funcionalidade | Descrição |
| :---: | :--- | :--- |
| **[1]** | Cadastrar aluno | Gera uma matrícula única e registra o aluno. |
| **[2]** | Registrar notas | Permite inserir múltiplas notas para um aluno (por matrícula). |
| **[3]** | Listar alunos e médias | Exibe uma tabela com todos os alunos, notas registradas e suas médias. |
| **[4]** | Buscar aluno | Exibe os dados, média e status de um aluno específico (por matrícula). |
| **[6]** | Relatórios | Sub-menu que permite listar: **a)** Alunos cadastrados; **b)** Médias Individuais; **c)** Aprovados e Reprovados. |
| **[0]** | Sair | Encerra o programa. |

---

## 🚀 Como Rodar os Projetos

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado.
2.  **Clonar o Repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd [pasta_do_projeto]
    ```
3.  **Execução:**
    * Para rodar o **Sistema de Estoque**:
        ```bash
        python estoque.py 
        # Ou o nome do arquivo que contém a classe SistemaEstoqueCLI
        ```
    * Para rodar o **Sistema de Notas**:
        ```bash
        python notas.py 
        # Ou o nome do arquivo que contém a classe SistemaEscolarCLI
        ```

*(Seus projetos devem estar em arquivos separados, ex: `estoque.py` e `notas.py`)*

## ✒️ Autores

* **[Seu Nome Aqui]** - Implementação do Sistema de Controle de Estoque.
* **[Nome da Sua Amiga Aqui]** - Implementação do Sistema de Controle de Alunos e Notas.

---