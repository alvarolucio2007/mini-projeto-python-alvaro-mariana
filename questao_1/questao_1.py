import json,os,platform
class Cores:
    VERDE='\033[92m'
    VERMELHO='\033[91m'
    AMARELO='\033[93m'
    AZUL='\033[94m'
    RESET='\033[0m'
class ControleEstoque:  #Aqui é a lógica do sistema em si
    """Sisteminha CRUD completinho 
    Todos os produtos devem estar em uma lista de dicionários,
        que possuem códigos, guardados em um set, e ter uma tupla com categorias"""
    
    def __init__(self):
        self.lista_dict_produtos=[] #Cria uma lista vazia, toda vez que rodar, vai estar vazia
        self.set_codigos=set() #Cria um set vazio, ja que 2 produtos não possuem o mesmo código
        self.tupla_categorias=("Alimento","Limpeza","Higiene","Outros") #Apenas as 4 categorias, nada de muito especial.
        self.carregar_dados()
    
    def carregar_dados(self): #Usa JSON
        try:
            with open("questao_1/estoque.json","r") as arquivo:
                dados_json=json.load(arquivo)
                self.lista_dict_produtos=dados_json
                for produto in self.lista_dict_produtos:
                    self.set_codigos.add(produto["Código"])
        except FileNotFoundError:
            print(f"{Cores.VERMELHO}JSON de nome 'estoque.json' não encontrado!{Cores.RESET}")
            return
    
    def salvar_dados(self): #Também usa JSON
        with open("questao_1/estoque.json","w") as arquivo:
            json.dump(self.lista_dict_produtos,arquivo)
   
    def buscar_nome(self,nome):
        encontrados=[p for p in self.lista_dict_produtos if nome.lower() in p["Nome"].lower()]
        if encontrados:
            for x in encontrados:
                print(json.dumps(x, ensure_ascii=False, indent=2))
        else:
            print(f"{Cores.VERMELHO}Não encontrado! Por favor, cheque novamente ou adicione!{Cores.RESET}")
        return 
   
    def listar_por_categoria(self,categoria):
        lista_categoria_temp=[p for p in self.lista_dict_produtos if p["Categoria"].lower()== categoria.lower()]
        if lista_categoria_temp:
            for produto in lista_categoria_temp:
                print(json.dumps(produto, ensure_ascii=False, indent=2))
        else:
            print(f"Nenhum produto encontrado na categoria '{categoria}'!")
        return
   
    def mostrar_estoque_baixo(self,limite):
        encontrado=[p for p in self.lista_dict_produtos if p["Estoque"]<limite]
        if encontrado:
            for p in encontrado:
                print(json.dumps(p, ensure_ascii=False,indent=2))
        else:
            print("Nenhum encontrado.")
   
    def cadastrar_produto(self,nome,codigo,categoria,preco,quantidade): #Cria e add um produto novo
        if codigo in self.set_codigos:
            print(f"{Cores.VERMELHO}Código já existente, por favor, tente novamente!{Cores.RESET}")
            return     
        if categoria not in self.tupla_categorias:
            print(f"{Cores.VERMELHO}Categoria inexistente! Categorias possíveis: {self.tupla_categorias}{Cores.RESET}")
            return
        if len(nome)<1:
            print(f"{Cores.VERMELHO}Nome inválido, por favor tente novamente!{Cores.RESET}")
            return
        if preco<0:
            print(f"{Cores.VERMELHO}Preço inválido, por favor, tente novamente!{Cores.RESET}")
            return
        if quantidade<0:
            print(f"{Cores.VERMELHO}Quantidade inválida, por favor tente novamente!{Cores.RESET}")
            return
        produto={
            "Código":codigo,
            "Nome":nome,
            "Categoria":categoria,
            "Preço":preco,
            "Estoque":quantidade #
        }
        self.lista_dict_produtos.append(produto)
        self.set_codigos.add(codigo)
        self.salvar_dados()
        print(f"{Cores.VERDE}Produto '{nome}' cadastrado com sucesso!{Cores.RESET}")
    
   
    def listar_produtos(self): #Mostra todos os produtos em estoque
        for p in self.lista_dict_produtos:
            print(json.dumps(p,ensure_ascii=False,indent=2))
    
    def atualizar_produto(self,codigo,campo,novo_valor):
        if codigo not in self.set_codigos or campo.lower() not in ["nome","categoria","preço","estoque","codigo"]:
            print(f"{Cores.VERMELHO}Parâmetros inválidos!{Cores.RESET}")
            return
        if type(novo_valor)==str and len(novo_valor)<1:
            print(f"{Cores.VERMELHO}Por favor, insira um novo valor válido!{Cores.RESET}")
            return
        if (type(novo_valor)==float or type(novo_valor)==int) and novo_valor<0:
            print(f"{Cores.VERMELHO}Por favor, insira um valor numérico válido!{Cores.RESET}")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==codigo:
                if campo.lower()=="nome":
                    self.lista_dict_produtos[i]["Nome"]=novo_valor
                    print(f"{Cores.AZUL}Nome atualizado com sucesso!{Cores.RESET}")
                if campo.lower()=="categoria":
                    self.lista_dict_produtos[i]["Categoria"]=novo_valor
                    print(f"{Cores.AZUL}Categoria atualizada com sucesso!{Cores.RESET}")
                if campo.lower()=="preço":
                    self.lista_dict_produtos[i]["Preço"]=float(novo_valor)
                    print(f"{Cores.AZUL}Preço atualizado com sucesso!{Cores.RESET}")
                if campo.lower()=="estoque":
                    self.lista_dict_produtos[i]["Estoque"]=float(novo_valor)
                    print(f"{Cores.AZUL}Estoque atualizado com sucesso!{Cores.RESET}")
                if campo.lower()=="codigo":
                    self.set_codigos.remove(codigo)
                    self.lista_dict_produtos[i]["Código"]=int(novo_valor)
                    self.set_codigos.add(novo_valor)
                    print(f"{Cores.AZUL}Código atualizado com sucesso!{Cores.RESET}")
        self.salvar_dados()
        return
            
    def buscar_produto(self,codigo): #Exibe informações de um produto específico
        if codigo not in self.set_codigos:
            print(f"{Cores.VERMELHO}Código inválido!{Cores.RESET}")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==codigo:
                print(str(self.lista_dict_produtos[i]).replace("'","").replace("{","").replace("}",""))
    
    def excluir_produto(self,codigo): #Exclui um produto específico
        if codigo not in self.set_codigos:
            print(f"{Cores.VERMELHO}Código inválido!{Cores.RESET}")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==codigo:
                self.lista_dict_produtos.pop(i)
                self.set_codigos.remove(codigo)
                self.salvar_dados()
                print(f"{Cores.AZUL}Produto removido com sucesso!{Cores.RESET}")
                break
    
    def verificar_input(self,tipo,nome):
        while True:
            valor_str=input(f"Qual o valor para {nome} ?")
            try:
                valor=tipo(valor_str)
                return valor
            except ValueError:
                print("Inválido, por favor tente novamente!")
    
    def sair_sistema(self): #Encerra o programa (o mais difícil de se programar kkkkkkkk)
        print("Saindo...")
        return

#Daqui pra baixo é a interação com o usuário via Terminal.

class SistemaEstoqueCLI:
    
    def __init__(self):
        self.logica=ControleEstoque()
    
    def limpar_tela(self):
        sistema=platform.system()
        os.system('cls' if sistema=="Windows" else 'clear')
        
    def mostrar_menu(self):
        self.limpar_tela()
        print(f"{Cores.AZUL}{"="*50}{Cores.RESET}")
        print(f"{Cores.AMARELO} Sistema de Estoque {Cores.RESET}")
        print(f"{Cores.AZUL}{'='*50}{Cores.RESET}")
        print(f"{Cores.VERDE}[1]{Cores.RESET} Cadastrar produto")
        print(f"{Cores.VERDE}[2]{Cores.RESET} Listar Produtos")
        print(f"{Cores.VERDE}[3]{Cores.RESET} Buscar")
        print(f"{Cores.VERDE}[4]{Cores.RESET} Atualizar Produto ")
        print(f"{Cores.VERDE}[5]{Cores.RESET} Excluir")
        print(f"{Cores.VERDE}[6]{Cores.RESET} Buscar por nome")
        print(f"{Cores.VERDE}[7]{Cores.RESET} Listar por categoria")
        print(f"{Cores.VERDE}[8]{Cores.RESET} Mostrar estoque baixo")
        print(f"{Cores.VERDE}[9]{Cores.RESET} Sair")
                
    def iniciar(self):    
        while True:
            user=input("Bem-vindo ao sistema! Gostaria de usá-lo? (s/n)")
            if user.lower()!="s":
                print("Ok, obrigado por utilizar o sistema! Salvando e desligando...")
                self.logica.salvar_dados()
                return False
            else:
                self.mostrar_menu()
                opcao=self.logica.verificar_input(int,"as opções acima?")
                self.processar_opcao(opcao)
                 
    def processar_opcao(self,opcao):
        if opcao not in range(1,10):
            print("Por favor, selecione uma opção válida!")
            return True
        elif opcao==1:
            nome=self.logica.verificar_input(str,"nome")
            codigo=self.logica.verificar_input(int,"codigo")
            categoria=self.logica.verificar_input(str,"categoria")
            preco=self.logica.verificar_input(float,"preço")
            quantidade=self.logica.verificar_input(float,"quantidade")
            self.logica.cadastrar_produto(nome,codigo,categoria,preco,quantidade)
            return True
        elif opcao==2:
            self.logica.listar_produtos()
            return True
        elif opcao==3:
            codigo=self.logica.verificar_input(int,"codigo")
            self.logica.buscar_produto(codigo)
            return True
        elif opcao==4:
            codigo=self.logica.verificar_input(int,"codigo")
            campo=self.logica.verificar_input(str,"campo")
            campo=campo.lower()
            if campo in ["preço","estoque","codigo"]:
                novo_valor=self.logica.verificar_input(float,"campo")
            else:
                novo_valor=self.logica.verificar_input(str,"campo")
            self.logica.atualizar_produto(codigo,campo,novo_valor)
            return True
        elif opcao==5:
            codigo=self.logica.verificar_input(int,"codigo")
            self.logica.excluir_produto(codigo)
            return True
        elif opcao==6:
            nome=self.logica.verificar_input(str,"nome")
            self.logica.buscar_nome(nome)
            return True
        elif opcao==7:
            categoria=self.logica.verificar_input(str,"categoria")
            self.logica.listar_por_categoria(categoria)
            return True
        elif opcao==8:
            limite=self.logica.verificar_input(float,"limite")
            self.logica.mostrar_estoque_baixo(limite)
            return True
        else:
            print("Entendido! Saindo...")
            return False
TUI=SistemaEstoqueCLI()
TUI.iniciar()