import os, json
from web3 import Web3
from brownie import ERC20, L2DepositedERC20


def deploy_contract(w3, abi, bytecode):
    tx_hash = w3.eth.contract(abi, bytecode).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

def main():
    # intialize web3 providers
    web3_l1 = Web3(Web3.HTTPProvider(os.environ['PROVIDER_KOVAN']))
    web3_l2 = Web3(Web3.HTTPProvider('https://kovan.optimism.io'))

    assert web3_l1.isConnected()
    assert web3_l2.isConnected()

    # need the ABI and bytecode for each of the following contracts:
    #   ERC20.sol -- token
    #   L2DepositedERC20.sol -- gateway
    # all are accessible via the brownie contract objects

    addr_token_l1 = deploy_contract(web3_l1, ERC20.abi, ERC20.bytecode)

    print('Done!')
