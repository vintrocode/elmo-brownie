import os, json
from web3 import Web3

# intialize web3 providers
web3_l1 = Web3(Web3.HTTPProvider(os.environ['PROVIDER_KOVAN']))
web3_l2 = Web3(Web3.HTTPProvider('https://kovan.optimism.io'))

assert web3_l1.isConnected()
print("Layer 1 Connected")
assert web3_l2.isConnected()
print("Layer 2 Connected")

# set default account so we don't have to build txns? idk
web3_l1.eth.defaultAccount = os.environ['METAMASK_PUBLIC_ADDRESS']


# L1 ERC20 -- artifacts/
with open('./client/src/artifacts/contracts/ERC20.json') as f:
    erc20_l1 = json.load(f)

# L2 ERC20 -- look in the artifacts-ovm folder!!!
with open('./client/src/artifacts-ovm/contracts/L2DepositedERC20.sol/L2DepositedERC20.json') as f:
    erc20_l2 = json.load(f)

# L1 ERC20 Gateway
with open('./node_modules/@eth-optimism/contracts/artifacts/contracts/optimistic-ethereum/OVM/bridge/tokens/OVM_L1ERC20Gateway.sol/OVM_L1ERC20Gateway.json') as f:
    l1_erc20_gateway = json.load(f)


# create deployed contract objects
elmo1 = web3_l1.eth.contract(abi=erc20_l1['abi'], address='0xe4c6a43edd78fa0F072dD12660c321bfDAb43210')
elmo2 = web3_l2.eth.contract(abi=erc20_l2['abi'], address='0x516b825146D217e1cF3aE6da51D577fEb3f998a0')
elmoGateway = web3_l1.eth.contract(abi=l1_erc20_gateway['abi'], address='0xE8CB48f2B992F1E988917c05EE04BB58521bbC97')

# approve the tokens for depositing
tx0 = elmo1.functions.approve(elmoGateway.address, 1234).buildTransaction(
    {
        'nonce': web3_l1.eth.get_transaction_count(os.environ['METAMASK_PUBLIC_ADDRESS']),
        'from': os.environ['METAMASK_PUBLIC_ADDRESS']
    }
)
signed0 = web3_l1.eth.account.sign_transaction(tx0, os.environ['METAMASK_SECRET_KEY'])
tx0_hash = web3_l1.eth.send_raw_transaction(signed0.rawTransaction)
assert web3_l1.eth.wait_for_transaction_receipt(tx0_hash)['status'] == 1, 'Transaction reverted'

# deposit tokens into the gateway
elmoGateway.functions.deposit(1234).call()
print(tx1)