alunos_e_notas = {}
alunos_cadastrados_set = set()
rodando = True

def calcular_media(notas):
    if notas:
        media = sum(notas) / len(notas)
        return media
    return 0.0

def exibir_menu():
    print()
    print("Menu Principal:")
    print("Escola: Gerenciamento de Notas")
    print("1 - Cadastrar aluno")
    print("2 - Registrar notas")
    print("3 - Listar alunos e médias")
    print("4 - Buscar aluno")
    print("5 - Mostrar aprovados e reprovados")
    print("6 - Relatórios")
    print("0 - Sair")
    print()

def cadastrar_aluno():
    print("Cadastrar Aluno")
    while True:
        nome_aluno = input("Digite o nome completo do aluno (ou 'voltar' para cancelar): ").strip()
        
        if nome_aluno.lower() == 'voltar':
            print("Cadastro cancelado.")
            return

        if nome_aluno in alunos_cadastrados_set:
            print(f"O aluno '{nome_aluno}' já está cadastrado.")
        elif not nome_aluno:
             print("O nome do aluno não pode ser vazio.")
        else:
            alunos_cadastrados_set.add(nome_aluno)
            alunos_e_notas[nome_aluno] = tuple() 
            print(f"'{nome_aluno}' cadastrado com sucesso!")
            break

def registrar_notas():
    print("Registrar Notas")
    
    if not alunos_e_notas:
        print("Nenhum aluno cadastrado ainda. Cadastre um aluno primeiro.")
        return

    print("Alunos cadastrados:")
    for aluno in alunos_e_notas.keys():
        print(f"- {aluno}")
        
    nome_aluno = input("Digite o nome do aluno para registrar as notas: ").strip()

    if nome_aluno in alunos_e_notas:
        notas_temporarias = []
        print("Digite as notas (digite 'fim' para terminar):")
        
        while True:
            nota_input = input(f"Nota {len(notas_temporarias) + 1}: ").lower().strip()
            
            if nota_input == 'fim':
                break
            
            try:
                nota = float(nota_input)
                
                if 0 <= nota <= 10:
                    notas_temporarias.append(nota)
                else:
                    print("A nota deve ser entre 0 e 10. Tente novamente.")

            except ValueError:
                print("Entrada inválida. Digite um número para a nota ou 'fim'.")
        
        alunos_e_notas[nome_aluno] = tuple(notas_temporarias)
        print(f"{len(notas_temporarias)} notas registradas para '{nome_aluno}'.")
        
    else:
        print(f"Aluno '{nome_aluno}' não encontrado.")

def listar_alunos_e_medias():
    print("Lista de Alunos e Médias")

    if not alunos_e_notas:
        print("Nenhum aluno cadastrado para listar.")
        return

    print("Aluno | Notas | Média")

    for nome, notas in alunos_e_notas.items():
        media = calcular_media(notas)
        notas_str = ", ".join(f"{n:.1f}" for n in notas)
        
        print(f"{nome} | {notas_str} | {media:.2f}")

def buscar_aluno():
    print("Buscar Aluno")
    
    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip()
    
    if nome_busca in alunos_e_notas:
        notas = alunos_e_notas[nome_busca]
        media = calcular_media(notas)
        
        print("Resultado")
        print(f"Nome: {nome_busca}")
        print(f"Notas: {', '.join(f'{n:.1f}' for n in notas) if notas else 'Nenhuma nota registrada'}")
        print(f"Média: {media:.2f}")
        
        if media >= 7.0:
            print("Status:APROVADO")
        elif media > 0.0:
            print("Status:REPROVADO")
        else:
            print("Status:Sem média para calcular")
    else:
        print(f"Aluno '{nome_busca}' não encontrado no sistema.")

def mostrar_aprovados_reprovados():
    print("Aprovados e Reprovados")
    
    if not alunos_e_notas:
        print("Nenhum aluno cadastrado para verificar.")
        return
        
    aprovados = []
    reprovados = []
    
    for nome, notas in alunos_e_notas.items():
        media = calcular_media(notas)
        
        if media >= 7.0:
            aprovados.append((nome, media))
        elif media < 7.0 and len(notas) > 0:
            reprovados.append((nome, media))
    
    print("APROVADOS")
    if aprovados:
        for nome, media in aprovados:
            print(f"- {nome} (Média: {media:.2f})")
    else:
        print("Nenhum aluno aprovado ainda.")
        
    print("REPROVADOS")
    if reprovados:
        for nome, media in reprovados:
            print(f"- {nome} (Média: {media:.2f})")
    else:
        print("Nenhum aluno reprovado com notas registradas.")

def menu_relatorios():
    print("Relatórios")
    print("a - Alunos cadastrados")
    print("b - Médias individuais")
    print("c - Aprovados (média ≥ 7) e Reprovados (média < 7)")
    print("v - Voltar ao menu principal")
    
    escolha = input("Escolha o tipo de relatório (a/b/c/v): ").lower().strip()
    
    if escolha == 'a':
        print("--- Relatório: Alunos Cadastrados ---")
        if alunos_cadastrados_set:
            for aluno in sorted(alunos_cadastrados_set):
                print(f"- {aluno}")
            print(f"Total de alunos: {len(alunos_cadastrados_set)}")
        else:
            print("Nenhum aluno cadastrado.")
            
    elif escolha == 'b':
        print("--- Relatório: Médias Individuais ---")
        listar_alunos_e_medias() 
        
    elif escolha == 'c':
        mostrar_aprovados_reprovados()
        
    elif escolha == 'v':
        print("Voltando ao menu principal.")
    else:
        print("Opção inválida no menu de relatórios.")

print("Bem-vindo(a) ao Sistema de Gestão Escolar (Versão Iniciante)!")

while rodando:
    exibir_menu()
    
    escolha = input("Digite sua opção: ").strip()
    
    if escolha == '1':
        cadastrar_aluno()
    elif escolha == '2':
        registrar_notas()
    elif escolha == '3':
        listar_alunos_e_medias()
    elif escolha == '4':
        buscar_aluno()
    elif escolha == '5':
        mostrar_aprovados_reprovados()
    elif escolha == '6':
        menu_relatorios()
    elif escolha == '0':
        rodando = False
        print("O sistema será encerrado. Até mais!")
    else:
        print("Opção inválida. Por favor, escolha um número de 0 a 6.")