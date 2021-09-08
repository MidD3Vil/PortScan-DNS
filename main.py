## Tabela de cores ANSI (Python) ##

# fonte #
Mblack = '\033[1;30m'   # Preto
Ired = '\033[1;31m'     # Vermelho
Dgreen = '\033[1;32m'   # Verde
Nyellow = '\033[1;33m'  # Amarelo
Iblue = '\033[1;34m'    # Azul
Gpurple = '\033[1;35m'  # Roxo
Hcyan = '\033[1;36m'    # Ciano
Twhite = '\033[1;37m'   # Branco
VRCRM = '\033[0;0m'     # Remover

from requests import get
import socket
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()

'''try:
    os.system('chmod 755 main.py')
except:
    print('Falha ao executar... Try: "chmod 755 main.py"')
    exit()'''

restart = 'S'
while restart == 'S':
    print(f'''{Ired}┏━━━━━━━━━━━━━━━━━━━━━━┓
┃ {Nyellow}[{Iblue} PORT SCANNER 2.0 {Nyellow}]{Ired} ┃
┃                      ┃                     
┣┫{Nyellow}[01]{Dgreen} Port Scanner{Ired}    ┃
┃                      ┃                    
┣┫{Nyellow}[02]{Dgreen} DNS Resolver{Ired}    ┃
┗━━━━━━━━━━━━━━━━━━━━━━┛''')
    print(f'{Twhite}>>> Tool by: Dr Midnight <<<')

    opc = str(input(f'\033[7mDigite a opção que deseja:{VRCRM} ')).strip()

    if opc == '1' or opc == '01' or opc == 'Port Scanner':
        clear()
        print(f'\n{Ired}########## #################### ##########')
        print(f'########## ### {Iblue}Port Scanner {Ired}### ##########')
        print('########## #################### ##########')
        print('{:^50}'.format(f'{Twhite}>>>>>>>>>> Tool by: Dr Midnight <<<<<<<<<<'))
        while True:
            alvo = input(f'\n\033[7m{Twhite}Digite o IP/Domínio:{VRCRM} ').strip()
            if len(alvo) > 13 or len(alvo) < 10:
                print(f'{Ired}!!! {Nyellow}IP Inválido {Ired}!!!')
            else:
                break
        print(f'\n{Nyellow}Scanning Started... Please wait')
        print(f'{Ired}Ctrl+C to interrupt the program\n')
        for port in range(65535):
            client = socket.socket()
            client.settimeout(0.05)
            if client.connect_ex((alvo, port)) == 0:
                if port == 21:
                    print(f'{Nyellow}Port {port}  {Dgreen}...Open(FTP / 21)')
                elif port == 80:
                    print(f'{Nyellow}Port {port}  {Dgreen}...Open(http / 80)')
                elif port == 443:
                    print(f'{Nyellow}Port {port}  {Dgreen}...Open(https / 443)')
                else:
                    print(f'{Nyellow}Port {port}  {Dgreen}...Open')
        restart = str(input(f'\n{Twhite}\033[7mDeseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
        clear()
    elif opc == '2' or opc == '02' or opc == 'DNS Resolver':
        clear()
        print(f'\n{Ired}########## #################### ##########')
        print(f'########## ### {Iblue}DNS Resolver {Ired}### ##########')
        print('########## #################### ##########')
        print('{:^50}'.format(f'{Twhite}>>>>>>>>>> Tool by: Dr Midnight <<<<<<<<<<'))
        while True:
            alvo = input(f'\n{Twhite}\033[7mDigite o Domínio para DNS (http[s]):{VRCRM} ').strip()
            if alvo.find('http') == -1:
                print(f'{Ired}!!! {Nyellow}Domínio Inválido {Ired}!!!')
            else:
                break
        print('')
        host = socket.gethostname()
        intern = socket.gethostbyname(host)
        extern = get('https://api.ipify.org').text

        print(f'{Nyellow}Host: {Dgreen}{host}')
        print(f'{Nyellow}IP Interno: {Dgreen}{intern}')
        print(f'{Nyellow}IP Externo: {Dgreen}{extern}')
        restart = str(input(f'\n{Twhite}\033[7mDeseja realizar outra consulta S/N?{VRCRM} ')).strip().upper()[0]
        clear()
    else:
        print(f'{Ired}!!! {Nyellow}Opção Inválida {Ired}!!!')
        clear()
