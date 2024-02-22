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


def use_prompt():
    client.read_until(b"#")

    while True:
        prompt = input()

        if (prompt == "closee"):
            disconnect()
            break
        
        client.write(prompt.encode('ascii') + b"\n")

        if prompt.startswith('telnet'):
            connect()
            continue

        print(client.read_until(b"#").decode('utf-8'))

def use_script(filename: str):
    output_filename = "Device_" + IP_ADDRESS + str(time.time()) + '.txt'
    script_list = open(filename, 'r')
    final_output = ''

    for line in script_list:
        client.write(line.encode('ascii'))

        if line.startswith('telnet'):
            connect()
            continue

        device_config = client.read_until(b"#").decode('utf-8')
        final_output += device_config
        print(final_output)

    script_list.close()

    saveoutput = open(output_filename,"w")
    saveoutput.write(final_output)
    saveoutput.close()

    print("Output File: " + output_filename)

connect()
use_script('script.txt')
# use_script('script.txt')
