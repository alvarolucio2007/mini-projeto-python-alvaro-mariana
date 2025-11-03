# Projeto 2: Sistemas de gestão em Python (C.R.U.D. Completo)
Este repositório contém dois sistemas C.R.U.D completos, desenvolvidos em Python, com foco na Programação Orientada a Objetos (POO) e estruturas de dados nativas ao Python. (Listas,Tuplas, Sets e Dicionários.)

## Tecnologias Utilizadas
| Tecnologia | Descrição |
| :--- | :--- |
| **Python 3.12.3**| Linguagem principal para tanto a lógica quanto a interface de ambos os sistemas. |
| **JSON** | Utilizado para salvar os dados permanentemente no Sistema de Controle de Estoque |
| **POO(Classes)** | Arquitetura principal para permitir a melhor separação e customização tanto da Lógica de Negócio quanto da Interface de Usuário |

## 1. Sistema de Controle de Estoque (Projeto 1)
Sistema de gestão de produtos com persistência de dados (salvos em `estoque.json`), possuindo as seguintes funções:
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
Sistema simples de gestão escolar, focado em registrar notas, calcular médias e verificar estado de aprovação