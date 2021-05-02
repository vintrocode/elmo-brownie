import os, json
from web3 import Web3
from brownie import ERC20, L2DepositedERC20, accounts


def main():

    # set up the accounts
    accounts.add(os.environ['METAMASK_SECRET_KEY'])
    accounts.default = accounts[1]

    # intialize web3 providers
    web3_l1 = Web3(Web3.HTTPProvider(os.environ['PROVIDER_KOVAN']))
    web3_l2 = Web3(Web3.HTTPProvider('https://kovan.optimism.io'))

    assert web3_l1.isConnected()
    assert web3_l2.isConnected()

    # need the ABI and bytecode for each of the following contracts:
    #   ERC20.sol -- token
    #   L2DepositedERC20.sol -- gateway
    # all are accessible via the brownie contract objects
    
    # deploy the L1 token
    tx_hash = web3_l1.eth.contract(
        abi=ERC20.abi, 
        bytecode=ERC20.bytecode).constructor(
            69000,
            'ELMO',
        ).transact(
            {'from': str(accounts.default)}
        )
    addr_token_l1 = web3_l1.eth.get_transaction_receipt(tx_hash)['contractAddress']

    print('Done!')
