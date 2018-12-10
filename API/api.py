import json
from flask import Flask, Response, render_template, jsonify
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

@app.route('/importar', methods=['POST'])
@cross_origin()
def importarChave():
    gpg = gnupg.GPG(gnupghome='./chaves')
    key_data = request.form['chaveImportar']
    import_result = gpg.import_keys(key_data)
    return ""

@app.route('/listar', methods=['GET'])
@cross_origin()
def listarChaves():
    gpg = gnupg.GPG(gnupghome='./chaves')
    public_keys = gpg.list_keys()
    emails = []
    for i in public_keys:
        emails.append({'email' : str(i['uids']).split("<")[1][:-3]})
    return jsonify(emails)


@app.route('/criptografar', methods=['POST'])
@cross_origin()
def criptografar():
    gpg = gnupg.GPG(gnupghome='./chaves')
    texto = request.form['texto']
    email = request.form['email']
    encrypted_data = gpg.encrypt(texto, email)
    if encrypted_data.ok == True:
        return jsonify({'mensagem' : str(encrypted_data)})
    return jsonify({'mensagem' : 'Incapaz de criptografar usando essa chave publica.'})
    

if __name__ == "__main__":
 app.run(debug=True)