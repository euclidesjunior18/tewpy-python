class Pro:
    
    def getIdOnArray(array, compar):
        cont = 0
        valor = 0
        for x in array:
            if x == compar:
                valor = cont
                break                
            else:
                valor = 99
            cont = cont + 1
        return(valor) #se retorna 0 signfica que não tem id pra atualizar
        
    
    def carregaUltIds(localArq): #retorna ultmos ids de tweet salvo no arquivo 
        arq = open(localArq, 'r')
        texto = arq.readlines()
        texto2 = []
        for linha in texto:
            limpa = linha.split(' \n')
            limpa = limpa[0]
            texto2.append(int(limpa))
        arq.close()
        return(texto2)
   
    def salvaUltIds(array, localArq):
        
        result = array 
        arq = open(localArq, 'w')
   
        texto = []
        for tweet in result:
            #print(f'SALVO ID: {tweet.id}')
            texto.append(tweet +' \n')
            
        arq.writelines(texto)
        print('escrito com sucesso')
        arq.close()