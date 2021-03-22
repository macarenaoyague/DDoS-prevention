from flask import Flask, request
from multiprocessing import Value

counters = {}
threshold = 10
app = Flask(__name__)

def initialize_dic():
    return {'GET': 0, 'POST': 0}

def check_threshold_get(source_ip):
    if counters[source_ip]['GET'] > threshold:
        print(f"{source_ip} has surpassed the threshhold")
        return True
    return False

def check_threshold_post(source_ip):
    if counters[source_ip]['POST'] > threshold:
        print(f"{source_ip} has surpassed the threshhold")
        return True
    return False

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/backend', methods = ['GET'])
def get_test():
    global counters
    if request.remote_addr not in counters:
        counters[request.remote_addr] = initialize_dic()
    counters[request.remote_addr]['GET'] += 1
    print(counters[request.remote_addr])
    print(request.remote_addr)
    check_threshold_get(request.remote_addr)
    return "xd"

@app.route('/backend', methods = ['POST'])
def post_test():
    global counters
    if request.remote_addr not in counters:
        counters[request.remote_addr] = initialize_dic()
    counters[request.remote_addr]['POST'] += 1
    print(counters[request.remote_addr])
    print(request.remote_addr)
    check_threshold_post(request.remote_addr)
    return "xd"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))