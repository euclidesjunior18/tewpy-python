print ('Importando TWEEPY')
import tweepy
print ('IMPORTADO COM SUCESSO')

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

print('AUTENTICANDO APLICACAO NO TWEETER...')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

print('AUTENTICADO COM SUCESSO..... BJS no core...')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
