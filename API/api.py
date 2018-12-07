import json
from flask import Flask, Response, render_template
from flask import request
from flask_cors import CORS, cross_origin
import requests
import hashlib
import datetime
import gnupg

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

privateKey=""


@app.route('/public/<email>/<palavra>', methods=['GET', 'POST'])
@cross_origin()
def chavePublica(email, palavra):
    gpg = gnupg.GPG(gnupghome='./chaves')
    input_data = gpg.gen_key_input( name_email=email, passphrase=palavra)
    key = gpg.gen_key(input_data)
    chave_public = gpg.export_keys(str(key))
    chave_privada = gpg.export_keys(str(key), True)
    global privateKey
    privateKey = chave_privada
    return json.dumps({'chave' : chave_public})

if __name__ == "__main__":
 app.run(debug=True)