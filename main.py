from telnetlib import Telnet

IP_ADDRESS = '10.30.6.120'

def main():
    client = Telnet(IP_ADDRESS)
    print(client.read_all())
    client.close()

main()
