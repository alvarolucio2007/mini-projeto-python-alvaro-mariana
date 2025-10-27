class Sistema():
    def __init__(self,dicio_itens):
        self.dicio_itens=dicio_itens
    def exibir_itens(self):
        print(self.dicio_itens)
    def procurar_itens(self,item):
        if item in self.dicio_itens.keys():
           print(f"O item {item} está em estoque, com {self.dicio_itens[item]}")
        else:
            print(f"O item {item} não está em estoque.")
    def atualizar_itens(self,item):
        if item in self.dicio_itens.keys():
            
            
        