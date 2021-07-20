from escreveArq import Manipula
from processoInt import Pro

print('INSIRA O ID DO USUARIO')
#user = ''
user = input()
cami = 'arq/ultraX.txt'

resp = Manipula.buscaUltIds(user, 1)  