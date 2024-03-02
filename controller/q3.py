# Change route path

import requests

URL = "http://10.30.6.4:5001/api/v1"
R2_DEVICE_ID = '65d7385dd2d3fd619292be25'

source_nw_addr = '192.168.1.64'
destination_nw_addr = '192.168.1.128'
next_hop_addr = '172.16.1.1'

actions = [
    {
        'device_id': R2_DEVICE_ID,
        'action': 2,
        'data': next_hop_addr
    }
]
payload = {
    'name': 'Change route path from R2-L2 to R3-L3',
    'src_ip': source_nw_addr,
    'src_port': 'any',
    'src_subnet': '0.0.0.63',
    'dst_ip': destination_nw_addr,
    'dst_port': 'any',
    'dst_subnet': '0.0.0.63',
    'actions': actions
}

response = requests.post(f"{URL}/flow/routing", json=payload)
print(response.json())