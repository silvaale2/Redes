#!/usr/bin/env python
import random
import socket
import time
import threading
from os import system


def atende(obj_conexao, endereco): 
    dados = obj_conexao.recv(1024)
    dados = dados.split("\n")
    dados[0] = dados[0].replace('\r', '')
    dados = dados[0].split(' ') 
    print (dados[0])
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
    
ip_server = '0.0.0.0'
porta_server = 9001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_server, porta_server))
print 'Servidor escutando: ', ip_server, porta_server
server.listen(5)                 # Now wait for client connection.
#print 'Entering infinite loop; hit CTRL-C to exit'

while True:
    # Estabelecendo a conexao    
    c, (client_host, client_port) = server.accept()
    print 'Conectado com o cliente: ', client_host, client_port
    c.recv(1024) # should receive request from client. (GET ....)
    c.send('HTTP/1.0 200 OK\n')
    c.send('Content-Type: text/html\n')
    c.send('\n') # header and body should be separated by additional newline
    c.send("""
    <html>
    <body>
    <?
    if ($dir=opendir("/home/alexandre/"))
    $i=1;
    ?>  
    <a href="cliente_final.py">cliente_final.py</a><br>
    <a href="servidor_final.py">servidor_final.py</a><br>
    <a href="tp1.txt">tp1.txt</a><br>
    </body>
    </html>     
    """) 
    obj_conexao, endereco = server.accept()
    thread = threading.Thread(target=atende, args=(obj_conexao, endereco),)
    thread.run()

            
            
    

