from flask import Flask, jsonify
import psutil
# Optional: For Wi-Fi-specific data
# import pywifi
# from pywifi import const

app = Flask(__name__)

@app.route('/wifi-data', methods=['GET'])
def get_wifi_data():
    wifi_info = {}
    stats = psutil.net_if_stats()
    print(stats)  # Add this line to check what data you're getting
    for interface, data in stats.items():
        wifi_info[interface] = {
            "is_up": data.isup,
            "speed": data.speed,
            "duplex": data.duplex,
            "mtu": data.mtu
        }
    return jsonify(wifi_info)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)


#OUTPUT

# {
#   "Ethernet": {
#     "duplex": 2,
#     "is_up": true,
#     "mtu": 1500,
#     "speed": 100
#   },
#   "Loopback Pseudo-Interface 1": {
#     "duplex": 2,
#     "is_up": true,
#     "mtu": 1500,
#     "speed": 1073
#   }
# }
# 1.  Ethernet :
#    -  duplex :  full-duplex, meaning the device can send and receive data simultaneously.
#    -  is_up : Ethernet interface is currently active and up.
#    -  mtu : Maximum packet size that can be transmitted over this network.[ maximum transmission unit]
#    -  speed :  Speed of 100 Mbps.

# 2.  Loopback Pseudo-Interface 1 :
#    - This is a virtual network interface used for internal communication (the loopback interface).
#    -  duplex :   2   (full-duplex).
#    -  is_up :   true   indicates the loopback interface is up.
#    -  mtu :   1500  , standard for Ethernet networks.
#    -  speed :   1073   is the speed of the loopback interface (this is generally a software interface, so the speed can vary).
