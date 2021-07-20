class Manipula:

    def autent():
        import tweepy
        #print ('IMPORTADO COM SUCESSO')

        consumer_key = ''
        consumer_secret = ''

        access_token = ''
        access_token_secret = ''

        #print('AUTENTICANDO APLICACAO NO TWEETER...')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        #print('AUTENTICADO COM SUCESSO..... BJS no core...')
        api = tweepy.API(auth)
        return(api)
        
    def salvaUltIds2(userId, localArq, ultIdT):
    #salva os ultmos 20 ids de tweet do usuário
        api = Manipula.autent()
        
        result = api.user_timeline(id=userId, since_id=ultIdT, count=99) 
        arq = open(localArq, 'w')
   
        texto = []
        for tweet in result:
            print(f'SALVO ID: {tweet.id}')
            texto.append(str(tweet.id)+'\n')

        arq.writelines(texto)
        print('escrito com sucesso')
        arq.close()
        
    def laikaPorId(id):
        api = Manipula.autent()
        api.create_favorite(id) 
        print (f'like ID: {id} com sucesso!><><><><')

    def unlaikaPorId(id):
        api = Manipula.autent()
        api.destroy_favorite(id) 
        print (f'unlike ID: {id} com sucesso! <><><>')
    
    def retornaUltId(userId):
        ids = []
        try:
            api = Manipula.autent()
            result = api.user_timeline(id=userId, count=1)
            for tweet in result:
                ids.append(tweet.id)            
        except: 
            print('ERRO AO BUSCAR ULT ID... tentando novamente...')
        return(ids[0])
        
    def buscaUltIds(userId, ultIdT):#retorna os ultimos ids de tweet do usuário
        api = Manipula.autent()
        texto = []
        try:
            result = api.user_timeline(id=userId, since_id=ultIdT, count=99)   
            for tweet in result:
                print(f'ENCONTRADO ID: {tweet.id}')
                texto.append(str(tweet.id))
            print('- SALVO NO ARRAY -')
        except:
            print('-XxX- ERRRO AO BUSCAR IDS, FAZENDO NOVA TENTATIVA....')
        return(texto)
        
    def enviaMsg(userId, msg):
        try:
            api = Manipula.autent()
            api.send_direct_message(userId, msg)
            print(' - XxX - MSG ENVIADA - XxX -')
        except:
            print('Erro ao enviar msg XXXX')
    