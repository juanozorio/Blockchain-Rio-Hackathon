from flask import Flask, request, jsonify
from service.ProjectService import ProjectService
from collections import OrderedDict
import datetime
from web3 import Web3
import os

app = Flask(__name__)
service = ProjectService()
# Configurações da conexão Web3
infura_url = 'https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Endereço e ABI do contrato Chainlink
contract_address = '0xYourContractAddress'
contract_abi = [
			{
				"inputs": [
					{
						"internalType": "address",
						"name": "_platformWallet",
						"type": "address"
					}
				],
				"stateMutability": "nonpayable",
				"type": "constructor"
			},
			{
				"inputs": [],
				"name": "TAX_RATE",
				"outputs": [
					{
						"internalType": "uint256",
						"name": "",
						"type": "uint256"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "address payable",
						"name": "projectWallet",
						"type": "address"
					},
					{
						"internalType": "bool",
						"name": "isSocialProject",
						"type": "bool"
					}
				],
				"name": "donate",
				"outputs": [],
				"stateMutability": "payable",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "platformWallet",
				"outputs": [
					{
						"internalType": "address",
						"name": "",
						"type": "address"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"stateMutability": "payable",
				"type": "receive"
			}
		]  # ABI do seu contrato
# Inicializar contrato
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def format_project(project):
    return OrderedDict([
        ('id', project.id),
        ('name', project.name),
        ('icon', project.icon),
        ('banner', project.banner),
        ('wallet', project.wallet),
        ('bio', project.bio),
        ('project_type', project.project_type),
        ('description', project.description),
        ('created_at', project.created_at.isoformat() if isinstance(project.created_at, datetime.datetime) else project.created_at),
        ('updated_at', project.updated_at.isoformat() if isinstance(project.updated_at, datetime.datetime) else project.updated_at),
    ])

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    try:
        project_id = service.create_project(
            name=data['name'],
            icon=data.get('icon', ''),
            banner=data.get('banner', ''),
            wallet=data['wallet'],
            bio=data.get('bio', ''),
            project_type=data['project_type'],
            description=data.get('description', '')
        )
        return jsonify({'id': project_id}), 201
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 400
    
@app.route('/validate_wallet', methods=['POST'])
def validate_wallet():
    data = request.json
    project_id = data['project_id']
    
    try:
        # Buscar a carteira do projeto do banco de dados
        project_wallet = service.get_project_wallet(project_id)
        
        # Verificar a carteira com Chainlink (chamar função do contrato)
        tx_hash = contract.functions.requestProjectWalletValidation(project_id).transact({
            'from': '0xYourWalletAddress',
            'gas': 3000000,
            'value': web3.toWei('0.1', 'ether')  # Exemplo de taxa
        })
        
        # Aguardar a confirmação da transação
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)
        
        if receipt.status:
            return jsonify({'wallet': project_wallet, 'status': 'validated'}), 200
        else:
            return jsonify({'error': 'Validation failed'}), 400
        
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 400
    
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = service.get_project(project_id)
    if project:
        return jsonify(format_project(project)), 200
    return jsonify({'error': 'Project not found'}), 404

@app.route('/projects', methods=['GET'])
def get_all_projects():
    projects = service.get_all_projects()
    return jsonify([format_project(project) for project in projects]), 200

@app.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    service.update_project(
        project_id,
        name=data['name'],
        icon=data.get('icon', ''),
        banner=data.get('banner', ''),
        wallet=data['wallet'],
        bio=data.get('bio', ''),
        project_type=data['project_type'],
        description=data.get('description', '')
    )
    project = service.get_project(project_id)
    return jsonify(format_project(project)), 200

@app.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    service.delete_project(project_id)
    return jsonify({'message': 'Project deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
