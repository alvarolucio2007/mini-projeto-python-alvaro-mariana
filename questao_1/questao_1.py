import json
import typing
import streamlit as st
import pandas as pd
import os

ProdutoDict=dict[str,str|float|int]
HistoricoDocumentacao=dict[str,str|float]
ListaMovimentacao=list[HistoricoDocumentacao]
ListaEstoque=list[ProdutoDict]
class ControleEstoque:  #Aqui é a lógica do sistema em si
    #
    """Sisteminha CRUD completinho 
    Todos os produtos devem estar em uma lista de dicionários,
        que possuem códigos, guardados em um set, e ter uma tupla com categorias"""
    lista_dict_produtos:ListaEstoque
    lista_movimentacoes:ListaMovimentacao
    set_codigos:set[int]
    JSON_PATH=os.path.join(os.getcwd(),"estoque.json")
    def __init__(self):
        self.lista_dict_produtos =[] #Cria uma lista vazia, toda vez que rodar, vai estar vazia
        self.set_codigos=set() #Cria um set vazio, ja que 2 produtos não possuem o mesmo código
        self.tupla_categorias :tuple[str,str,str,str] =("Alimento","Limpeza","Higiene","Outros") #Apenas as 4 categorias, nada de muito especial.
        self.lista_movimentacoes=[]
        self.carregar_dados()
    
    def carregar_dados(self) -> None: #Usa JSON
        if not os.path.exists(self.JSON_PATH):
            with open(self.JSON_PATH,"w") as f:
                json.dump([],f)
            self.lista_dict_produtos=[]
        try:
            with open(self.JSON_PATH,"r") as arquivo:
                try:
                    dados_json:ListaEstoque=json.load(arquivo)
                    self.lista_dict_produtos=dados_json
                    for produto in self.lista_dict_produtos:
                        produto["Código"]=int(produto["Código"])
                        produto["Preço"]=float(produto["Preço"])
                        produto["Estoque"]=float(produto["Estoque"])
                        self.set_codigos.add(int(produto["Código"]))
                except json.JSONDecodeError:
                    self.lista_dict_produtos=[]
                    self.salvar_dados()
                    pass
        except FileNotFoundError:
            with open(self.JSON_PATH,"w") as f:
                json.dump([],f)
            self.lista_dict_produtos=[]
            return False
        return
    
    def salvar_dados(self) -> None: #Também usa JSON
        with open(self.JSON_PATH,"w") as arquivo:
            json.dump(self.lista_dict_produtos,arquivo)
   
    def buscar_nome(self,nome : str) -> list|Exception:
        encontrados=[p for p in self.lista_dict_produtos if nome.lower() in str(p["Nome"]).lower()]
        if encontrados:
            return encontrados
        else:
            raise ValueError("Nenhum produto encontrado!")
   
    def listar_por_categoria(self,categoria : str) -> list:
        lista_categoria_temp=[p for p in self.lista_dict_produtos if str(p["Categoria"]).lower()== categoria.lower()]
        return lista_categoria_temp
   
    def mostrar_estoque_baixo(self,limite : float) -> list:
        encontrado=[p for p in self.lista_dict_produtos if int(p["Estoque"])<limite]
        return encontrado
   
    def cadastrar_produto(self,nome:str,codigo:int,categoria:str,preco:float,quantidade:float) -> None :#Cria e add um produto novo
        if codigo in self.set_codigos:
            raise ValueError("Código já existente!")
        if categoria not in self.tupla_categorias:
            raise ValueError(f"Categoria inexistente! Categorias possíveis: {self.tupla_categorias}")
        if len(nome)<1:
            raise ValueError("Nome não pode estar vazio!")
        if preco<0:
            raise ValueError("Preço não pode ser negativo!")
        if quantidade<0:
            raise ValueError("Quantidade não pode ser negativa!")
        produto : dict[str, typing.Any]={
            "Código":int(codigo),
            "Nome":str(nome),
            "Categoria":str(categoria),
            "Preço":float(preco),
            "Estoque":float(quantidade) #
        }
        self.lista_dict_produtos.append(produto)
        self.set_codigos.add(codigo)
        self.salvar_dados()
        
    def atualizar_produto(self,codigo:int,campo:str,novo_valor:str|int|float):
        if codigo not in self.set_codigos or campo.lower() not in ["nome","categoria","preço","estoque","codigo"]:
            raise ValueError("Parâmetros inválidos!")
        if type(novo_valor) is str and len(novo_valor)<1:
            raise ValueError("Por favor, insira um novo valor válido!")
        if (type(novo_valor) is float or type(novo_valor) is int) and novo_valor<0:
            raise ValueError("Por favor, insira um valor numérico válido!")
        for i in range(len(self.lista_dict_produtos)):
            if int(self.lista_dict_produtos[i]["Código"])==codigo:
                if campo.lower()=="nome":
                    self.lista_dict_produtos[i]["Nome"]=str(novo_valor)

                elif campo.lower()=="categoria":
                    (self.lista_dict_produtos[i]["Categoria"])=str(novo_valor)

                elif campo.lower()=="preço":
                    self.lista_dict_produtos[i]["Preço"]=float(novo_valor)

                elif campo.lower()=="estoque":
                    self.lista_dict_produtos[i]["Estoque"]=float(novo_valor)

                elif campo.lower()=="codigo":
                    self.set_codigos.remove(codigo)
                    self.lista_dict_produtos[i]["Código"]=int(novo_valor)
                    self.set_codigos.add(int(novo_valor))
                break
        self.salvar_dados()
        return
            
    def buscar_produto(self,codigo:int): #Exibe informações de um produto específico
        if codigo not in self.set_codigos:
            raise ValueError("Código não encontrado!")
        for produto in self.lista_dict_produtos:
            if int(produto["Código"])==codigo:
                return produto
    
    def excluir_produto(self,codigo:int) -> None: #Exclui um produto específico
        if codigo not in self.set_codigos:
            raise ValueError(f"Código {codigo} não encontrado!")
        for i in range(len(self.lista_dict_produtos)):
            if int(self.lista_dict_produtos[i]["Código"])==(codigo):
                _=self.lista_dict_produtos.pop(i)
                self.set_codigos.remove(codigo)
                self.salvar_dados()
                break
        return
    
    def movimentar_produto(self,data:str,produto:str,tipo:str,quantidade:float)->None:
        if self.buscar_nome(produto):
            self.lista_movimentacoes.append({
                "data":data,
                "produto":produto,
                "tipo":tipo,
                "qnt":quantidade
            })
            
            
        

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
            categoria=st.selectbox("Categoria", self.estoque.tupla_categorias)
            col3,col4=st.columns(2)
            with col3:
                preco=st.number_input("Preço (R$)", min_value=0.01, format="%.2f")
            with col4:
                quantidade=st.number_input("Quantidade em estoque", min_value=0.0,format="%.2f")
            clique_salvar=st.form_submit_button("Cadastrar e Salvar", width='stretch')
            if clique_salvar:
                try:
                    self.estoque.cadastrar_produto(
                        nome=nome,
                        codigo=int(codigo),
                        categoria=categoria,
                        preco=float(preco),
                        quantidade=float(quantidade)
                    )
                    st.rerun()
                    st.success(f"Produto {codigo} adicionado com sucesso (Código: {codigo})")
                except Exception as e:
                    st.error(f"Falha no cadastro! Verifique se o código já existe. Código de erro: {e}")
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
            clique_salvar=st.form_submit_button("Atualizar e Salvar",width='stretch')
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
                    st.rerun()
                except Exception as e:
                    st.error(f"Falha na atualização: {e}")
        return 
    def renderizar_buscar(self) -> None:
        st.markdown("Busca de produto")
        tipo_busca=st.selectbox("Tipo de busca",("Nome","Categoria","Estoque Baixo"))
        if tipo_busca=="Nome":
            busca=st.text_input("Qual seria o nome?",max_chars=100)
            if busca:
                resultados=self.estoque.buscar_nome(busca)
                df_resultados=pd.DataFrame(resultados)
                if not df_resultados.empty:
                    st.success(f"Encontrado(s) {len(df_resultados)} produto(s).")
                    st.dataframe(df_resultados,width='stretch',hide_index=True)
                else:
                    st.warning(f"Nenhum produto encontrado com o nome '{busca}'")
        elif tipo_busca=="Categoria":
            busca=st.selectbox("Categoria",self.estoque.tupla_categorias)
            resultados=self.estoque.listar_por_categoria(busca)
            df_resultados=pd.DataFrame(resultados)
            if not df_resultados.empty:
                st.success(f"Encontado(s) {len(df_resultados)} produto(s).")
                st.dataframe(df_resultados,width='stretch',hide_index=True)
        else:
            busca=st.number_input("Qual seria o limite?",min_value=0,step=1)
            resultados=self.estoque.mostrar_estoque_baixo(busca)
            df_resultados=pd.DataFrame(resultados)
            if not df_resultados.empty:
                st.warning(f"{len(df_resultados)} produto(s) estão abaixo do limite!")
                st.dataframe(df_resultados,width='stretch',hide_index=True)
            else:
                st.success("Todos os produtos estão acima do limite de estoque!")  
        return
    def renderizar_excluir(self) -> None:
        st.markdown("Excluir Produto")
        st.warning("Esta ação é permanente e não pode ser desfeita.")
        if 'codigo_excluir' not in st.session_state:
            st.session_state.codigo_excluir=None
        with st.form("form_exclusao_busca"):
            codigo_excluir_input=st.number_input("Insira o código (ID) do produto a ser excluído:",min_value=1,step=1,key="codigo_excluir_input_widget")
            
            clique_buscar=st.form_submit_button("Buscar Produto para Exclusão",width='stretch')
            if clique_buscar:
                st.session_state.codigo_excluir=int(codigo_excluir_input)
                st.rerun()
        
        codigo_excluir=st.session_state.codigo_excluir
            
        if codigo_excluir and codigo_excluir in self.estoque.set_codigos:
            nome_produto=next(
                    (p["Nome"] for p in self.estoque.lista_dict_produtos if int(p["Código"]) == int(codigo_excluir)),
                    "Produto Desconhecido")
            st.error(f"Você está prestes a excluir o produto: {nome_produto} (Código: {int(codigo_excluir)})")
            clique_excluir=st.button("CONFIRMAR EXCLUSÃO",width='stretch')
            if clique_excluir:
                try:
                    self.estoque.excluir_produto(int(codigo_excluir))
                    st.success(f"Produto {nome_produto} excluido com sucesso! ")
                    st.rerun()
                except Exception as e:
                    st.error(f"Falha na exclusão. Erro:{e}")
        elif codigo_excluir is not None and codigo_excluir not in self.estoque.set_codigos:
            st.info(f"Nenhum produto encontrado com o código {int(codigo_excluir)}")
            st.session_state.codigo_excluir=None
        elif codigo_excluir is None:
            st.info("Digite um código e clique em buscar!")
        return
    def renderizar_movimentacao(self) -> None:
        st.markdown("Registrar Movimentação de Produto")
        with st.form("form_movimentar"):
            st.text_input("Qual o nome do produto?")
            
            st.form_submit_button("Cadastrar Movimentação de Item!")
            
        
    def renderizar_home(self):
        st.title("Visão Geral do Estoque")
        st.info({self.estoque.JSON_PATH})
        try:
            st.dataframe(
                self.estoque.lista_dict_produtos,
                width='stretch',
                hide_index=True
            )
        except Exception as e:
            print(f"Erro! {e}")
        
            
    def rodar(self):
        opcao=self.renderizar_menu_lateral()
        if opcao=="Cadastrar Produto":
            self.renderizar_cadastro()
        elif opcao=="Home(Listagem)":
            self.renderizar_home()
        elif opcao=="Atualizar Produto":
            self.renderizar_atualizar()
        elif opcao=="Buscar Produto":
            self.renderizar_buscar()
        elif opcao=="Excluir Produto":
            self.renderizar_excluir()
        #elif opcao=="Movimentar Produto":
         #   self.renderizar_movimentacao()
        else:
            st.info("Ainda em construção...")
        
if __name__=='__main__':
    app=FrontEnd()
    app.rodar()
