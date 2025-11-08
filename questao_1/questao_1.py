import json
import typing
import streamlit as st
import pandas as pd

class Cores:
    VERDE :str ='\033[92m' #streamlit 
    VERMELHO :str ='\033[91m'
    AMARELO :str ='\033[93m'
    AZUL :str ='\033[94m'
    RESET:str='\033[0m'
ProdutoDict=dict[str,str|float|int]
ListaEstoque=list[ProdutoDict]
class ControleEstoque:  #Aqui é a lógica do sistema em si
    """Sisteminha CRUD completinho 
    Todos os produtos devem estar em uma lista de dicionários,
        que possuem códigos, guardados em um set, e ter uma tupla com categorias"""
    lista_dict_produtos:ListaEstoque
    set_codigos:set[int]
    def __init__(self):
        self.lista_dict_produtos =[] #Cria uma lista vazia, toda vez que rodar, vai estar vazia
        self.set_codigos=set() #Cria um set vazio, ja que 2 produtos não possuem o mesmo código
        self.tupla_categorias :tuple[str,str,str,str] =("Alimento","Limpeza","Higiene","Outros") #Apenas as 4 categorias, nada de muito especial.
        self.carregar_dados()
    
    def carregar_dados(self) -> None: #Usa JSON
        try:
            with open("/home/alvaro/Códigos/mini-projeto/mini-projeto-python-alvaro-mariana/questao_1/estoque.json","r") as arquivo:
                dados_json : ListaEstoque =json.load(arquivo)
                self.lista_dict_produtos=dados_json
                for produto in self.lista_dict_produtos:
                    self.set_codigos.add(int(produto["Código"]))
        except FileNotFoundError:
            print(f"{Cores.VERMELHO}JSON de nome 'estoque.json' não encontrado!{Cores.RESET}")
            return
    
    def salvar_dados(self) -> None: #Também usa JSON
        with open("/home/alvaro/Códigos/mini-projeto/mini-projeto-python-alvaro-mariana/questao_1/estoque.json","w") as arquivo:
            json.dump(self.lista_dict_produtos,arquivo)
   
    def buscar_nome(self,nome : str) -> list|None:
        encontrados=[p for p in self.lista_dict_produtos if nome.lower() in str(p["Nome"]).lower()]
        if encontrados:
            return encontrados
        else:
            print(f"{Cores.VERMELHO}Não encontrado! Por favor, cheque novamente ou adicione!{Cores.RESET}")
        return 
   
    def listar_por_categoria(self,categoria : str) -> None:
        
        lista_categoria_temp=[p for p in self.lista_dict_produtos if str(p["Categoria"]).lower()== categoria.lower()]
        if lista_categoria_temp:
            for produto in lista_categoria_temp:
                print(json.dumps(produto, ensure_ascii=False, indent=2))
        else:
            print(f"Nenhum produto encontrado na categoria '{categoria}'!")
        return
   
    def mostrar_estoque_baixo(self,limite : float) -> None:
        encontrado=[p for p in self.lista_dict_produtos if int(p["Estoque"])<limite]
        if encontrado:
            for p in encontrado:
                print(json.dumps(p, ensure_ascii=False,indent=2))
        else:
            print("Nenhum encontrado.")
   
    def cadastrar_produto(self,nome:str,codigo:int,categoria:str,preco:float,quantidade:float) -> None :#Cria e add um produto novo
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
        produto : dict[str, typing.Any]={
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
    
   
    def listar_produtos(self) -> None: #Mostra todos os produtos em estoque
        for p in self.lista_dict_produtos:
            print(json.dumps(p,ensure_ascii=False,indent=2))
    
    def atualizar_produto(self,codigo:int,campo:str,novo_valor:str|int|float):
        if codigo not in self.set_codigos or campo.lower() not in ["nome","categoria","preço","estoque","codigo"]:
            print(f"{Cores.VERMELHO}Parâmetros inválidos!{Cores.RESET}")
            return
        if type(novo_valor) is str and len(novo_valor)<1:
            print(f"{Cores.VERMELHO}Por favor, insira um novo valor válido!{Cores.RESET}")
            return
        if (type(novo_valor) is float or type(novo_valor) is int) and novo_valor<0:
            print(f"{Cores.VERMELHO}Por favor, insira um valor numérico válido!{Cores.RESET}")
            return
        for i in range(len(self.lista_dict_produtos)):
            if int(self.lista_dict_produtos[i]["Código"])==codigo:
                if campo.lower()=="nome":
                    self.lista_dict_produtos[i]["Nome"]=str(novo_valor)
                    print(f"{Cores.AZUL}Nome atualizado com sucesso!{Cores.RESET}")
                if campo.lower()=="categoria":
                    (self.lista_dict_produtos[i]["Categoria"])=str(novo_valor)
                    print(f"{Cores.AZUL}Categoria atualizada com sucesso!{Cores.RESET}")
                if campo.lower()=="preço":
                    self.lista_dict_produtos[i]["Preço"]=(novo_valor)
                    print(f"{Cores.AZUL}Preço atualizado com sucesso!{Cores.RESET}")
                if campo.lower()=="estoque":
                    self.lista_dict_produtos[i]["Estoque"]=(novo_valor)
                    print(f"{Cores.AZUL}Estoque atualizado com sucesso!{Cores.RESET}")
                if campo.lower()=="codigo":
                    self.set_codigos.remove(codigo)
                    self.lista_dict_produtos[i]["Código"]=(novo_valor)
                    self.set_codigos.add(int(novo_valor))
                    print(f"{Cores.AZUL}Código atualizado com sucesso!{Cores.RESET}")
        self.salvar_dados()
        return
            
    def buscar_produto(self,codigo:int): #Exibe informações de um produto específico
        if codigo not in self.set_codigos:
            print(f"{Cores.VERMELHO}Código inválido!{Cores.RESET}")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==str(codigo):
                print(str(self.lista_dict_produtos[i]).replace("'","").replace("{","").replace("}",""))
    
    def excluir_produto(self,codigo:int): #Exclui um produto específico
        if codigo not in self.set_codigos:
            print(f"{Cores.VERMELHO}Código inválido!{Cores.RESET}")
            return
        for i in range(len(self.lista_dict_produtos)):
            if self.lista_dict_produtos[i]["Código"]==str(codigo):
                _=self.lista_dict_produtos.pop(i)
                self.set_codigos.remove(codigo)
                self.salvar_dados()
                print(f"{Cores.AZUL}Produto removido com sucesso!{Cores.RESET}")
                break
    
    def verificar_input(self,tipo:type[typing.Any] ,nome:str|float|int) -> typing.Any:
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

class FrontEnd():
    def __init__(self) -> None:
        self.estoque=ControleEstoque()
        self.produtos=self.estoque.lista_dict_produtos
    def renderizar_menu_lateral(self):
        with st.sidebar:
            st.header("Selecione a ação")
            opcao_selecionada=st.radio("Navegação",["Home(Listagem)","Cadastrar Produto","Buscar Produto","Atualizar Produto","Excluir Produto"])
            return opcao_selecionada
            
    def renderizar_cadastro(self) -> None:
        st.markdown("Cadastro de Novo Produto")
        with st.form("form_cadastro"):
            col1,col2=st.columns(2)
            with col1:
                nome=st.text_input("Nome do Produto", max_chars=100)
            with col2:
                codigo=st.number_input("Código (ID)", min_value=1, step=1)
            caregoria=st.selectbox("Categoria", self.estoque.tupla_categorias)
            col3,col4=st.columns(2)
            with col3:
                preco=st.number_input("Preço (R$)", min_value=0.01, format="%.2f")
            with col4:
                quantidade=st.number_input("Quantidade em estoque", min_value=0.0,format="%.2f")
            clique_salvar=st.form_submit_button("Cadastrar e Salvar", use_container_width=True)
            if clique_salvar:
                try:
                    self.estoque.atualizar_produto(
                        codigo=int(codigo),
                        campo=tipo_de_dado.lower(),
                        novo_valor=novo_valor
                    )
                    st.success(f"Produto {codigo} atualizado com sucesso! Novo {tipo_de_dado}: {novo_valor}")
                except Exception as e:
                    st.error(f"Falha na atualização: {e}")
        return
    
    def renderizar_atualizar(self) -> None:
        st.markdown("Atualização de Produto")
        tipo_de_dado=st.selectbox(
            "Tipo de dado",
            ("Código","Nome","Categoria","Preço","Estoque"),
            key="upd_campo_select"
        )
        novo_valor=None
        with st.form("form_atualizar"):
            codigo=st.number_input("Código (ID)", min_value=1,step=1)
            st.markdown(f"Novo valor para {tipo_de_dado}.")
                
            if tipo_de_dado in ["Preço","Estoque"]:
                novo_valor=st.number_input("Qual seria o novo valor?",min_value=0,key="upd_valor_num")
            elif tipo_de_dado=="Código":
                novo_valor=st.number_input("Qual seria o novo valor?",min_value=1,key="upd_valor_cod")
            elif tipo_de_dado=="Nome" or tipo_de_dado=="Categoria":
                novo_valor=st.text_input("Qual seria o novo valor?",max_chars=100,key="upd_valor_str")
            clique_salvar=st.form_submit_button("Atualizar e Salvar",use_container_width=True)
            if clique_salvar:
                if novo_valor is None:
                    st.error("Erro! Por favor, insira o novo valor corretamente!")
                    return
                try:
                    self.estoque.atualizar_produto(
                        codigo=int(codigo),
                        campo=tipo_de_dado.lower(),
                        novo_valor=novo_valor
                    )
                    st.success(f"Produto {codigo} atualizado com sucesso! Novo {tipo_de_dado}: {novo_valor}")
                except Exception as e:
                    st.error(f"Falha na atualização: {e}")
        return 
    def renderizar_buscar(self) -> None:
        st.markdown("Rendeirização de produto")

        tipo_busca=st.selectbox("Tipo de busca",("Nome","Tipo","Estoque Baixo"))
        if tipo_busca=="Nome":
            busca=st.text_input("Qual seria o nome?",max_chars=100)
            try:
                st.dataframe(
                    self.estoque.buscar_nome(busca),
                    use_container_width=True,
                    hide_index=True
                )
            except Exception as e:
                st.error(f"Falha na busca: {e}")
                
        
            
        
    def rodar(self):
        opcao=self.renderizar_menu_lateral()
        if opcao=="Cadastrar Produto":
            self.renderizar_cadastro()
        elif opcao=="Home(Listagem)":
            st.title("Visão Geral do Estoque")
        elif opcao=="Atualizar Produto":
            self.renderizar_atualizar()
        elif opcao=="Buscar Produto":
            self.renderizar_buscar()
        else:
            st.info("Ainda em construção...")
        
if __name__=='__main__':
    app=FrontEnd()
    app.rodar()