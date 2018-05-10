from blockchain.blockchain import *
from transaction.transaction import *
from wallet.wallet import *
from flask import Flask, request, render_template,jsonify
from flask_cors import CORS
import json

app = Flask(__name__, instance_relative_config=True)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/blockchain',methods=['GET'])
def get_blockchain():
    response = {
        'blockchain' : blockchain.get_all_blockchain_json()
    }
    return jsonify(response),200

@app.route('/api/blocks/latest',methods=['GET'])
def get_latest_block():
    response={
        'block' : blockchain.get_latest_block_json()
    }
    return jsonify(response),200

@app.route('/api/blocks', methods=['GET'])
def get_block_by_index():
    index = request.args['index']
    response = {
        'block':blockchain.get_block_by_index_json(index)
    }
    return jsonify(response),200

@app.route('/api/transactions' , methods=['GET'])
def get_transactions():
    #TODO
    return

@app.route('/api/mine' , methods=['POST'])
def post_mine():
    #TODO
    pass

@app.route('/api/wallets/generate',methods=['GET'])
def generate_wallet():
    wallet = Wallet()
    wallet.generate_wallet('Password')
    response = {
        'keys': wallet.get_wallet_keys_json()
    }
    return jsonify(response),200


if __name__ == '__main__':
    blockchain = Blockchain()
    app.run()
    pass