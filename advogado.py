class Advogado:
    def __init__(self,cod_oab,nome,processos):
        self._cod_oab = cod_oab
        self._nome = nome
        self._processos = processos

    #gets
    
    def get_cod_oab(self):
        return self._cod_oab

    def get_nome(self):
        return self._nome

    
    def get_processos(self):
        return self._processos 
    
    #sets
    
    
    def set_cod_oab(self,novo_cod):
        self._cod_oab = novo_cod


    def set_nome(self,novo_nome):
        self._nome = novo_nome

    def set_processos(self,novos_processos):
        self._processos = novos_processos          

    #metodos
    
    def lista_clientes(self):
        clientes = []
        for i in range(len(self._processos)):
            if self._processos[i]._pessoa not in clientes:
                    clientes.append(self._processos[i].get_pessoa()) 
        for i in range(len(clientes)):
            return(clientes[i])


    def __str__(self):
        return f'Nome: {self._nome}, codigo OAB: {self._cod_oab}'       