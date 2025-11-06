# Projeto 2: Sistemas de gestão em Python (C.R.U.D. Completo)
Este repositório contém dois sistemas C.R.U.D completos, desenvolvidos em Python, com foco na Programação Orientada a Objetos (POO) e estruturas de dados nativas ao Python. (Listas,Tuplas, Sets e Dicionários.)

## Tecnologias Utilizadas
| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3.12.3**| Linguagem principal para tanto a lógica quanto a interface de ambos os sistemas. |
| **JSON** | Utilizado para salvar os dados permanentemente no Sistema de Controle de Estoque |
| **POO(Classes)** | Arquitetura principal para permitir a melhor separação e customização tanto da Lógica de Negócio quanto da Interface de Usuário |

## 1. Sistema de Controle de Estoque (Projeto 1)
### Nota: Este sistema fora incrementado pós prazo, para ver o sistema original dentro do prazo, **[Clique aqui](https://github.com/alvarolucio2007/mini-projeto-python-alvaro-mariana/tree/af693224725d526940fae8d41e448ccb6d70c379)**
Sistema de gestão de produtos com persistência de dados (salvos em `estoque.json`), possuindo as seguintes funções:

### Menu e Funcionalidades

| Opção | Funcionalidade (CRUD) | Descrição |
| :---: | :--- | :--- |
| **[1]** | **Create** (Cadastrar) | Adiciona um novo produto, validando se o código já existe. |
| **[2]** | **Read** (Listar) | Exibe todos os produtos e seus detalhes. |
| **[3]** | **Read** (Buscar por Código) | Exibe os detalhes de um produto específico. |
| **[4]** | **Update** | Permite alterar qualquer campo de um produto (Nome, Preço, etc.) pelo seu código. |
| **[5]** | **Delete** (Excluir) | Remove um produto permanentemente pelo seu código. |
| **[6-8]**| **Relatórios/Busca** | Funções de filtro (por nome, categoria e estoque baixo). |
| **[9]** | Sair | Salva os dados no JSON e encerra o programa. |

## 2. Sistema de Controle de Alunos e Notas (Projeto 2)
Sistema simples de gestão escolar, focado em registrar notas, calcular médias e verificar estado de aprovação.

### Menu e Funcionalidades

| Opção | Funcionalidade | Descrição |
| :---: | :--- | :--- |
| **[1]** | Cadastrar aluno | Registra um novo aluno no sistema, usando o nome como identificador único. |
| **[2]** | Registrar notas | Permite inserir múltiplas notas para um aluno já cadastrado. As notas são validadas no intervalo de 0 a 10. |
| **[3]** | Listar alunos e médias | Exibe uma tabela com o nome de todos os alunos, as notas registradas e suas médias calculadas. |
| **[4]** | Buscar aluno | Exibe os detalhes (Notas, Média e Status) de um aluno específico pelo nome. |
| **[5]** | Mostrar Aprovados/Reprovados | Lista os alunos com base no critério de aprovação: Média $\ge 7.0$ (Aprovado) e Média $< 7.0$ (Reprovado, desde que tenha notas). |
| **[6]** | Relatórios | Abre um sub-menu para visualizações detalhadas (Lista de Alunos, Médias Individuais, Aprovados/Reprovados). |
| **[0]** | Sair | Encerra o sistema. |

## Autores
### Este projeto de dupla foi desenvolvido por:
#### Sistema de Controle de Estoque (Projeto 1): Álvaro Lúcio Mousinho Coelho
#### Sistema de Controle de Alunos e Notas (Projeto 2): Mariana Siqueira Lima
