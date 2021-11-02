from flask import Flask, request
import json
import service as service

app = Flask(__name__)


@app.route('/key', methods=["Get"])
def fetch_key():
    result = {'key': str(service.fetch_key())}
    return json.dumps(result)


@app.route('/encrypt', methods=["post"])
def encrypt_file():
    data = request.get_json()
    s = {'encrypt_data': str(service.encrypt_file(data['content'], data['key']))}
    return json.dumps(s)


@app.route('/decrypt', methods=["post"])
def decrypt_file():
    data = request.get_json()
    result = service.decrypt_file(bytes(data['content'], 'utf-8'), data['key'])
    s = {'decrypt_data': result}
    return json.dumps(s)


if __name__ == "__main__":
    app.run()
