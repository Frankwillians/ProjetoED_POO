class Custo:
    def __init__(self,data,descricao,valor):
        self._data = data
        self._descricao = descricao
        self._valor = valor
   
   #getters
    @property
    def data(self):
       return self._data

    @property
    def descricao(self):
        return self._descricao

    @property
    def valor(self):
        return self._valor

    #setters     
    
    @data.setter
    def data(self,nova_data):
        self._data = nova_data

    @descricao.setter
    def descricao(self,nova_desc):
        self._descricao = nova_desc

    @valor.setter
    def valor(self,novo_valor):
        self._valor = novo_valor       