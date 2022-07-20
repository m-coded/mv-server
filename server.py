import socket
import  threading 
import pyfiglet
from colorama import Fore, Back, Style


ascii_banner = pyfiglet.figlet_format('''''''''''''''"MV SERVER"''''''''')
print(Fore.GREEN,ascii_banner)

def color():
    name =''
tile='''
  [+]#######################################################################[+]                                                                                                                                                 
  [+]  Tool created by marvez vz2 will  be  comming with crypter fud!!      [+]
  [+]                                                                       [+]
  [+]   contact[+]marvez@protonmail.com/[+]dicord/subject101                [+]
  [+]#######################################################################[+]
'''

print(Fore.WHITE, tile)
color()




host = 'local ip' 
port = 56653
respond= "quite, disconnect"


def handle_client(conn,addr):
    print(f"[+]NEW  CONNECTION ADDING {addr}")

    connected =True
    while connected:
        meg = conn.rec(1024).decode("utf_8")
        if  meg  == respond:
            connected = False
        print(f"{addr} and {meg}"  )
        meg =f"got  message  from  {meg}"
        conn.send(meg.encode("uft_8"))
        conn.close()

def con():
    print("[+]SEVER CONNECTION AS  STARTED")
server =socket.socket()
server.bind((host,port))
server.listen()
print("[+[SERVER]]server waiting for incomming connection from ",{host})

while True:

 conn, addr = server.accept()
 thread = threading.thread(target= handle_client, agrs=(conn, addr))
 thread.start()
 print("[+]CONNECTION  AS  BEEN ESTERBLISHED  FROM " , {host})
 print(f"[+]ACTIVE CONNECTION {threading.activeCount()-1}")

 message = "hello"
 server.send(message.encode)

 if __name__== " _main_ ":
    conn()
    handle_client()
