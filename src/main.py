from blockchain.blockchain import *
from flask import Flask, request, render_template,jsonify
from flask_cors import CORS
import json

app = Flask(__name__, instance_relative_config=True)
CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blockchain',methods=['GET'])
def get_blockchain():
    response = {
        'blockchain' : blockchain.get_all_blockchain_json()
    }
    return jsonify(response),200

@app.route('/blocks/latest',methods=['GET'])
def get_latest_block():
    response={
        'block' : blockchain.get_latest_block_json()
    }
    return jsonify(response),200

@app.route('/blocks', methods=['GET'])
def get_block_by_index():
    index = request.args['index']
    response = {
        'block':blockchain.get_block_by_index(index)
    }
    return jsonify(response),200

@app.route('/transactions' , methods=['GET'])
def get_transactions():
    #TODO
    return

@app.route('/mine' , methods=['POST'])
def post_mine():
    #TODO
    pass


if __name__ == '__main__':
    blockchain = Blockchain()
    app.run()
    pass