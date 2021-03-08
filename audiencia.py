class Audiencia:
    def __init__ (self,data,recomendacao,duracao):
        self._data = data
        self._recomendacao = recomendacao
        self._duracao = duracao
 
    #getters
    
    def get_data(self):
        return self._data
    
    def get_recomendacao(self):
        return self._recomendacao    
    
    def get_duracao(self):
        return self._duracao

   
    
    #setters

    def set_data(self,nova_data):
        self._data = nova_data
    

    def set_recomendacao(self,nova_recomendacao):
        self._recomendacao = nova_recomendacao    
    
    
    def set_duracao(self,nova_duracao):
        self._duracao = nova_duracao
    


    

    def __str__ (self):
        return f'realizada na data de: {self._data}, recomendação {self._recomendacao}, e teve duração de {self._duracao} min'        