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

def get_path(src_ip: str, dst_ip: str):
    response = requests.get(f"{URL}/path/{src_ip},{dst_ip}")
    return response.json()

def traceroute(src_ip: str, dst_ip: str):
    result = get_path(src_ip, dst_ip)

    print(f"There are {len(result.get('paths'))} possible paths.")

    for path in result.get('paths'):
        print(f"Path: {path.get('path')}")
    
    print()

traceroute('192.168.1.1', '192.168.1.129')
traceroute('192.168.1.65', '192.168.1.129')