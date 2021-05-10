import json, os
from brownie import *


def main():
    # add your metamask to brownie
    accounts.add(private_key=os.environ['METAMASK_SECRET_KEY'])

    # brownie runs on kovan, it has the L1 ERC20 loaded

    # L1 ERC20 Gateway
    with open('./node_modules/@eth-optimism/contracts/artifacts/contracts/optimistic-ethereum/OVM/bridge/tokens/OVM_L1ERC20Gateway.sol/OVM_L1ERC20Gateway.json') as f:
        l1_erc20_gateway = json.load(f)

    # create elmoGateway 
    elmoGateway = Contract.from_abi(
        'elmoGateway', 
        '0xE8CB48f2B992F1E988917c05EE04BB58521bbC97', 
        l1_erc20_gateway['abi']
    )

    elmoGateway.deposit(1234, 
    {
        'from': accounts[0],
        'gas': 1000000,
        'allow_revert': True
    })

