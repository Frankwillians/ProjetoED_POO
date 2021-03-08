from audiencia import Audiencia
from advogado import Advogado
from custo import Custo
from pessoa import Pessoa 
from processo import Processo

proc_exec = []
proc_exec2 = []
lista_adv = []
lista_pess = []
proc_marcus = []
lista_time_pess1 = []
lista_time_pess2 = []
lista_geral = [ ]


#custos 

custo1 = Custo('21/09/21','roubo',2000)
custo2 = Custo('21/09/21','estelionato',5700)
custo3 = Custo('21/09/21','roubo de carro',750)

# pessoas: 
pess_1 = Pessoa('123.405.454-53','Carlos',proc_exec)
pess_2 = Pessoa('143.604.265-92','Maria',proc_exec2)


lista_pess.append(pess_1)
lista_pess.append(pess_2)

#advogados:
adv1 = Advogado('25698','Marcus',proc_marcus)
lista_adv.append(adv1)
proc_francis = []
adv2 = Advogado('29788','Francis',proc_francis)
lista_adv.append(adv2)
#lista de audiencias por processo
#processo 1 :
lista_aud = []

aud1 = Audiencia('27/08/2021','nenhuma',60)
aud2 = Audiencia('28/09/2021','nenhuma',90)
aud3 = Audiencia('25/12/2021','nenhuma',45)

lista_aud.append(aud1)
lista_aud.append(aud2)
lista_aud.append(aud3)

#processo 2:

lista_aud2 = []
aud4 = Audiencia('27/08/2021','nenhuma',90)
aud5 = Audiencia('28/09/2021','nenhuma',30)
lista_aud2.append(aud4)
lista_aud2.append(aud5)

#processo 3:
lista_aud3 = []
aud6 = Audiencia('27/08/2021','nenhuma',90)
aud7 = Audiencia('28/09/2021','nenhuma',30)
aud8 = Audiencia('28/09/2021','nenhuma',40)
lista_aud3.append(aud6)
lista_aud3.append(aud7)
lista_aud3.append(aud8)

#criação de processos:
#processo 1:
process_1 = Processo('roubo',custo1.valor,'indef','andamento',pess_1,adv1,lista_aud)
proc_exec.append(process_1)
proc_marcus.append(process_1)
lista_geral.append(process_1)
lista_time_pess1.append(process_1)

#setando no processo 1:
process_1.set_audiencias(lista_aud)



#processo 2:
process_2 = Processo('estelionato',custo2.valor,'defer','andamento',pess_1,adv1,lista_aud2)
proc_exec.append(process_2)
proc_marcus.append(process_2)
lista_geral.append(process_2)
lista_time_pess1.append(process_2)
#setando no processo 2:
process_2.set_audiencias(lista_aud2)


#processo 3:
process_3 = Processo('roubo de carro',custo3.valor,'defer','encerrada',pess_2,adv2,lista_aud3)
proc_exec2.append(process_3)
proc_francis.append(process_3)
lista_geral.append(process_3)
lista_time_pess2.append(process_3)
#setando no processo 3:
process_3.set_audiencias(lista_aud3)


#setando processos:
pess_1.set_processos(proc_exec)
pess_2.set_processos(proc_exec2)

#setando advogados: 
adv1.set_processos(proc_marcus)
adv2.set_processos(proc_francis)

while True:



    print('='*100)
    print('Pessoas cadastradas'.center(100))
    print('='*100)



    print(f''' 
                                (1) - para saber informações de Carlos
                                (2) - para saber informações de Maria
                                

    ''')

    pess = 0

    while pess != 1 and pess != 2:
        pess = int(input('digite: '))



    print('='*100)
    print('Menu Pessoal'.center(100))
    print('='*100)

    print(''' 
                                    (1) - pesquisar audiencias por tempo
                                    (2) - decisões deferidas e indeferidas
                                    (3) - total de custos pessoais
                                    (4) - total de minutos gastos em audiencias
                                    (5) - listar processos pessoais 
                                    (6) - para sair do menu pessoal
                                    
                                    
    ''')

    print('='*100)



    if pess == 1:

        code = 0
        while code != 6:
            print()
            code = int(input('digite a opção desejada: '))
            print()

            if code == 1:
                print('='*100)
                print(f'existem {len(proc_exec)} processos'.center(100))
                print('='*100)
                
                print(f'''

                                    (1) - para acessar o processo {proc_exec[0]}
                                    (2) - para acessar o processo {proc_exec[1]}
                ''')
                
                proc = int(input('digite: '))
            
                
                
                if proc == 1:
                    print()
                    tempo = int(input('digite o tempo em minutos: '))
                    print()
                    print('as audiencias localizadas foram: ')
                    print()
                    print(proc_exec[0].audiencias_temp(tempo))
               

                elif proc == 2:
                    tempo = int(input('digite o tempo em minutos: '))
                    print()
                    print('as audiencias localizadas foram: ')
                    print()
                    print(proc_exec[1].audiencias_temp(tempo))
              




            elif code == 2:
                print(f"a quantidade de processos deferidos foi de: {lista_pess[0].num_descisoes('True')}")
                print(f"a quantidade de processos indeferidos foi de: {lista_pess[0].num_descisoes('False')}")
                print()
                                

            elif code == 3:
                print()
                print(f'o custo total de processos desta pessoa é de: R${pess_1.custo_total():.2f}')
                print()    

            elif code == 4:
                
                print('='*100)
                print(f'existem {len(proc_exec)} processos'.center(100))
                print('='*100)
                
                print(f'''

                                    (1) - para acessar o processo {proc_exec[0]}
                                    (2) - para acessar o processo {proc_exec[1]}
                ''')
                
                proc = int(input('digite: '))
            
                
                
                if proc == 1:
                    
                    print()
                    print(f'As audiencias tiveram um tempo total de {lista_time_pess1[0].total_horas()} Minutos')
                    print()

                elif proc == 2:
                    print()
                    print(f'As audiencias tiveram um tempo total de {lista_time_pess1[1].total_horas()} Minutos')
                    print()
            
            elif code == 5:
                print('='*100)
                print(f'Processos de {pess_1}'.center(100))
                print('='*100)
                for i in range(len(lista_pess)):
                    print(f'{i+1} - {lista_pess[0].processos_cliente()[i]}'.center(100))
                    print('-'*100)
                print('='*100)
                
    if pess == 2:
        code = 0
        while code != 6:
            code = int(input('digite a opção desejada: '))
            print()
            if code == 1:
                tempo = int(input('digite o tempo em minutos: '))
                print()
                print('as audiencias localizadas foram: ')
                print()
                print(proc_exec2[0].audiencias_temp(tempo))


            elif code == 2:
                print(f"a quantidade de processos deferidos foi de: {lista_pess[1].num_descisoes('True')}")
                print(f"a quantidade de processos indeferidos foi de: {lista_pess[1].num_descisoes('False')}")
                print()
                                

            elif code == 3:
                print()
                print(f'o custo total de processos desta pessoa é de: R${pess_2.custo_total():.2f}')
                print()    

            elif code == 4:
                print(f'As audiencias tiveram um tempo total de {lista_time_pess2[0].total_horas()} Minutos')
                print()

            elif code == 5:
                print('='*100)
                print(f'Processos do {pess_2}'.center(100))
                print('='*100)
                for i in range(1):
                    print(f'{i+1} - {lista_pess[1].processos_cliente()[i]}'.center(100))
                    print('-'*100)
                print('='*100)



    adv_menu = ''
    while adv_menu != 'S' and adv_menu != 'N':
        adv_menu = input('deseja informações de advogados? [S/N]: ').upper()


    if adv_menu == 'S':

        print()
        print('='*100)
        print('Advogados disponiveis'.center(100))
        print('='*100)

        for i in range (len(lista_adv)):
            print(f'{lista_adv[i]}'.center(100))

        print('='*100)

        code = 0
        while code != 3:
            print('='*100)
            print('''
                                    (1) - ganhos totais do advogado
                                    (2) - listar os clientes do advogado
                                    (3) - para sair do menu de advogados
            ''')
            print('='*100)
            code = int(input('digite: ')) 
            print()
            if code == 1:
                cod_oab = input('digite o codigo oab do advogado que deseja consultar os ganhos totais: ')
                print()
                total = 0    
                for i in range(len(lista_pess)):
                    total += lista_pess[i].custo_total_adv(cod_oab)
                print(f'Os ganhos totais do advogado totalizam: R${total:.2f}') 
                print()

            elif code == 2:
                print()
                oabcd = input('digite o codigo oab para listagem dos clientes do advogado desejado: ')
                print()
                if oabcd == '25698':
                    print(adv1.lista_clientes())
                    print()
                elif oabcd == '29788':
                    print(adv2.lista_clientes())    
                    print()
    con =''
    while con != 'S' and con != 'N':
        con = input('Deseja continuar ? [S/N]: ').upper()
    if con == 'N':

        break
print('Programa Encerrado!')



