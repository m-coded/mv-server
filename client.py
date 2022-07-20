import socket



host = 'local ip' 
port = 56652
respond= "quite, disconnect"

client=socket.socket()
client.connect((host,port))
msg =input(">>")
client.send(msg.encode("utf_8"))


if  msg == respond: 
 connected =False
else:
    msg= client.recv(56652).decode("utf_8")
    print(f"[server]  {msg}")
