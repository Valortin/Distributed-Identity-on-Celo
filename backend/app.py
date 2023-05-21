# app.py

from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to the Ethereum network
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load the contract ABI
# Connect to the deployed smart contract
contract_address = '0x1234567890abcdef...'
contract_abi = [
    # Insert the ABI of your smart contract here
]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Implement backend logic for user registration
def register_user(username, password):
    # Encode the function call to registerUser in the smart contract
    tx_hash = contract.functions.registerUser(username, password).transact()

    # Wait for the transaction to be mined
    w3.eth.waitForTransactionReceipt(tx_hash)

    # Process the transaction receipt as needed

# Implement backend logic for user authentication
def authenticate_user(username, password):
    # Encode the function call to authenticateUser in the smart contract
    result = contract.functions.authenticateUser(username, password).call()

    # Process the result and return authentication status

@app.route('/register', methods=['POST'])
def handle_register():
    username = request.json['username']
    password = request.json['password']

    register_user(username, password)
    return jsonify({'message': 'User registered successfully'})

@app.route('/authenticate', methods=['POST'])
def handle_authenticate():
    username = request.json['username']
    password = request.json['password']

    authenticated = authenticate_user(username, password)
    return jsonify({'authenticated': authenticated})

if __name__ == '__main__':
    app.run()
