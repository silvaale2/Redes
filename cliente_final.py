from socket import *
import sys

serverHost = 'localhost'
serverPort = 80
url = sys.argv[1]
if len(sys.argv) > 2:
    serverPort = int(sys.argv[2])
serverArq= sys.argv[1]
server= sys.argv[0]
print (server, serverArq, serverPort)

cliente = socket(AF_INET, SOCK_STREAM)
#cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ip = gethostbyname(serverArq)
#ip = ip.replace("","")
#print (ip, serverPort)
cliente.connect((serverHost, serverPort)) 
msg = 'GET /' + ' HTTP/1.1\n\n'
print (msg)
cliente.send(msg)
dados = cliente.recv(1024)
#print (dados)
x = dados
while dados:
    dados = cliente.recv(1024)
    x = x + dados
z = x.find('\n')
resposta = x[:z] 
resposta = resposta.split(' ') 
print (resposta)

if resposta[2] == 'OK' and resposta[1] == '200':
    z = x.find('\n\n')
    x = x[z+2:]
    f = open(' ','w')    
    f.write(x)
    f.close()
else:
    print 'Arquivo nao existe'
cliente.close()
