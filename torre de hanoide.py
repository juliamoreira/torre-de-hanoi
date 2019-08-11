discos = int (input("Informe o numero de discos: "))        #pede o numero de discos                #gera lista com o numero de discos
haste = '|'     
torre1 = [haste * i for i in range(1, discos * 2,  2)]      #printa cada disco com o numero primo seguinte a ele, exceto 1
torre2 = ['' * i for i in range(1, discos * 2,  2)]  #torres vazias
torre3 = torre2[:]  
horizontal = "_"
d_size = 0    
torres = [torre1,torre2,torre3]     #conjunto pra acessar todas as torres
jogadas = 0   #contabiliza jogadas

def print_torres(torre1, torre2, torre3, d_size):   #mostra as torres
    ls = d_size * 2 + 2 
    for line in zip(torre1, torre2, torre3): #faz uma lista de tuplas com o zip pras torres
        l , c, r = line
        print('|%s|%s|%s|' % (l.center(ls), c.center(ls), r.center(ls)))         #mostras as filas e centraliza
    print(('-' * (d_size * 2 + 2 )).center(ls + 1) * 3)   #printa a base da torre de acordo com o tamanho das torres 

def imprecise():                                                                                       #funcao para informar quando a jogada é invalida e a requerir novamente
    mommytorre = int (input ("Informe a torre do qual se origina o disco a ser movido: "))-1               #pede a torre de origem
    finaltorre = int (input("Informe a torre na qual sera posto o disco : "))-1                            #pede o torre destinataria
    return (mommytorre, finaltorre)                                                                     #altera os valores
 
def checa_jogadas(mommytorre, finaltorre):
    if mommytorre not in [0, 1, 2] or finaltorre not in [0, 1, 2]:          #ve se o input é valido
        return False
    elif torres[mommytorre] == []:    #checa se a torre de origem esta vazi
        return False
    else:
        origem = [item for item in torres[mommytorre] if '|' in item]   #cria uma lista pra checar a quant de pipes da torre de origem
        destino = [item for item in torres[finaltorre] if '|' in item]   #cria uma lista pra checar a quant de pipes da torre de destino
        if (len(origem) == 0) or (len(destino) > 0    #caso a torre de origem estiver vazia OU o tamanho do destino é maior que 
            and origem[0].count('|') > destino[0].count('|')):  #e tambem se o  disco é maior que o ultimo disco da torre de destino 
            return False
    return True  #caso nao houver nenhuma das inconformidades listadas, realizara a jogada
        
def winner():
      if torre3 == [haste * i for i in range(1, discos * 2,  2)]: #confere se houve ganhador
        print ("Parabéns!! O jogo foi concluído com êxito!")            #invalida playing
        return True

def move(mommytorre, finaltorre):                                 #realiza as jogadas
    global jogadas    #contabiliza jogadas
    to = torres[mommytorre] #to acessara a lista de torres no indice de mommytorre(input)
    td = torres[finaltorre]   #td acessara a lista de torres no indice de finaltorre(input)
    origem = [item for item in to if '|' in item][0]  #cria uma lista com todos os pipes e acessa o primeiro elemento dela 
    destino = [item for item in td if item != '']    #cria uma lista com todos os pipes
    if (len(destino) == 0): #caso nao houver pipes, o ultimo elemento da torre de destino recebe o ultimo elemento de mommytorre 
        td[-1] = origem
    else:
        td[td.index(destino[0]) -1] = origem     #retira o elemento da mommy torre e o insere na finaltorre
    to[to.index(origem)] = ''
    jogadas +=1                                                 #contabiliza a jogada

def playing():                                  #definicao do jogo todo
    while not winner():
        print_torres(torre1, torre2, torre3, discos)   #mostra o tab 
        valores = imprecise()  #valores sera definido por imprecise, que sao os inputs
        if checa_jogadas(valores[0], valores[1]):  #chama a funcao checa jogadas para conferir os inputs
            move(valores[0], valores[1])    #move com a funcao do mesmo nome
            print (jogadas, "jogadas realizadas")
        else:
            print ("Jogada imprecisa!!Por favor, reveja seu movimento <3")   #requer novamente caso valor for invalido


playing()  #chama a funcao do jogo
