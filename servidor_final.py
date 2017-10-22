import socket
from os import system
import threading

def atende(obj_conexao, endereco): 
    dados = obj_conexao.recv(1024)
    dados = dados.split("\n")
    dados[0] = dados[0].replace('\r', '')
    dados = dados[0].split(' ') 
    print (dados)
    if dados[0] == 'GET':
        dados = dados[1]
        dados = dados[1:]
        print (dados)
        try:            
            f = open(dados,'r')
            obj_conexao.send('HTTP/1.1 200 OK\n\n')
            l = f.read(1024)
            while l:
                obj_conexao.send(l)
                l = f.read(1024)
        except IOError:
            obj_conexao.send('HTTP/1.1 404 Bad Request\n\n')
    else:
        obj_conexao.send('HTTP/1.1 501 Not implemented\n\n')
    obj_conexao.close()    
    
ip_server = "0.0.0.0"
porta_server = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_server, porta_server))
server.listen(5)
print "Escutando  %s : %d" % (ip_server, porta_server)

while True:
    obj_conexao, endereco = server.accept()
    print "Conectado por: ", endereco
    thread = threading.Thread(target=atende, args=(obj_conexao, endereco),)
    thread.run()
    
        
   