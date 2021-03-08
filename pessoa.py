class Pessoa:
    def __init__(self, cpf, nome, processos = []):
        self._cpf = cpf
        self._nome = nome
        self._processos = processos

        
   #getters
       

    
    def get_cpf(self):
       return self._cpf
    
    def get_nome(self):
        return self._nome
    
    def get_processos(self):
        return self._processos
    
    #setters

    
    def set_cpf(self,novo_cpf):
       self._cpf = novo_cpf
    
    def set_nome(self,novo_nome):
        self._nome = novo_nome
    
  
    def set_processos(self,novos_processos):
        self._processos = novos_processos       

    
    #metodos 

    def num_descisoes(self,dec):
        if dec == 'True':
            defer = 0
            for i in range(len(self._processos)):
                if self._processos[i].get_decisao() == True:
                    defer += 1
            return defer
        elif dec == 'False':
            indef = 0
            for i in range(len(self._processos)):
                if self._processos[i].get_decisao() == False:
                    indef += 1             
            return indef

    def custo_total(self):
        custo = 0
        for i in range(len(self._processos)):
            custo += self._processos[i].get_custo()
        return custo    

    def custo_total_adv(self,cod_oab):
        adv_custo = 0
        for i in range (len(self._processos)):
            if self._processos[i]._advogado._cod_oab == cod_oab:
                adv_custo += self._processos[i].get_custo()
                
        return adv_custo 
    
    def processos_cliente(self):
       lista = []
       for i in range(len(self._processos)):
           lista.append(self._processos[i])
       return lista

  


    def __str__(self):
        return f'Cliente: {self._nome}, de CPF: {self._cpf}'