import os
from brownie import ERC20, L2DepositedERC20, accounts, network

def main():
    
    print(network.show_active())
    network.gas_limit(10000000)

    accounts.add(os.environ['METAMASK_SECRET_KEY'])
    accounts.default = accounts[1]
    ERC20.deploy(1337, 'ELMO', {'from': accounts.default})
