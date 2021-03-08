class Processo:
    def __init__(self,descricao,custo,decisao,status,pessoa,advogado,audiencias):
        self._descricao = descricao
        self._custo = custo
        self._decisao = decisao
        self._status = status
        self._pessoa = pessoa
        self._advogado = advogado
        self._audiencias = audiencias
  
    
    
    #geters
    def get_decisao(self):
        if self._decisao == 'defer':
            return True
        elif self._decisao == 'indef':
            return False    
    
    def get_status(self):
        return self._status
    
    def get_pessoa(self):
        return self._pessoa

    def get_advogado(self):
        return self._advogado
    
    def get_audiencias(self):
        return self._audiencias  
    def get_custo(self):
        return self._custo               

    #setters
    def set_status(self,novo):
         self._status = novo

    def set_custo(self,novo):
        self._custo = novo  

    def set_audiencias(self,nova):
        self._audiencias = nova

    def set_decisao(self,novo):
        self._decisao = novo
    def set_advogado (self,novo):
        self._advogado = novo
    def set_pessoa(self,nova):
        self._pessoa = nova    

    #metodos 

    def audiencias_temp(self,tempo):
        for i in range (len(self._audiencias)):
            if self._audiencias[i].get_duracao() >= tempo:
                print(self._audiencias[i])
        return ''    

    def total_horas(self):
        total = 0
        for i in range(len(self._audiencias)):
            total += self._audiencias[i].get_duracao()
        return total    


    def __str__(self):
        return f'{self._descricao}'
            

