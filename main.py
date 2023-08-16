import os
import json
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('HOST')
host, port = host.split(":")
port = int(port)

token = os.getenv('TOKEN')

isp_list = os.getenv('ISP_LIST').split(',')
print(isp_list)

app = Flask(__name__)

@app.route("/check", methods=['POST'])
def check():
    assert token == request.headers.get('Authorization').split(' ')[-1]
    data = json.loads(request.data)
    print(data)
    result = data.get('isDebugMode') and data.get('offer') != data.get('gpRedirect') and data.get('isp') in isp_list
    return json.dumps({
        "result": bool(result)
    })

app.run(host, port)