import json
class SistemaUm():  #Aqui é a lógica do sistema em si
    """Sisteminha CRUD completinho 
    Todos os produtos devem estar em uma lista de dicionários,
        que possuem códigos, guardados em um set, e ter uma tupla com categorias"""
    def __init__(self):
        self.lista_dict_produtos=[] #Cria uma lista vazia, toda vez que rodar, vai estar vazia
        self.set_codigos=set() #Cria um set vazio, ja que 2 produtos não possuem o mesmo código
        self.tupla_categorias=("Alimento","Limpeza","Higiene","Outros") #Apenas as 4 categorias, nada de muito especial.
        self.carregar_dados()
    def carregar_dados(self):
        try:
            with open("estoque.json","r") as arquivo:
                dados_json=json.load(arquivo)
                self.lista_dict_produtos=dados_json
                for produto in self.lista_dict_produtos:
                    self.set_codigos.add(produto["Código"])
        except FileNotFoundError:
            print("JSON de nome 'estoque.json' não encontrado!")
            return
    def salvar_dados(self):
        with open("estoque.json","w") as arquivo:
            json.dump(self.lista_dict_produtos,arquivo)
                 
    def cadastrar_produto(self,nome,codigo,categoria,preco,quantidade): #Cria e add um produto novo
        if codigo in self.set_codigos:
            print("Código já existente, por favor, tente novamente!")
            return     
        if categoria not in self.tupla_categorias:
            print(f"Categoria inexistente! Categorias possíveis: {self.tupla_categorias}")
            return
        if len(nome)<1:
            print("Nome inválido, por favor tente novamente!")
            return
        if preco<0:
            print("Preço inválido, por favor, tente novamente!")
            return
        if quantidade<0:
            print("Quantidade inválida, por favor tente novamente!")
            return
        produto={
            "Código":codigo,
            "Nome":nome,
            "Categoria":categoria,
            "Preço":preco,
            "Estoque":quantidade
        }
        self.lista_dict_produtos.append(produto)
        self.set_codigos.add(codigo)
        print(f"Produto '{nome}' cadastrado com sucesso!")
    
    def listar_produtos(self): #Mostra todos os produtos em estoque
        for i in range(len(self.lista_dict_produtos)):
            print(str(self.lista_dict_produtos[i]).replace("'","").replace("{","").replace("}",""))
    
    def atualizar_produto(self,codigo,campo,novo_valor):
        if codigo not in self.set_codigos or campo.lower() not in ["nome","categoria","preço","estoque"]:
            print("Parâmetros inválidos!")
            return
        if type(novo_valor)==str and len(novo_valor)<1:
            print("Por favor, insira um novo valor válido!")
            return
        if (type(novo_valor)==float or type(novo_valor)==int) and novo_valor<=0:
            print("Por favor, insira um valor numérico válido!")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==codigo:
                if campo.lower()=="nome":
                    self.lista_dict_produtos[i]["Nome"]=novo_valor
                    print("Nome atualizado com sucesso!")
                if campo.lower()=="categoria":
                    self.lista_dict_produtos[i]["Categoria"]=novo_valor
                    print("Categoria atualizada com sucesso!")
                if campo.lower()=="preço":
                    self.lista_dict_produtos[i]["Preço"]=novo_valor
                    print("Preço atualizado com sucesso!")
                if campo.lower()=="estoque":
                    self.lista_dict_produtos[i]["Estoque"]=novo_valor
                    print("Estoque atualizado com sucesso!")
                if campo.lower()=="codigo":
                    self.set_codigos.remove(codigo)
                    self.lista_dict_produtos[i]["Código"]=novo_valor
                    self.set_codigos.add(novo_valor)
                    print("Código atualizado com sucesso!")
    def buscar_produto(self,codigo): #Exibe informações de um produto específico
        if codigo not in self.set_codigos:
            print("Código inválido!")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==codigo:
                print(str(self.lista_dict_produtos[i]).replace("'","").replace("{","").replace("}",""))
    def excluir_produto(self,codigo): #Exclui um produto específico
        if codigo not in self.set_codigos:
            print("Código inválido!")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==codigo:
                self.lista_dict_produtos.pop(i)
                self.set_codigos.remove(codigo)
                print("Produto removido com sucesso!")
                break
    def sair_sistema(self): #Encerra o programa (o mais difícil de se programar kkkkkkkk)
        print("Saindo...")
        return

#Daqui pra baixo é a interação com o usuário via Terminal.

sistema_um=SistemaUm()
while True:
    pergunta_usuario=input("Você gostaria de usar o sistema? (s/n)")
    if pergunta_usuario.lower() not in ["s","n"]:
        print("Por favor, insira respostas válidas!")
    elif pergunta_usuario.lower()=="n":
        sistema_um.salvar_dados()
        print("Entendido, obrigado por usar o sistema! Desligando...")
        break
    else:
        while True:
            try:
                print("""
                === SISTEMA DE ESTOQUE ===
                1 - Cadastrar produto
                2 - Listar produtos
                3 - Buscar produto
                4 - Atualizar produto
                5 - Excluir produto
                6 - Sair
                """)
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                print("Por favor, insira um valor válido! Apenas entre 1 e 6.")
                continue
            if opcao not in range(1,7):
                print("Por favor, insira um valor válido! Apenas entre 1 e 6.")
                continue
            else:
                if opcao==1:
                    try:
                        nome=input("Qual o nome do produto?")
                        codigo=int(input("Qual o código do produto?"))
                        categoria=input("Qual a categoria do produto? (são Alimento, Limpeza, Higiene e Outros.)")
                        preco=float(input("Qual o preço do produto?"))
                        quantidade=int(input("Qual a quantidade do produto?"))
                    except ValueError:
                        print("Por favor, insira corretamente os valores! Em código, preço e quantidade, são números inteiros,float e inteiros respectivamente, mas em nome e categoria, são quaisquer um.")
                        continue
                    sistema_um.cadastrar_produto(nome,codigo,categoria,preco,quantidade)
                elif opcao==2:
                    sistema_um.listar_produtos()
                elif opcao==3:
                    try:
                        codigo=int(input("Qual o código do produto? (apenas números.)"))
                    except ValueError:
                        print("Por favor, insira apenas números!")
                        continue
                    sistema_um.buscar_produto(codigo)
                elif opcao==4:
                    try:
                        codigo=int(input("Qual o código do produto?"))
                    except ValueError:
                        print("Por favor, insira um código válido!")
                        continue
                    campo=input("Qual o campo no qual você gostaria de editar?")
                    novo_valor=input("Qual o novo valor para tal campo?")
                    sistema_um.atualizar_produto(codigo,campo,novo_valor)
                elif opcao==5:
                    try:
                        codigo=int(input("Qual o código do produto? (apenas números.)"))
                    except ValueError:
                            print("Por favor, insira apenas números!")
                            continue
                    sistema_um.excluir_produto(codigo)
                else:
                    sistema_um.sair_sistema()
                    break