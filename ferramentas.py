#-*-coding:utf8;-*-
#qpy:console
import os
import socket
import time 
import datetime
import pip
print('bem_vindo ao robodroid')
print('carregando...')
time.sleep(3)
print('•••'*10)
print('vamos começar')
print('•••'*10)
while True:
    print(''''[hora]-ver hora atual
[date]-data atual
[modulo]-baixar biblioteca py
[whois]-informaçoes do sites
[tabuada]-entra na tabuada
[portas]-ver portas aberta de ip
[ip]-para ver ip do site
[meu-ip]-mostra seu ip interno
[desligar]-sair do programa  ''')
    time.sleep(4)
    os.system('clear')
    os.system('pwd')
    print('==='*10)
    resposta=input('o que dejesa: ')
    print('==='*10)
    if resposta == 'hora':
       curr_time = time.localtime() 
       curr_clock = time.strftime("%H:%M:%S", curr_time)
       print(curr_clock)
       print('==='*10)
    if resposta == 'date':
       x= datetime.datetime.now()
       print(x.year)
       print(x.strftime("%A"))
       print('==='*10)
    if resposta == 'modulo':
       ferramenta = input('nome da ferramenta: ')
       pip.main(['install',ferramenta])
    if resposta == 'whois':
        dominio=input('example.com: ')
        whoisData = whois.whois(dominio)
        print(whoisData.text)
    if resposta == 'tabuada':
       tabuada=int(input("Tabuada do numero: ")) 
       for count in range(10):
           print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )
    if resposta == 'portas':
        alvo = input('Digite o IP: ')
        number=int(input('ate que porta: '))
        for porta in range(1, number):
            client = socket.socket()
            client.settimeout(0.05) 
            if client.connect_ex((alvo, porta)) == 0:
                print('•••'*10)
                print('scaneando...')
                print('•••'*10)
                print('Porta Aberta ==>', porta)
                print('•••'*10)
                time.sleep(10)
    if resposta == 'ip':
        site = input('nome do site .com: ')
        addr1 = socket.gethostbyname(site)
        print('==='*10) 
        print(addr1)
        print('==='*10)
        time.sleep(10)
    if resposta == 'desligar':
       print('desligado')
       break
    elif resposta == 'meu-ip':
       ip_local = socket.gethostbyname(socket.gethostname()) 
       print(f'IP Local: {ip_local}')
       time.sleep(10)
