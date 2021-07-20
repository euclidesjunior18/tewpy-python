from escreveArq import Manipula
from processoInt import Pro

user = '@Euc1ydes'
cami = 'arq/ultraX.txt'
ultidarq = 1

conta = 1
resp = []

while(conta >= 0):
    try:
        ret = Pro.carregaUltIds(cami)  
        if ultidarq == 1:
            ultidarq = ret[0]    
    except: 
        resp = Manipula.buscaUltIds(user, 1)   
        Pro.salvaUltIds(resp, cami)
        ret = Pro.carregaUltIds(cami)
    
    #print(ultidarq)
    try:
        ultid = Manipula.retornaUltId(user)
    except:
        ultid = ultidarq
    
    pos = int(Pro.getIdOnArray(ret, ultidarq))
    #print(ultid)
    if ultid > ultidarq:  
        if ultidarq == 1:
            resp = Manipula.buscaUltIds(user, 1)   #faz a requisição dos ultimos 99 tweets
            Pro.salvaUltIds(resp, cami) #salva  ultimos 99 tweets
            pos = 1
        else:
            pos = int(Pro.getIdOnArray(ret, ultidarq))
            resp = Manipula.buscaUltIds(user, ret[0])   #faz a requisição dos ultimos {pos} tweets
            Pro.salvaUltIds(resp, cami) #salva  ultimos {pos} tweets
            ret = Pro.carregaUltIds(cami)
            
        if pos < 99 or pos > 0:
            for x in ret:
                try:
                    print(f'laikando tuite ID: {x} - pos: {pos}')
                    Manipula.laikaPorId(x)         
                except:
                    print(f'laike tuite ID: {x} deu mierda')
        ultidarq = ultid

    print(f'ULTIMO ID: {ultid} - ID ARQ: {ultidarq} - vez= {conta}')
    conta += 1