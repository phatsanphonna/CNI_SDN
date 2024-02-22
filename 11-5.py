from telnetlib import Telnet
import time

IP_ADDRESS = '10.30.6.24'
USERNAME = 'cisco'
PASSWORD = 'cisco'

client = Telnet(IP_ADDRESS)

def connect():
    print('Connecting...')
    client.read_until(b"Username: ")
    client.write(USERNAME.encode('ascii') + b"\n")

    if PASSWORD:
        client.read_until(b"Password: ")
        client.write(PASSWORD.encode('ascii') + b"\n")
    
    client.read_until(b"#")
    print('Connected')

def disconnect():
    client.write(b"exit\n")
    client.read_all()

final_output = ''

connect()
client.write(b"telnet 172.16.1.2\n")
connect()

client.write(b"traceroute 192.168.1.129 source 192.168.1.1\n")
final_output += client.read_until(b"#").decode('utf-8')

print('Done Traceroute')

print(final_output)