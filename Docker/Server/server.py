from prometheus_client import start_http_server, Summary
import random
import time
from prometheus_client import Gauge
import json
import subprocess
from subprocess import PIPE
import os


# Create a metric to track time spent and requests made.
#upTime = Gauge('my_speed_test_result_download', 'speed_test')
#downTime = Gauge('my_speed_test_result_upload', 'speed_test')

# サブプロセスを呼ぶところ
IPport = os.environ.get('SERVER_PORT',"31113")
def run_iperf3_server():
    print("start iperf3 subprocess")
    process = subprocess.run(['iperf3', '-s', '-J','-1',"--port",IPport], stdout=PIPE, stderr=PIPE)
    return json.loads(process.stdout)


def bit_to_mbit(bit):
    return bit / 1024 / 1024

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    print("start Program")
    #start_http_server(8001)
    while True:
        #計測
        try:
            print("starting iperf3 test")
            result = run_iperf3_server()
            print(result)
        except Exception as e:
            print(e)
            time.sleep(60*1)
        #結果
        #print(bit_to_mbit(result["download"]), bit_to_mbit(result["upload"]))
        #公開
        #upTime.set(bit_to_mbit(result["download"]))
        #downTime.set(bit_to_mbit(result["upload"]))
        #待機
        time.sleep(10)