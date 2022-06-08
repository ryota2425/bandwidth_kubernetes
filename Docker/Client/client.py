from prometheus_client import start_http_server, Summary
import random
import time
import os

from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import json
import subprocess
from subprocess import PIPE

# Create a metric to track time spent and requests made.
registry = CollectorRegistry()
bandwidth_sender = Gauge('my_bandwidth_sender', 'iperf3_bandwidth_sender',registry=registry)
bandwidth_receiver = Gauge('my_bandwidth_receiver', 'iperf3_bandwidth_receiver',registry=registry)
#downTime = Gauge('my_speed_test_result_upload', 'speed_test')

# サブプロセスを呼ぶところ
# iperf3 -c 192.168.30.80 -J -f "m" --get-server-output
IPaddr = os.environ.get('SERVER_IP',"192.168.30.80")#
IPport = os.environ.get('SERVER_PORT',"31113")
IPaddr_upload = os.environ.get('UPLOAD_IP',"192.168.30.50:30011")#
def run_iperf3_server():
    print("start iperf subprocess")
    process = subprocess.run(['iperf3', '-c', IPaddr ,'-J',"--port",IPport], stdout=PIPE, stderr=PIPE)
    return json.loads(process.stdout)


def bit_to_mbit(bit):
    return bit / 1024 / 1024

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    print("start Program")
    #start_http_server(8001)
    while True:
        try:
        #計測
            print("starting iperf3 test")
            result = run_iperf3_server()
            #print(result)
            #結果
            print("sender",bit_to_mbit(result["end"]["streams"][0]["sender"]["bits_per_second"])) #["streams"]["receiver"]["sum_sent"]
            print("receiver",bit_to_mbit(result["end"]["streams"][0]["receiver"]["bits_per_second"]))

            #公開
            bandwidth_sender.set(bit_to_mbit(result["end"]["streams"][0]["sender"]["bits_per_second"]))
            bandwidth_receiver.set(bit_to_mbit(result["end"]["streams"][0]["receiver"]["bits_per_second"]))
            push_to_gateway(IPaddr_upload, job='batch_bandwidth', registry=registry)
            #downTime.set(bit_to_mbit(result["upload"]))
        except Exception as e:
            print(e)
            time.sleep(60*1)
        #待機
        time.sleep(60*1)
