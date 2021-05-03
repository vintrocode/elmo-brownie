import os, json
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from eth_account import Account

def deploy_l1_erc20(w3, json_obj, acct):
    instance = w3.eth.contract(abi=json_obj['abi'], bytecode=json_obj['bytecode'])
    
    # do this to send gas for the tx
    block = w3.eth.getBlock('latest')
    gas_limit = block.gasLimit

    construct_txn = instance.constructor(
        69000,  # initial supply
        'ELMO'  # name
    ).buildTransaction({
        'from': acct.address,
        'gasPrice': w3.eth.gas_price,
        'gas': gas_limit,
        'nonce': 0,
        'chainId': 42
    })

    signed = w3.eth.account.sign_transaction(construct_txn, acct.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    addr = w3.eth.wait_for_transaction_receipt(tx_hash)['contractAddress']
    print("Layer 1 ERC20 address: " + str(addr))
    return addr

def deploy_l1_erc20_gateway(w3, elmo_1, elmo_2, json_obj, acct):
    instance = w3.eth.contract(abi=json_obj['abi'], bytecode=json_obj['bytecode'])

    # do this to send gas for the tx
    block = w3.eth.getBlock('latest')
    gas_limit = block.gasLimit

    construct_txn = instance.constructor(
        elmo_1,  # l1 erc20 addr
        elmo_2,  # l2 gateway addr
        '0x48062eD9b6488EC41c4CfbF2f568D7773819d8C9'  # address of proxy for L1 messenger
    ).buildTransaction({
        'from': acct.address,
        'gasPrice': w3.eth.gas_price,
        'gas': gas_limit,
        'nonce': 1,
        'chainId': 42
    })

    signed = w3.eth.account.sign_transaction(construct_txn, acct.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    addr = w3.eth.wait_for_transaction_receipt(tx_hash)['contractAddress']
    print("OVM_L1ERC20Gateway -- Layer 1 Gateway to L2 address: " + str(addr))
    return addr

def deploy_l2_erc20(w3, json_obj, acct):
    instance = w3.eth.contract(abi=json_obj['abi'], bytecode=json_obj['bytecode'])

    construct_txn = instance.constructor(
        '0x4200000000000000000000000000000000000007',  # l2 messenger addr
        'ELMO2'  # name
    ).buildTransaction({
        'from': acct.address,
        'gasPrice': 0,
        'nonce': 0,
        'chainId': 69
    })

    signed = w3.eth.account.sign_transaction(construct_txn, acct.key)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    addr = w3.eth.wait_for_transaction_receipt(tx_hash)['contractAddress']
    print("Layer 2 ERC20 address: " + str(addr))
    return addr




def main():

    # going to need to set the gas limit on both networks likely, brownie only does 1
    

    # intialize web3 providers
    web3_l1 = Web3(Web3.HTTPProvider(os.environ['PROVIDER_KOVAN']))
    web3_l2 = Web3(Web3.HTTPProvider('https://kovan.optimism.io'))

    assert web3_l1.isConnected()
    print("Layer 1 Connected")
    assert web3_l2.isConnected()
    print("Layer 2 Connected")


    # configure the L1 & L2 middleware, need to be connected to networks first
    acct_l1 = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530') 
    web3_l1.middleware_onion.add(construct_sign_and_send_raw_middleware(acct_l1))
    web3_l1.eth.default_account = acct_l1.address

    # fund the random account on L1 with kETH from your kovan acct -- make sure you've got kETH, if not google "kovan faucet"
    funding_txn = web3_l1.eth.account.sign_transaction({
        'nonce': web3_l1.eth.get_transaction_count(os.environ['METAMASK_PUBLIC_ADDRESS']),
        'gasPrice': web3_l1.eth.gas_price,
        'gas': 100000,
        'to': acct_l1.address,
        'value': web3_l1.toWei(0.05,'ether')
    },
    os.environ['METAMASK_SECRET_KEY'])
    tx_hash = web3_l1.eth.send_raw_transaction(funding_txn.rawTransaction)
    web3_l1.eth.wait_for_transaction_receipt(tx_hash)
    print('Money sent from your Metamask to ' + str(acct_l1.address) + " successfully!")

    # configure the L2 middlware account
    acct_l2 = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
    web3_l2.middleware_onion.add(construct_sign_and_send_raw_middleware(acct_l2))
    web3_l2.eth.default_account = acct_l2.address

    print("L1 middleware default account: " + str(web3_l1.eth.default_account))
    print("L2 middleware default account: " + str(web3_l2.eth.default_account))

    # read the components in
    # NOTE: can't use brownie here as the bytecode will differ per compiler (EVM/OVM)

    # L1 ERC20 -- artifacts/
    with open('./client/src/artifacts/contracts/ERC20.json') as f:
        erc20_l1 = json.load(f)

    # L2 ERC20 -- look in the artifacts-ovm folder!!!
    with open('./client/src/artifacts-ovm/contracts/L2DepositedERC20.sol/L2DepositedERC20.json') as f:
        erc20_l2 = json.load(f)

    # L1 ERC20 Gateway
    with open('./node_modules/@eth-optimism/contracts/artifacts/contracts/optimistic-ethereum/OVM/bridge/tokens/OVM_L1ERC20Gateway.sol/OVM_L1ERC20Gateway.json') as f:
        l1_erc20_gateway = json.load(f)

    

    print("Artifacts loaded")

    # deploy the contracts
    elmo_1 = deploy_l1_erc20(web3_l1, erc20_l1, acct_l1)
    elmo_2 = deploy_l2_erc20(web3_l2, erc20_l2, acct_l2)
    elmo_gateway = deploy_l1_erc20_gateway(web3_l1, elmo_1, elmo_2, l1_erc20_gateway, acct_l1)

    # create deployed contract objects
    elmo1 = web3_l1.eth.contract(abi=erc20_l1['abi'], address=elmo_1)
    elmo2 = web3_l2.eth.contract(abi=erc20_l2['abi'], address=elmo_2)
    elmoGateway = web3_l1.eth.contract(abi=l1_erc20_gateway['abi'], address=elmo_gateway)



    print("Deploys successful. Send some bread to the boys...")
    # Alex: 0x595b57BA293565b65CfB0b0b0e757B88Ad788b4a
    # RJ: 0x81431b69B1e0E334d4161A13C2955e0f3599381e
    # Ben: 0xEd9A98c2ea26705CDA86d7D5399b50C53270Cc91
    # Vince: 0x22C74a95c53FD6cFB886B37FFCEDB6FEedbE2023

    the_boys = {
        'Alex': '0x595b57BA293565b65CfB0b0b0e757B88Ad788b4a', 
        'RJ': '0x81431b69B1e0E334d4161A13C2955e0f3599381e', 
        'Ben': '0xEd9A98c2ea26705CDA86d7D5399b50C53270Cc91', 
        'Vince': '0x22C74a95c53FD6cFB886B37FFCEDB6FEedbE2023'
    }

    for boi in the_boys:
        addr = the_boys[boi]
        # Send Elmo1
        tx_hash = elmo1.functions.transfer(addr, 10000).transact({'from': acct_l1.address})
        tx_receipt = web3_l1.eth.wait_for_transaction_receipt(tx_hash)
        boi_bal = elmo1.functions.balanceOf(addr).call()
        print("YO " + str(boi) + " YOU JUST GOT " + str(boi_bal) + " MOTHAF*KIN ELMO (!!!)")
    
    print("AAAHHH LET'S GO WE'RE DONE BABYYYYY")




if __name__ == '__main__':
    main()