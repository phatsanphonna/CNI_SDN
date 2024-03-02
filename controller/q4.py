# Change route path

import requests

URL = "http://10.30.6.4:5001/api/v1"
R2_DEVICE_ID = '65d7385dd2d3fd619292be25'

def goto_lb3_via_r2():
    source_nw_addr = '192.168.1.0'
    destination_nw_addr = '192.168.2.128'
    next_hop_addr = '10.0.8.1'

    actions = [
        {
            'device_id': R2_DEVICE_ID,
            'action': 2,
            'data': next_hop_addr
        }
    ]
    payload = {
        'name': 'Change route path from G1-R2-L1 to G2-R3-L3',
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

def goto_lb3_via_r3():
    source_nw_addr = '192.168.1.64'
    destination_nw_addr = '192.168.2.128'
    next_hop_addr = '172.16.1.4'

    actions = [
        {
            'device_id': R2_DEVICE_ID,
            'action': 2,
            'data': next_hop_addr
        }
    ]
    payload = {
        'name': 'Change route path from G1-R2-L2 to G2-R3-L3',
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

goto_lb3_via_r2()
goto_lb3_via_r3()