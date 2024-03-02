import requests

MY_DEVICES_IP = [
    '10.30.6.24',
    '172.16.1.2',
    '172.16.1.9'
]
URL = "http://10.30.6.4:5001/api/v1"

def get_interface_status(status: int):
    if status == 1:
        return "UP"
    return "DOWN"

def get_devices():
    response = requests.get(f"{URL}/device")
    return response.json()

def print_interfaces(interfaces: list[dict]):
    for interface in interfaces:
        interface_status = get_interface_status(int(interface.get("operational_status")))
    
        print(f'[{interface_status}] Interface {interface.get("index")}: {interface.get("description")}')
        print(f'    IPv4 Address: {interface.get("ipv4_address", "N/A")}')
        print(f'    Incoming Bandwidth Per Second: {interface.get("bw_in_usage_persec")}')
        print()


devices = get_devices().get('devices')
my_devices = filter(lambda device: device.get('device_ip') in MY_DEVICES_IP, devices)

for device in my_devices:
    print(f'Device Name: {device.get("name")}')
    print(f"Device IP: {device.get('device_ip')} ({device.get('_id').get('$oid')})")
    interfaces = device.get("interfaces")
    print_interfaces(interfaces)
    print()